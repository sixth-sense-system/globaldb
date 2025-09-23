import sys, yaml, pyarrow.parquet as pq
from pathlib import Path
import pandas as pd

root = Path("13_OpsLog")
schemas_dir = root / "schemas"
data_dir = root / "data"


def load_yaml(p):
    with open(p, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_table(schema):
    table = schema["table"]
    parquet_path = data_dir / f"{table}.parquet"
    if not parquet_path.exists():
        print(f"[WARN] Missing {parquet_path} (OK on very first run).")
        return
    df = pq.read_table(parquet_path).to_pandas()
    # required columns
    for col in schema["columns"]:
        if col.get("required") and col["name"] not in df.columns:
            sys.exit(f"[ERROR] {table}: missing required column {col['name']}")
    # enums
    for col in schema["columns"]:
        if col.get("type") == "enum" and col["name"] in df.columns and "values" in col:
            bad = set(df[col["name"]].dropna().unique()) - set(col["values"])
            if bad:
                sys.exit(
                    f"[ERROR] {table}: invalid enum values for {col['name']}: {bad}"
                )
    print(f"[OK] {table}: {len(df)} rows; schema valid.")


def main():
    for yml in sorted(schemas_dir.glob("*.yaml")):
        schema = load_yaml(yml)
        validate_table(schema)


if __name__ == "__main__":
    main()
