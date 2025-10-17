import argparse
import pandas as pd
from sklearn.datasets import load_iris
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_dir", type=str, default="data")
    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    iris = pd.read_csv("zameen_updated.csv")
    df = pd.concat([iris.data, iris.target.rename("target")], axis=1)
    df.to_csv(os.path.join(args.out_dir, "zameen_updated.csv"), index=False)
    print("Saved zameen_updated.csv in", args.out_dir)
