#!/usr/bin/env python3
"""Lightweight structural validator for the NEX-ViP Colab notebook."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

REQUIRED_STAGE_MARKERS = [
    "PHASE I — STAGE 0",
    "PHASE II — STAGE 5",
    "PHASE III — STAGE 10A",
    "PHASE IV — STAGE 13A",
    "STAGE 17D-V2",
]

PROHIBITED_SECRET_MARKERS = [
    "api_key=",
    "password=",
    "github_token=",
    "hf_token=",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("notebook", nargs="?", default="notebooks/NEX_ViP_clean.ipynb")
    args = parser.parse_args()

    path = Path(args.notebook)
    nb = json.loads(path.read_text(encoding="utf-8"))
    cells = nb.get("cells", [])
    source = "\n".join("".join(c.get("source", [])) for c in cells)

    assert nb.get("nbformat") == 4, "Expected nbformat 4"
    assert len(cells) >= 50, "Notebook appears incomplete"

    for marker in REQUIRED_STAGE_MARKERS:
        assert marker in source, f"Missing stage marker: {marker}"

    lower_source = source.lower()
    for marker in PROHIBITED_SECRET_MARKERS:
        assert marker not in lower_source, f"Potential embedded secret marker: {marker}"

    sha = hashlib.sha256(path.read_bytes()).hexdigest()
    print(f"PASS: {path}")
    print(f"cells: {len(cells)}")
    print(f"sha256: {sha}")


if __name__ == "__main__":
    main()
