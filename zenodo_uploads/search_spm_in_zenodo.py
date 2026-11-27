"""
Zenodo SPM Dataset Search
=========================
Searches Zenodo for scanning probe microscopy (SPM) datasets from
Bruker, Nanonis, and Omicron instruments, filtered to STM, STS, and
AFM techniques in the physics / materials science domain.

Output: title, DOI, and selected metadata — no files are downloaded.

Requirements:
    pip install requests

Usage:
    python zenodo_spm_search.py

Authentication (recommended):
    export ZENODO_TOKEN="your_token_here"
    python zenodo_spm_search.py

    Get a token at: https://zenodo.org/account/settings/applications/tokens/new/
    Required scope: none (public records are readable without scopes)

Rate limits (as of Nov 2025):
    - Anonymous  : 25 results/page, 30 requests/minute
    - Authenticated: 100 results/page, 30 requests/minute
"""

import os
import time
import json
import requests

# ── Configuration ──────────────────────────────────────────────────────────────

BASE_URL = "https://zenodo.org/api/records"

TOKEN = os.environ.get("ZENODO_TOKEN", "")

HEADERS = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}

# Authenticated users get 100 results/page; anonymous only 25
PAGE_SIZE = 100 if TOKEN else 25

# Zenodo enforces 30 requests/minute — we wait 2 s between queries to be safe
REQUEST_DELAY = 2.0

# ── Query definitions ──────────────────────────────────────────────────────────
#
# Zenodo uses Elasticsearch query string syntax.
# Searchable metadata fields include: title, description, keywords,
# creators.name, resource_type.type, subjects, notes.
#
# File extension terms (.sxm, .spm, etc.) are searched as free text
# across title/description/keywords — not as structured file-type filters,
# since Zenodo does not index file extensions as a separate metadata field.
#
# Instrument / manufacturer keywords
MANUFACTURER_TERMS = (
    "Bruker OR Nanonis OR Omicron OR Nanoscope OR Scienta"
)

# Known SPM file extensions per manufacturer:
#   Bruker/Nanoscope : .spm, .000, .001  (binary Nanoscope format)
#   Nanonis          : .sxm, .dat
#   Omicron/Scienta  : .par, .tf0, .sf0  (also .VERT, .I(V), .Z(V))
FILE_EXT_TERMS = (
    '".spm" OR ".sxm" OR ".par" OR ".tf0" OR ".sf0" OR "Nanoscope format"'
)

# Technique keywords
TECHNIQUE_TERMS = (
    'STM OR STS OR AFM OR '
    '"scanning tunneling microscopy" OR '
    '"scanning tunneling spectroscopy" OR '
    '"atomic force microscopy" OR '
    '"scanning probe microscopy"'
)

# Domain / subject keywords
DOMAIN_TERMS = (
    '"material science" OR "materials science" OR '
    '"surface science" OR "condensed matter" OR '
    '"thin film" OR "2D material" OR "graphene" OR '
    '"topological insulator" OR "superconductor"'
)

# Four complementary queries — deduplicated after merging
QUERIES = {
    "manufacturers_and_techniques": (
        f"({MANUFACTURER_TERMS}) AND ({TECHNIQUE_TERMS}) "
        "AND resource_type.type:dataset"
    ),
    "file_extensions_and_techniques": (
        f"({FILE_EXT_TERMS}) AND ({TECHNIQUE_TERMS}) "
        "AND resource_type.type:dataset"
    ),
    "domain_and_techniques": (
        f"({DOMAIN_TERMS}) AND ({TECHNIQUE_TERMS}) "
        "AND resource_type.type:dataset"
    ),
    "spm_broad": (
        '"scanning probe microscopy" OR "SPM dataset" OR '
        '"STM data" OR "AFM data" OR "STS data"'
        " AND resource_type.type:dataset"
    ),
}

# ── Helpers ────────────────────────────────────────────────────────────────────

def search_zenodo(query: str) -> list[dict]:
    """Run a single Zenodo search page and return raw hit records."""
    params = {
        "q": query,
        "type": "dataset",
        "size": PAGE_SIZE,
        "sort": "mostrecent",
        "page": 1,
    }
    try:
        r = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=20)
        r.raise_for_status()
        return r.json().get("hits", {}).get("hits", [])
    except requests.HTTPError as exc:
        print(f"  [HTTP ERROR] {exc.response.status_code} — "
              f"{exc.response.text[:120]}")
        return []
    except requests.RequestException as exc:
        print(f"  [ERROR] {exc}")
        return []


def extract_metadata(record: dict) -> dict:
    """Extract title, DOI, URL, and key metadata from a Zenodo record."""
    meta = record.get("metadata", {})

    doi = record.get("doi") or meta.get("doi", "N/A")
    title = meta.get("title", "N/A")
    creators = [c.get("name", "") for c in meta.get("creators", [])]
    pub_date = meta.get("publication_date", "N/A")
    keywords = meta.get("keywords", [])
    resource_type = meta.get("resource_type", {}).get("title", "N/A")
    access = meta.get("access_right", "N/A")
    desc = meta.get("description", "")
    desc_short = (desc[:250] + "…") if len(desc) > 250 else desc
    url = record.get("links", {}).get("html", f"https://doi.org/{doi}")

    return {
        "title": title,
        "doi": doi,
        "url": url,
        "creators": creators,
        "publication_date": pub_date,
        "resource_type": resource_type,
        "access_right": access,
        "keywords": keywords,
        "description_preview": desc_short,
    }


def deduplicate(records: list[dict]) -> list[dict]:
    """Remove duplicate records by DOI."""
    seen: set[str] = set()
    unique = []
    for rec in records:
        key = rec.get("doi") or rec.get("title", "")
        if key and key not in seen:
            seen.add(key)
            unique.append(rec)
    return unique


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    mode = "authenticated" if TOKEN else "anonymous (add ZENODO_TOKEN for 100 results/page)"
    print("=" * 65)
    print("  Zenodo SPM Dataset Search")
    print(f"  Mode        : {mode}")
    print("  Instruments : Bruker · Nanonis · Omicron")
    print("  Techniques  : STM · STS · AFM")
    print("  Domain      : Physics / Materials Science")
    print("=" * 65)

    all_records: list[dict] = []

    for label, query in QUERIES.items():
        print(f"\n[Query: {label}]")
        print(f"  {query[:110]}{'…' if len(query) > 110 else ''}")

        hits = search_zenodo(query)
        print(f"  → {len(hits)} result(s) returned")

        for hit in hits:
            m = extract_metadata(hit)
            m["_query_label"] = label
            all_records.append(m)

        time.sleep(REQUEST_DELAY)   # stay within 30 req/min limit

    unique = deduplicate(all_records)

    print("\n" + "=" * 65)
    print(f"  Total unique datasets found: {len(unique)}")
    print("=" * 65)

    for i, rec in enumerate(unique, 1):
        print(f"\n{'─' * 60}")
        print(f"  [{i}] {rec['title']}")
        print(f"  DOI    : {rec['doi']}")
        print(f"  URL    : {rec['url']}")
        print(f"  Date   : {rec['publication_date']}")
        print(f"  Access : {rec['access_right']}")
        creators_str = ", ".join(rec["creators"][:3])
        if len(rec["creators"]) > 3:
            creators_str += " et al."
        print(f"  By     : {creators_str}")
        if rec["keywords"]:
            print(f"  Tags   : {', '.join(rec['keywords'][:8])}")
        if rec["description_preview"]:
            print(f"  Desc   : {rec['description_preview']}")

    output_file = "zenodo_spm_results.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(unique, f, indent=2, ensure_ascii=False)

    print(f"\n[✓] Full metadata saved to: {output_file}")
    print("    (No files were downloaded — metadata only)\n")


if __name__ == "__main__":
    main()