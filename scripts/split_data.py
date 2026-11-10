"""Create reproducible train/validation/test splits.

Dataset-specific split logic will be added after the chosen category and
dataset layout are confirmed.
"""

import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    print(f"Data directory: {args.data_dir.resolve()}")
    print(f"Seed: {args.seed}")
    print("TODO: implement dataset-specific split generation.")

if __name__ == "__main__":
    main()
