# NEX-ViP

**NEX-ViP for Efficient Latent Video Prediction with Perceptual Fidelity and Motion Analysis**

This repository contains the Colab implementation and reproducibility materials for the revised NEX-ViP study. The code corresponds to the executable system used for the reported experiments: a convolutional context encoder, a 512-dimensional latent transition MLP, and a residual decoder evaluated with autoregressive rollouts.

> **Scope note.** The executable implementation does **not** contain modular-polynomial arithmetic, cryptographic verification, an explicit low-rank transition constraint, or an analytically imposed Newtonian update. Jacobian/SVD analysis is post-hoc. Motion diagnostics are proposal-derived **2-D image-plane** analyses.

## Repository contents

```text
NEX-ViP/
├── README.md
├── notebooks/
│   ├── NEX_ViP_executed.ipynb   # original executed Colab notebook with outputs
│   └── NEX_ViP_clean.ipynb      # identical code cells with outputs removed
├── docs/
│   ├── EXPERIMENT_PROTOCOL.md
│   ├── REPRODUCIBILITY.md
│   └── DATA_AND_ARTIFACTS.md
├── scripts/
│   └── validate_notebook.py
├── results/
│   └── README.md
├── requirements.txt
├── environment.yml
├── CITATION.cff
├── .zenodo.json
├── .gitignore
└── MANIFEST.sha256
```

## Reproducibility at a glance

- **Primary platform:** Google Colab
- **GPU used in the reported runs:** NVIDIA Tesla T4
- **Python:** 3.12 runtime in the executed notebook
- **PyTorch observed in the executed notebook:** 2.11.0+cu128
- **Lightning:** 2.2.1
- **TorchMetrics:** 1.9.0
- **Dataset:** CLEVRER
- **Input resolution:** 64 × 64 RGB
- **Context:** 4 frames
- **Primary evaluation horizons:** t+1, t+5, t+10
- **Extended rollout diagnostics:** t+20, t+30
- **Controlled seeds:** 2024, 2025, 2026
- **OpenSTL baseline source:** pinned to commit `eecf8a3078f0a178dbc7b28723da20f94ce36985`

## Quick start

1. Open `notebooks/NEX_ViP_clean.ipynb` in Google Colab.
2. Enable a GPU runtime.
3. Place the CLEVRER dataset and required proposal archive in Google Drive as described in `docs/DATA_AND_ARTIFACTS.md`.
4. Run cells sequentially from Stage 0 onward.
5. The notebook writes revision artifacts beneath:

   ```text
   /content/drive/MyDrive/CLEVRER/NEXVIP_SCIENTIFIC_REVISION/
   ```

6. Use the final synthesis stages to regenerate manuscript tables, figures, statistical summaries, compute profiles, and corrected image-plane motion outputs.

For the exact outputs from the authors' execution, see `notebooks/NEX_ViP_executed.ipynb`.

## Main experimental modules

The notebook is organized as an interruption-safe staged workflow:

- **Phase I:** implementation audit, dataset audit, checkpoint-compatible architecture recovery, training-protocol recovery
- **Phase II:** multi-horizon visual metrics, physical-metric applicability audit, static-region degradation, extended rollout, Jacobian/SVD analysis
- **Phase III:** frozen 9,000/1,000 internal split, multi-seed ablations
- **Phase IV:** standardized strong-baseline evaluation, paired statistics, compute profiling, proposal-derived motion/contact diagnostics, final evidence synthesis
- **Final correction:** Stage 17D-V2 recomputes velocity strictly from consecutive final centroids and acceleration strictly from consecutive raw velocity vectors

## Model definition used in the experiments

The implemented NEX-ViP forward path is:

```text
4 RGB context frames
    ↓ channel concatenation
Convolutional encoder
    ↓
512-D latent state
    ↓
Linear(512,512) → ReLU → Linear(512,512)
    ↓
Residual decoder
    ↓
Δx(t+1)
    ↓
clip(x_t + Δx(t+1), 0, 1)
    ↓
autoregressive context update
```

The model contains approximately **18.646 M trainable parameters**.

## Reported comparison models

- PredRNN++
- PhyDNet
- SimVPv2-gSTA
- TAU

Baseline implementations are run through the pinned OpenSTL revision noted above. The manuscript explicitly distinguishes standardized **evaluation** from perfectly harmonized **training**, because NEX-ViP uses 4→1 training while the OpenSTL baseline protocol uses 4→10 training.

## Reproduction and evidence boundaries

Please read `docs/REPRODUCIBILITY.md` before attempting a full rerun. In particular:

- The internal CLEVRER evaluation split is not the official held-out CLEVRER test set.
- Image-plane trajectory/contact analyses do not establish world-coordinate Newtonian consistency.
- Momentum and kinetic-energy conservation are not reported because mass and world-coordinate velocity are unavailable.
- Acceleration estimates are retained for audit but are not treated as primary physical evidence when below tracker calibration resolution.

## Notebook integrity

Executed notebook SHA-256:

```text
034b1bbeac19431d362532ea5a2a82e349a9780ae1f071cb2ca0aa8eef84adeb
```

Clean notebook SHA-256:

```text
a16cbb9d4a1dde1f3e6e3ce5e7e950b52c6a6352770d3e3ef41a52d4d917de69
```

## Citation

Please cite the associated manuscript. A machine-readable citation template is provided in `CITATION.cff`. Replace placeholder author metadata and publication metadata with the final accepted bibliographic record before archival release.

## Archival release

For journal submission, create a versioned GitHub release and archive that release on Zenodo. Insert the resulting Zenodo DOI into the manuscript's **Code Availability** statement.

## License

No software license is asserted in this repository package. The repository owner should select and add an appropriate license before public archival release.
