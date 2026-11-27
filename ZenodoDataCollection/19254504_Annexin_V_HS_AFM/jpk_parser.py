"""
JPK (Bruker NanoRacer) AFM file parser.

JPK files are big-endian TIFF files with proprietary tag extensions.
Each IFD stores one imaging channel (height, amplitude, phase, etc.)
as 32-bit signed integers, with linear calibration stored in custom tags.

Tag reference (JPK-specific tags, all big-endian):
  0x8000  software version
  0x8003  scan start timestamp
  0x8006  scan end timestamp
  0x8017  full instrument metadata (Java-properties key-value text)
  0x8046  image width  (pixels)
  0x8047  image height (pixels)
  0x8081  channel logical name
  0x8100  channel display name
  0x8102  physical unit
  0x8103  scaling type (NullScaling / LinearScaling)
  0x8104  linear scale factor (float64)
  0x8105  linear scale offset (float64)
"""

import struct
import sys
from pathlib import Path


# ── low-level TIFF helpers (big-endian) ──────────────────────────────────────

def _u16(data, off):  return struct.unpack_from(">H", data, off)[0]
def _u32(data, off):  return struct.unpack_from(">I", data, off)[0]
def _i32(data, off):  return struct.unpack_from(">i", data, off)[0]
def _f64(data, off):  return struct.unpack_from(">d", data, off)[0]
def _ascii(data, off, n): return data[off:off+n].decode("ascii", errors="replace").strip("\x00")

_TYPE_SIZES = {1:1, 2:1, 3:2, 4:4, 5:8, 6:1, 7:1, 8:2, 9:4, 10:8, 11:4, 12:8}
_TYPE_NAMES = {1:"BYTE", 2:"ASCII", 3:"SHORT", 4:"LONG", 5:"RATIONAL",
               6:"SBYTE", 7:"UNDEF", 8:"SSHORT", 9:"SLONG", 10:"SRATIONAL",
               11:"FLOAT", 12:"DOUBLE"}


def _read_tag_value(data, typ, cnt, voff):
    """Return the typed value(s) for one IFD entry."""
    tname  = _TYPE_NAMES.get(typ, "UNKNOWN")
    tsize  = _TYPE_SIZES.get(typ, 1)
    total  = tsize * cnt

    # Values that fit in 4 bytes are stored inline (left-aligned, big-endian).
    if total <= 4:
        raw = struct.pack(">I", voff)[:total]
        data_src = raw
        abs_off  = 0
    else:
        data_src = data
        abs_off  = voff

    if tname == "ASCII":
        return _ascii(data_src, abs_off, cnt)
    if tname in ("SHORT", "SSHORT"):
        fmt = f">{cnt}{'H' if tname=='SHORT' else 'h'}"
        vals = struct.unpack_from(fmt, data_src, abs_off)
        return vals[0] if cnt == 1 else list(vals)
    if tname in ("LONG", "SLONG"):
        fmt = f">{cnt}{'I' if tname=='LONG' else 'i'}"
        vals = struct.unpack_from(fmt, data_src, abs_off)
        return vals[0] if cnt == 1 else list(vals)
    if tname == "DOUBLE":
        vals = [_f64(data_src, abs_off + i*8) for i in range(cnt)]
        return vals[0] if cnt == 1 else vals
    return data_src[abs_off:abs_off+min(total, 64)].hex()


def _parse_ifd(data, ifd_off):
    """Return a dict {tag_int: value} for one IFD."""
    n = _u16(data, ifd_off)
    tags = {}
    for i in range(n):
        e   = ifd_off + 2 + i * 12
        tag = _u16(data, e)
        typ = _u16(data, e + 2)
        cnt = _u32(data, e + 4)
        vof = _u32(data, e + 8)
        tags[tag] = _read_tag_value(data, typ, cnt, vof)
    next_ifd = _u32(data, ifd_off + 2 + n * 12)
    return tags, next_ifd


def _read_strips(data, tags):
    """Assemble and decode strip data into a flat list of int32 values."""
    strip_offsets = tags.get(0x0111, [])
    strip_counts  = tags.get(0x0117, [])
    if isinstance(strip_offsets, int):
        strip_offsets = [strip_offsets]
        strip_counts  = [strip_counts]

    raw = bytearray()
    for off, cnt in zip(strip_offsets, strip_counts):
        raw.extend(data[off:off+cnt])

    bps = tags.get(0x0102, 16)
    n_pixels = len(raw) // (bps // 8)
    fmt = f">{n_pixels}{'i' if bps == 32 else 'h'}"
    return list(struct.unpack(fmt, bytes(raw)))


# ── per-channel calibration ───────────────────────────────────────────────────

def _calibrate(raw_values, tags):
    """
    Apply linear calibration: physical = scale * raw + offset.

    Tag 0x8103 / 0x8033 selects the conversion type.  If 'LinearScaling',
    tags 0x8104 and 0x8105 hold scale and offset respectively.
    """
    scaling = tags.get(0x8103, "NullScaling")
    if scaling == "LinearScaling":
        scale  = tags.get(0x8104, 1.0)
        offset = tags.get(0x8105, 0.0)
        return [scale * v + offset for v in raw_values]
    return list(raw_values)


# ── public interface ──────────────────────────────────────────────────────────

def parse_jpk(filepath):
    """
    Parse a JPK AFM file and return a dict with instrument metadata and
    a list of imaging channels.

    Returns
    -------
    {
        "file": str,
        "instrument": {
            "software_version": str,
            "scan_start": str,
            "scan_end": str,
            "timestamp_ms": str,
            "session_id": str,
            "feedback_mode": str,
            "scan_rate_hz": float,
            "scan_size_x_m": float,
            "scan_size_y_m": float,
            "image_pixels_x": int,
            "image_pixels_y": int,
            "scan_direction": str,
            "full_metadata": str,
        },
        "cantilever": {
            "name": str,
            "spring_constant_Nm": float,
            "sensitivity_nmV": float,
            "resonance_freq_Hz": float,
            "q_factor": float,
            "environment": str,
        },
        "channels": [
            {
                "index": int,
                "logical_name": str,
                "display_name": str,
                "unit": str,
                "scaling": str,
                "scale_factor": float,
                "offset": float,
                "width": int,
                "height": int,
                "data_raw": list[int],
                "data_calibrated": list[float],
                "data_2d": list[list[float]],   # row-major, calibrated
            }, ...
        ]
    }
    """
    filepath = Path(filepath)
    with open(filepath, "rb") as fh:
        data = fh.read()

    # Validate TIFF magic
    if data[0:2] != b"MM":
        raise ValueError("Not a big-endian TIFF / JPK file.")
    if _u16(data, 2) != 42:
        raise ValueError("TIFF magic number mismatch.")

    # Walk all IFDs
    ifd_off = _u32(data, 4)
    ifds    = []
    while ifd_off:
        tags, ifd_off = _parse_ifd(data, ifd_off)
        ifds.append(tags)

    # IFD 0 carries the global instrument metadata
    meta_tags = ifds[0]
    full_meta = meta_tags.get(0x8017, "")

    def _meta_get(key):
        for line in full_meta.splitlines():
            if line.strip().startswith(key + " :"):
                return line.split(" : ", 1)[1].strip()
        return ""

    result = {
        "file": str(filepath),
        "instrument": {
            "software_version":  meta_tags.get(0x8000, ""),
            "scan_start":        meta_tags.get(0x8003, ""),
            "scan_end":          meta_tags.get(0x8006, ""),
            "timestamp_ms":      meta_tags.get(0x8008, ""),
            "session_id":        meta_tags.get(0x8015, ""),
            "feedback_mode":     meta_tags.get(0x8030, ""),
            "scan_rate_hz":      meta_tags.get(0x8049, float("nan")),
            "scan_pos_x_m":      meta_tags.get(0x8040, float("nan")),
            "scan_pos_y_m":      meta_tags.get(0x8041, float("nan")),
            "scan_size_x_m":     meta_tags.get(0x8042, float("nan")),
            "scan_size_y_m":     meta_tags.get(0x8043, float("nan")),
            "image_pixels_x":    meta_tags.get(0x8046, 0),
            "image_pixels_y":    meta_tags.get(0x8047, 0),
            "scan_direction":    meta_tags.get(0x804B, ""),
            "full_metadata":     full_meta,
        },
        "cantilever": {
            "name":                _meta_get("cantilever-calibration-info.cantilever-name"),
            "spring_constant_Nm":  _meta_get("cantilever-calibration-info.spring-constant"),
            "sensitivity_nmV":     _meta_get("cantilever-calibration-info.sensitivity"),
            "resonance_freq_Hz":   _meta_get("cantilever-calibration-info.frequency"),
            "q_factor":            _meta_get("cantilever-calibration-info.qFactor"),
            "environment":         _meta_get("cantilever-calibration-info.calibration-environment"),
        },
        "channels": [],
    }

    # Remaining IFDs are data channels
    for idx, tags in enumerate(ifds[1:], start=1):
        w   = tags.get(0x0100, 0)
        h   = tags.get(0x0101, 0)
        raw = _read_strips(data, tags)
        cal = _calibrate(raw, tags)
        grid = [cal[r*w:(r+1)*w] for r in range(h)]

        channel = {
            "index":          idx,
            "logical_name":   tags.get(0x8081, ""),
            "display_name":   tags.get(0x8100, tags.get(0x8052, "")),
            "unit":           tags.get(0x8102, tags.get(0x80d2, "")),
            "scaling":        tags.get(0x8103, "NullScaling"),
            "scale_factor":   tags.get(0x8104, 1.0),
            "offset":         tags.get(0x8105, 0.0),
            "width":          w,
            "height":         h,
            "data_raw":       raw,
            "data_calibrated": cal,
            "data_2d":        grid,
        }
        result["channels"].append(channel)

    return result


# ── human-readable text report ────────────────────────────────────────────────

def format_report(parsed):
    lines = []
    a = lines.append

    a("=" * 70)
    a("JPK AFM FILE REPORT")
    a("=" * 70)
    a(f"File : {parsed['file']}")

    inst = parsed["instrument"]
    a("")
    a("── INSTRUMENT ──────────────────────────────────────────────────────")
    a(f"  Software version  : {inst['software_version']}")
    a(f"  Scan start        : {inst['scan_start']}")
    a(f"  Scan end          : {inst['scan_end']}")
    a(f"  Session ID        : {inst['session_id']}")
    a(f"  Feedback mode     : {inst['feedback_mode']}")
    a(f"  Scan direction    : {inst['scan_direction']}")
    a(f"  Image resolution  : {inst['image_pixels_x']} × {inst['image_pixels_y']} pixels")

    sx = inst["scan_size_x_m"]
    sy = inst["scan_size_y_m"]
    if isinstance(sx, float):
        a(f"  Scan size X       : {sx*1e9:.3f} nm")
        a(f"  Scan size Y       : {sy*1e9:.3f} nm")
        px = inst["scan_pos_x_m"]
        py = inst["scan_pos_y_m"]
        if isinstance(px, float) and px == px:
            a(f"  Scanner position  : ({px*1e9:.1f}, {py*1e9:.1f}) nm")

    sr = inst["scan_rate_hz"]
    if isinstance(sr, float):
        a(f"  Scan rate         : {sr:.2f} Hz")

    cant = parsed["cantilever"]
    a("")
    a("── CANTILEVER ──────────────────────────────────────────────────────")
    a(f"  Name              : {cant['name']}")
    a(f"  Spring constant   : {cant['spring_constant_Nm']}")
    a(f"  Sensitivity       : {cant['sensitivity_nmV']}")
    a(f"  Resonance freq    : {cant['resonance_freq_Hz']}")
    a(f"  Q factor          : {cant['q_factor']}")
    a(f"  Environment       : {cant['environment']}")

    chans = parsed["channels"]
    a("")
    a(f"── CHANNELS ({len(chans)} found) ─────────────────────────────────────────────")
    for ch in chans:
        a("")
        a(f"  Channel {ch['index']}: {ch['display_name'] or ch['logical_name']}")
        a(f"    Logical name  : {ch['logical_name']}")
        a(f"    Unit          : '{ch['unit']}'")
        a(f"    Scaling       : {ch['scaling']}")
        a(f"    Scale factor  : {ch['scale_factor']:.6e}")
        a(f"    Offset        : {ch['offset']:.6e}")
        a(f"    Size          : {ch['width']} × {ch['height']} pixels")
        cal = ch["data_calibrated"]
        if cal:
            mn, mx = min(cal), max(cal)
            mean   = sum(cal) / len(cal)
            unit   = ch["unit"] or "raw"
            scale  = 1e9 if unit == "m" else 1.0
            uname  = "nm" if unit == "m" else unit
            a(f"    Min value     : {mn*scale:.4f} {uname}")
            a(f"    Max value     : {mx*scale:.4f} {uname}")
            a(f"    Mean value    : {mean*scale:.4f} {uname}")
            a(f"    Peak-to-peak  : {(mx-mn)*scale:.4f} {uname}")

    a("")
    a("── FULL INSTRUMENT METADATA ─────────────────────────────────────────")
    for line in inst["full_metadata"].splitlines():
        a(f"  {line}")

    a("")
    a("=" * 70)
    return "\n".join(lines)


# ── CLI entry point ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else (
        "/home/rubel/NOMAD-FAIRmat/SPMfolder/ZenodoDataset/"
        "19254504_Annexin_V_HS_AFM/For Zenodo/"
        "imaging-13.08.28.653/save-2022.11.04-13.08.28.684.jpk"
    )
    parsed = parse_jpk(path)
    print(format_report(parsed))
