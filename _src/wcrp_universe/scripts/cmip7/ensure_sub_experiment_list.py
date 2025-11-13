#!/usr/bin/env python3
"""
Wrapper sub_experiment_id into a list where needed.

Usage:
    python ensure_sub_experiment_list.py -d CMIP7_experiment [-r] [-b] [--dry-run]

- If sub_experiment_id is present and not a list, it becomes a list containing the original value.
- If original value is None/null, it becomes ["none"].
- If already a list, file is left unchanged.
"""

import json
from pathlib import Path
import shutil
import argparse

def process_file(path: Path, backup: bool = False, dry_run: bool = False) -> bool:
    """
    Returns True if file was modified (i.e. value wrapped into a list), False otherwise.
    """
    try:
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except Exception as e:
        print(f"ERROR: cannot read {path}: {e}")
        return False

    if "sub_experiment_id" not in data:
        # nothing to do
        return False

    val = data["sub_experiment_id"]

    # if already a list, nothing to do
    if isinstance(val, list):
        return False

    # convert None -> "none", else keep value as-is
    if val is None:
        new_val = ["none"]
    else:
        # ensure we convert booleans/ints/etc to their JSON representation
        # for strings "none" we keep "none"
        new_val = [val]

    # assign back (assignment to existing key preserves insertion order in py3.7+)
    data["sub_experiment_id"] = new_val

    if dry_run:
        print(f"DRY-RUN: would update {path} : sub_experiment_id -> {new_val}")
        return True

    # optional backup
    if backup:
        bak = path.with_suffix(path.suffix + ".bak")
        try:
            shutil.copy(path, bak)
        except Exception as e:
            print(f"WARNING: backup failed for {path}: {e}")

    # atomic write: write to .tmp then replace
    tmp = path.with_suffix(path.suffix + ".tmp")
    try:
        with tmp.open("w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=4, ensure_ascii=False)
        tmp.replace(path)
        print(f"UPDATED: {path.name} -> sub_experiment_id wrapped into list")
        return True
    except Exception as e:
        print(f"ERROR: cannot write {path}: {e}")
        if tmp.exists():
            tmp.unlink(missing_ok=True)
        return False


def main(target_dir: str, recursive: bool = False, backup: bool = False, dry_run: bool = False):
    p = Path(target_dir)
    if not p.exists() or not p.is_dir():
        print(f"Target directory does not exist or is not a dir: {target_dir}")
        return

    pattern = "**/*.json" if recursive else "*.json"
    files = list(p.glob(pattern))

    if not files:
        print("No JSON files found.")
        return

    modified = 0
    skipped = 0
    errors = 0
    for f in files:
        try:
            changed = process_file(f, backup=backup, dry_run=dry_run)
            if changed:
                modified += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"ERROR processing {f}: {e}")
            errors += 1

    print(f"\nSummary: modified: {modified}, skipped (no change): {skipped}, errors: {errors}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wrap sub_experiment_id into a list if needed.")
    parser.add_argument("-d", "--dir", default=".", help="Target directory containing JSON files")
    parser.add_argument("-r", "--recursive", action="store_true", help="Process subdirectories recursively")
    parser.add_argument("-b", "--backup", action="store_true", help="Create .bak backup before modifying each file")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files, just show what would change")
    args = parser.parse_args()

    main(args.dir, recursive=args.recursive, backup=args.backup, dry_run=args.dry_run)
