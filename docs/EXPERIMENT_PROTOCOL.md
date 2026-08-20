# Experiment Protocol

## Dataset and split

The experiments use CLEVRER. The revision workflow establishes a deterministic internal split of the 10,000 available training videos into 9,000 training videos and 1,000 frozen internal evaluation videos using split seed `20260817`.

The internal 1,000-video partition is not presented as the official CLEVRER held-out test set.

## Input and prediction protocol

- RGB frames are evaluated at 64 × 64 resolution.
- Four consecutive frames form the context window.
- NEX-ViP is trained with a 4-context-to-1-target objective.
- Recursive inference appends each predicted frame and removes the oldest context frame.
- Primary reporting horizons: t+1, t+5, t+10.
- Extended rollout diagnostics: t+20 and t+30.

## Training configuration

Controlled NEX-ViP revision experiments use:

- AdamW
- learning rate: 2e-4
- weight decay: 1e-4
- batch size: 32
- epochs: 20
- seeds: 2024, 2025, 2026
- loss: L1 + 0.5 × (1 - SSIM)

No learning-rate scheduler, Jacobian loss, explicit low-rank loss, modular-polynomial loss, or physics-conservation loss is part of the verified NEX-ViP training objective.

## Visual metrics

The notebook reports:

- MSE
- SSIM
- LPIPS

at t+1, t+5, and t+10, with additional long-rollout diagnostics at t+20 and t+30.

## Ablations

The controlled revision includes:

1. full model
2. encoder-frozen/random control
3. identity transition
4. direct-frame decoder
5. no L1
6. no SSIM

## Baseline protocol

Strong comparison models:

- PredRNN++
- PhyDNet
- SimVPv2-gSTA
- TAU

OpenSTL is pinned to commit:

`eecf8a3078f0a178dbc7b28723da20f94ce36985`

The evaluation set/cache is standardized. Training is not fully harmonized: NEX-ViP uses 4→1 training while the baseline protocol uses 4→10 training. This difference must be retained as a stated limitation.

## Statistical analysis

At t+10, the manuscript uses paired, two-sided Wilcoxon signed-rank tests across the same 1,000 evaluation videos. The pre-specified family contains 12 tests (4 baselines × 3 metrics), followed by Holm correction.

## Motion analysis

Motion quantities are proposal-derived 2-D image-plane measurements. The final Stage 17D-V2 procedure:

1. uses final localized centroids only;
2. computes velocity by finite differences of consecutive centroids;
3. computes acceleration by finite differences of consecutive raw velocities;
4. uses the same definition for observed-RGB tracker calibration;
5. does not use stored tracker search-state `vx`, `vy`, `ax`, or `ay` fields for manuscript kinematics.

## Compute profiling

The standardized compute profile uses:

- Tesla T4
- batch size 1
- 4-context-to-10-prediction rollout
- FP32
- TF32 disabled
- 10 warm-up runs
- 30 timed runs
- `torch.profiler(with_flops=True)` for operator-accounted FLOPs

Profiler FLOPs represent supported operations, not a theoretical count of every low-level operation.
