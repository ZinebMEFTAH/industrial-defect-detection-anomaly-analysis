"""Dataset acquisition helper.

Download MVTec AD manually from its official distribution and extract it under
data/mvtec_anomaly_detection/. This placeholder intentionally does not scrape
or redistribute dataset files.
"""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

if __name__ == "__main__":
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Dataset directory: {DATA_DIR}")
    print("Place the dataset here after downloading it from its official source.")
