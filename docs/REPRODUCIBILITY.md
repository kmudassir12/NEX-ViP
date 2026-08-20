# Reproducibility Guide

## Recommended environment

The provided notebook was executed in Google Colab with a Tesla T4 GPU. Package versions observed directly in notebook output include PyTorch `2.11.0+cu128`, Lightning `2.2.1`, and TorchMetrics `1.9.0`.

Because Colab images change over time, exact archival reproduction should record the runtime package manifest at execution time. `requirements.txt` captures the direct third-party dependencies used by the notebook; CUDA-enabled PyTorch installation may need to be adapted to the available runtime.

## Run order

Run the notebook sequentially. Later stages intentionally depend on artifacts created and persisted by earlier stages.

The revision is staged so that large or expensive work can be resumed from Drive artifacts rather than re-executed from the beginning.

## Persistent artifact root

The notebook expects the following primary revision root:

```text
/content/drive/MyDrive/CLEVRER/NEXVIP_SCIENTIFIC_REVISION/
```

The source dataset is expected beneath:

```text
/content/drive/MyDrive/CLEVRER/
```

## External dependency

The strong-baseline phase vendors OpenSTL and pins it to commit:

```text
eecf8a3078f0a178dbc7b28723da20f94ce36985
```

Do not silently update OpenSTL when reproducing the manuscript results.

## Reproducibility checks

Before treating a run as manuscript-equivalent, confirm:

- split seed and split manifest match the recorded revision artifacts;
- seeds 2024, 2025, and 2026 are all present where multi-seed results are claimed;
- the same 1,000-video evaluation cache is used for paired baseline testing;
- Stage 17D-V2 is used for reported velocity/acceleration derivatives;
- no NaN remains in the final three-seed physical summary;
- t+10 significance uses exactly 12 paired tests before Holm correction;
- compute profiling is performed under the stated T4/FP32 protocol.

## Checkpoints and large artifacts

Model checkpoints, CLEVRER videos, derender proposals, baseline caches, and per-video result files can exceed normal GitHub limits and are intentionally not bundled into this lightweight source repository package. Archive them separately on an appropriate research-data service if journal policy or licensing allows.

## What not to infer from this implementation

The executable code does not support claims of:

- cryptographic/zero-knowledge verification;
- polynomial or modular identity proofs;
- analytically enforced Newtonian updates;
- explicit low-rank transition constraints;
- world-coordinate momentum or kinetic-energy conservation.

Jacobian/SVD analyses are post-hoc empirical diagnostics only.
