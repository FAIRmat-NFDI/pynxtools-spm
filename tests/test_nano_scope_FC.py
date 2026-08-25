"""Tests for the Bruker NanoScope force-curve (``.spm.txt``) format.

The ``.spm.txt`` file is the NanoScope ASCII export of a force ramp
(force-distance) measurement: a quoted ``"\\Key: value"`` header terminated by
``\\*Force file list end``, followed by tab-delimited extend (``_Ex``) and
retract (``_Rt``) columns. This module covers the value/unit splitting done by
``TxtBruker`` and the force-curve specific groups built by ``BrukerTxtAFM``.
"""

import numpy as np
import pytest

from pynxtools_spm.nxformatters.bruker.bruker_txt_afm import (
    BrukerTxtAFM,
    NXScanControlPointForce,
)
from pynxtools_spm.parsers.bruker_txt import TxtBruker


# ---------------------------------------------------------------------------
# TxtBruker.extract_data_unit — unit storage consistency
# ---------------------------------------------------------------------------


class TestExtractDataUnit:
    """Verify that all three value patterns store units under the /unit suffix."""

    def setup_method(self):
        self.parser = TxtBruker.__new__(TxtBruker)

    @pytest.mark.parametrize(
        "key, val, expected_value, expected_unit_key, unit_value",
        [
            # Pattern 1: V (coeff unit) value unit
            (
                "/Ciao_scan_list/0/@2:CantFrequency",
                "V (0.00001164153 kHz/LSB) 87.0 kHz",
                "87.0",
                "/Ciao_scan_list/0/@2:CantFrequency/unit",
                "kHz",
            ),
            # Pattern 2: S [Tag] Value  — no unit stored
            ("/Ciao_scan_list/0/AFMMode", "S [AFMMode] Contact", None, None, None),
            # Pattern 3: value unit (simple)
            (
                "/Ciao_scan_list/0/Free_Amplitude",
                "500 nm",
                "500",
                "/Ciao_scan_list/0/Free_Amplitude/unit",
                "nm",
            ),
            # Fallback: plain string, no unit
            ("/Ciao_force_list/0/Samps/line", "512", "512", None, None),
        ],
    )
    def test_unit_key_uses_slash_unit_suffix(
        self, key, val, expected_value, expected_unit_key, unit_value
    ):
        result = self.parser.extract_data_unit(key, val)

        # No /@unit or /@units key should ever appear
        for k in result:
            assert not k.endswith("/@unit"), f"Found legacy /@unit key: {k}"
            assert not k.endswith("/@units"), f"Found legacy /@units key: {k}"

        if expected_value is not None:
            assert result.get(key) == expected_value

        if expected_unit_key is not None:
            assert expected_unit_key in result, (
                f"Expected unit key '{expected_unit_key}' not found in {result}"
            )
            assert result[expected_unit_key] == unit_value


# ---------------------------------------------------------------------------
# BrukerTxtAFM — amplitude_setpoint computation
# ---------------------------------------------------------------------------


class TestAmplitudeSetpoint:
    """Verify _construct_cantilever_oscillator computes amplitude_setpoint correctly."""

    def _make_formatter(self, raw_data: dict) -> BrukerTxtAFM:
        fmt = BrukerTxtAFM.__new__(BrukerTxtAFM)
        fmt.raw_data = raw_data
        fmt.template = {}
        return fmt

    def test_computes_product_of_ratio_and_reference(self):
        raw_data = {
            "/Ciao_scan_list/0/Free_Amplitude": 500,
            "/Ciao_scan_list/0/Setpoint/Amplitude_Ratio": 0.9,
        }
        fmt = self._make_formatter(raw_data)

        conf_dict = {
            "reference_amplitude": {
                "raw_path": "/Ciao_scan_list/0/Free_Amplitude",
                "@units": "@default:mV",
            },
            "amplitude_setpoint": {
                "#note": "handled by _construct_cantilever_oscillator",
                "raw_path": "/Ciao_scan_list/0/Setpoint/Amplitude_Ratio",
            },
        }
        fmt._construct_cantilever_oscillator(
            conf_dict, "/entry/instrument/cantilever", "cantilever_oscillator"
        )

        path = "/entry/instrument/cantilever/cantilever_oscillator/amplitude_setpoint"
        assert path in fmt.template
        assert fmt.template[path] == pytest.approx(450.0)
        assert fmt.template[f"{path}/@units"] == "mV"

    def test_skips_when_ratio_missing(self):
        raw_data = {"/Ciao_scan_list/0/Free_Amplitude": 500}
        fmt = self._make_formatter(raw_data)

        conf_dict = {
            "reference_amplitude": {
                "raw_path": "/Ciao_scan_list/0/Free_Amplitude",
                "@units": "@default:mV",
            },
            "amplitude_setpoint": {
                "raw_path": "/Ciao_scan_list/0/Setpoint/Amplitude_Ratio",
            },
        }
        fmt._construct_cantilever_oscillator(
            conf_dict, "/entry/instrument/cantilever", "cantilever_oscillator"
        )

        assert (
            "/entry/instrument/cantilever/cantilever_oscillator/amplitude_setpoint"
            not in fmt.template
        )


# ---------------------------------------------------------------------------
# BrukerTxtAFM — scan region approach/retrace geometry
# ---------------------------------------------------------------------------


class TestScanRegionGeometry:
    """Verify construct_scan_region_grp derives start/end/range from ramp arrays."""

    def _make_formatter(self, raw_data: dict) -> BrukerTxtAFM:
        fmt = BrukerTxtAFM.__new__(BrukerTxtAFM)
        fmt.raw_data = raw_data
        fmt.template = {}
        fmt.scan_control = NXScanControlPointForce()
        return fmt

    def test_approach_retrace_start_end_range(self):
        approach = np.linspace(0.0, 100.0, 512)
        retrace = np.linspace(100.0, 0.0, 512)
        raw_data = {
            "/Calc_Ramp_Ex_nm": approach,
            "/Calc_Ramp_Ex_nm/unit": "nm",
            "/Calc_Ramp_Rt_nm": retrace,
            "/Calc_Ramp_Rt_nm/unit": "nm",
        }
        fmt = self._make_formatter(raw_data)
        fmt.construct_scan_region_grp(
            partial_conf_dict={}, parent_path="/entry", group_name="scan_region"
        )

        sc = fmt.scan_control
        assert sc.approach_start == pytest.approx(0.0)
        assert sc.approach_end == pytest.approx(100.0)
        assert sc.approach_range == pytest.approx(100.0)
        assert sc.approach_start_unit == "nm"

        assert sc.retrace_start == pytest.approx(100.0)
        assert sc.retrace_end == pytest.approx(0.0)
        assert sc.retrace_range == pytest.approx(100.0)
        assert sc.retrace_start_unit == "nm"

    def test_template_fields_written(self):
        approach = np.array([10.0, 50.0, 90.0])
        retrace = np.array([90.0, 50.0, 10.0])
        raw_data = {
            "/Calc_Ramp_Ex_nm": approach,
            "/Calc_Ramp_Ex_nm/unit": "nm",
            "/Calc_Ramp_Rt_nm": retrace,
            "/Calc_Ramp_Rt_nm/unit": "nm",
        }
        fmt = self._make_formatter(raw_data)
        fmt.construct_scan_region_grp(
            partial_conf_dict={}, parent_path="/entry", group_name="scan_region"
        )

        base = "/entry/scan_region"
        assert fmt.template[
            f"{base}/scan_startN[scan_start_approach]"
        ] == pytest.approx(10.0)
        assert fmt.template[f"{base}/scan_endN[scan_end_approach]"] == pytest.approx(
            90.0
        )
        assert fmt.template[f"{base}/scan_startN[scan_start_retrace]"] == pytest.approx(
            90.0
        )
        assert fmt.template[f"{base}/scan_endN[scan_end_retrace]"] == pytest.approx(
            10.0
        )


# ---------------------------------------------------------------------------
# BrukerTxtAFM — point-force scan step size computation
# ---------------------------------------------------------------------------


class TestPointForceScanStepSize:
    """Verify construct_point_force_scan_grp computes step sizes correctly."""

    def _make_formatter(self, raw_data: dict, sc_kwargs: dict) -> BrukerTxtAFM:
        fmt = BrukerTxtAFM.__new__(BrukerTxtAFM)
        fmt.raw_data = raw_data
        fmt.template = {}
        fmt.scan_control = NXScanControlPointForce(**sc_kwargs)
        return fmt

    def test_step_size_from_shared_samps_line(self):
        raw_data = {"/Ciao_force_list/0/Samps/line": "512 512"}
        fmt = self._make_formatter(
            raw_data,
            sc_kwargs={
                "approach_range": 100.0,
                "approach_range_unit": "nm",
                "retrace_range": 100.0,
                "retrace_range_unit": "nm",
            },
        )

        conf_dict = {
            "scan_pointsN[scan_points_n]": [
                {"approach": {"raw_path": "/Ciao_force_list/0/Samps/line"}},
                {"retrace": {"raw_path": "/Ciao_force_list/0/Samps/line"}},
            ]
        }
        fmt.construct_point_force_scan_grp(
            conf_dict, "/entry/scan_ctrl", "point_forceSCAN[point_force_scan]"
        )

        assert fmt.scan_control.approach_points == 512
        assert fmt.scan_control.retrace_points == 512
        expected_step = 100.0 / (512 - 1)
        base = "/entry/scan_ctrl/point_forceSCAN[point_force_scan]"
        assert fmt.template[f"{base}/step_sizeN[step_size_approach]"] == pytest.approx(
            expected_step
        )
        assert fmt.template[f"{base}/step_sizeN[step_size_retrace]"] == pytest.approx(
            expected_step
        )
        assert fmt.template[f"{base}/step_sizeN[step_size_approach]/@units"] == "nm"
