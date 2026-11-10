# Industrial Defect Detection & Anomaly Analysis

Computer-vision project for industrial quality inspection. The project compares:
- Classical image-processing methods
- Supervised object detection (YOLO)
- Unsupervised anomaly detection (PatchCore / PaDiM)

The central experiment studies how performance changes when labelled defective examples are scarce.

## Project status
🚧 Work in progress.

## Planned pipeline
1. Explore and split the dataset
2. Preprocess and align images
3. Build a classical baseline
4. Train unsupervised anomaly detectors on normal images
5. Train a supervised detector with different defect-label budgets
6. Tune the accept/reject threshold using error costs
7. Evaluate image-level and pixel-level performance

## Repository structure
See the folders in this repository. Dataset images and trained model weights are intentionally excluded from Git.

## Setup
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Dataset
The project is designed to start with MVTec AD. Download data separately and keep it under `data/`. Do not commit datasets or large model weights.

## Reproducibility
- Set random seeds in experiment scripts.
- Record configuration, dataset split, and metrics for every run.
- Save machine-readable results under `results/`.

## Safety and data
Do not commit passwords, API keys, private data, downloaded datasets, or large model weights.
