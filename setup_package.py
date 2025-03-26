# Copyright (c) 2025 Graphcore Ltd. All rights reserved.
#!/usr/bin/env python3
"""
Script to set up the simple_evals package by copying files from the simple-evals submodule.
This should be run during the build process to properly structure the package.
"""

import os
import shutil
import sys
import glob


def setup_package():
    """Copy files from simple-evals submodule to the package directory."""
    source_dir = "simple-evals"
    target_dir = "simple_evals"

    if not os.path.exists(source_dir):
        print(
            f"Error: Source directory '{source_dir}' not found. Make sure the submodule is initialized.",
            file=sys.stderr,
        )
        return False

    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # Copy .py files from the root of simple-evals to simple_evals/
    for filename in os.listdir(source_dir):
        if filename.endswith(".py"):
            src_path = os.path.join(source_dir, filename)
            dst_path = os.path.join(target_dir, filename)
            shutil.copy2(src_path, dst_path)
            print(f"Copied {src_path} to {dst_path}")

    # Create and copy sampler directory
    sampler_src_dir = os.path.join(source_dir, "sampler")
    sampler_dst_dir = os.path.join(target_dir, "sampler")

    os.makedirs(sampler_dst_dir, exist_ok=True)

    # Copy sampler files
    for filename in os.listdir(sampler_src_dir):
        if filename.endswith(".py"):
            src_path = os.path.join(sampler_src_dir, filename)
            dst_path = os.path.join(sampler_dst_dir, filename)
            shutil.copy2(src_path, dst_path)
            print(f"Copied {src_path} to {dst_path}")

    # Copy data files
    data_extensions = [".json", ".jsonl", ".csv", ".txt"]
    for ext in data_extensions:
        for src_path in glob.glob(
            os.path.join(source_dir, f"**/*{ext}"), recursive=True
        ):
            # Calculate relative path from source_dir
            rel_path = os.path.relpath(src_path, source_dir)
            dst_path = os.path.join(target_dir, rel_path)

            # Create destination directory if needed
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)

            # Copy the file
            shutil.copy2(src_path, dst_path)
            print(f"Copied data file {src_path} to {dst_path}")

    print("Package setup completed successfully.")
    return True


if __name__ == "__main__":
    if not setup_package():
        sys.exit(1)
