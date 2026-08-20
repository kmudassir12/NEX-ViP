# Journal Submission Repository Checklist

Use this checklist before citing the repository in the revised manuscript.

## Required before archival release

- [ ] Upload `notebooks/NEX_ViP_executed.ipynb`.
- [ ] Upload `notebooks/NEX_ViP_clean.ipynb`.
- [ ] Verify the notebook SHA-256 values documented in `notebooks/README.md`.
- [ ] Run `python scripts/validate_notebook.py notebooks/NEX_ViP_clean.ipynb`.
- [ ] Replace placeholder author metadata in `CITATION.cff` and `.zenodo.json` with the final author list.
- [ ] Select and add the intended software license.
- [ ] Confirm that no dataset videos, private credentials, tokens, or restricted checkpoints are committed.
- [ ] Create a tagged release, recommended tag: `v1.0.0-submission`.
- [ ] Archive that release in Zenodo and obtain the DOI.
- [ ] Insert the Zenodo DOI into the manuscript Code Availability statement.

## Scientific consistency checks

- [ ] The repository states that the CLEVRER 1,000-video partition is an internal evaluation split, not the official test set.
- [ ] The baseline comparison is described as standardized evaluation rather than fully harmonized training.
- [ ] Stage 17D-V2 raw-centroid derivatives are used for manuscript velocity values.
- [ ] Exactly 12 paired t+10 tests are used before Holm correction.
- [ ] Jacobian/SVD analysis is described as post-hoc empirical analysis.
- [ ] No modular-polynomial, cryptographic, explicit low-rank, Newtonian-guarantee, momentum-conservation, or energy-conservation claims are made beyond the executable evidence.

## Recommended archival record

The Zenodo record should archive the exact tagged source release and include:

- manuscript title;
- complete authorship;
- GitHub repository URL;
- software version/tag;
- keywords;
- linked article metadata when available.
