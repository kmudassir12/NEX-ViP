# Results Directory

This directory is intentionally lightweight.

The executed Colab notebook contains the console outputs from the reported workflow. Large CSVs, figures, checkpoints, per-video metrics, and cached tensors are persisted by the notebook to Google Drive and are not bundled here by default.

For journal submission, recommended lightweight additions are:

- final manuscript tables as CSV;
- final figures as PNG/PDF;
- final statistical summary;
- final compute profile table;
- split manifest and its SHA-256 checksum.

Do not commit datasets or large checkpoints directly to GitHub.
