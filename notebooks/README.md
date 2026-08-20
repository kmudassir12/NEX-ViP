# Notebooks

This directory is reserved for the exact Colab notebooks associated with the NEX-ViP revision workflow.

For journal submission, place the following two files here:

1. `NEX_ViP_executed.ipynb` — the original executed Colab notebook, including retained outputs that document the reported workflow.
2. `NEX_ViP_clean.ipynb` — the same notebook code with cell outputs removed for clean reruns.

Expected SHA-256 checksums from the prepared submission package:

```text
NEX_ViP_executed.ipynb  034b1bbeac19431d362532ea5a2a82e349a9780ae1f071cb2ca0aa8eef84adeb
NEX_ViP_clean.ipynb     a16cbb9d4a1dde1f3e6e3ce5e7e950b52c6a6352770d3e3ef41a52d4d917de69
```

After upload, run:

```bash
python scripts/validate_notebook.py notebooks/NEX_ViP_clean.ipynb
sha256sum notebooks/NEX_ViP_executed.ipynb notebooks/NEX_ViP_clean.ipynb
```

The notebook must retain the final Stage 17D-V2 raw-centroid derivative correction used for the manuscript's image-plane velocity analysis.
