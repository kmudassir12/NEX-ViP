# Data and Artifacts

## CLEVRER

The source videos are not redistributed in this repository. Obtain CLEVRER from its official distribution and comply with the dataset's terms.

The notebook was written against a Google Drive layout rooted at:

```text
/content/drive/MyDrive/CLEVRER/
```

The revision artifact root is:

```text
/content/drive/MyDrive/CLEVRER/NEXVIP_SCIENTIFIC_REVISION/
```

## Expected large inputs

Depending on the stage, the notebook expects:

- CLEVRER video data;
- the trained NEX-ViP checkpoint used by the revision audit;
- `derender_proposals.zip` for proposal-derived object motion/contact analysis;
- intermediate evaluation caches and baseline checkpoints created by earlier stages.

## Outputs

The notebook persists stage-specific outputs including:

- dataset and implementation audits;
- visual metrics;
- static-region diagnostics;
- long-rollout summaries;
- Jacobian/SVD artifacts;
- train/evaluation split manifests;
- ablation checkpoints and metrics;
- OpenSTL baseline results;
- paired significance tables;
- compute profiles;
- proposal-derived motion/contact tables;
- final manuscript figures and evidence manifests.

## GitHub policy

Do not commit raw CLEVRER videos, large model checkpoints, or other artifacts that exceed GitHub file-size limits. Keep this repository focused on source code, configuration, manifests, and lightweight reproducibility documentation.

## Archival recommendation

For submission, use Zenodo (or another journal-approved repository) for the tagged source release and, if licensing permits, a separate data record for large derived artifacts. Link both records from the manuscript Data Availability / Code Availability sections.
