# Copyright (c) 2025 Graphcore Ltd. All rights reserved.
#!/usr/bin/env python3
"""
Test script to verify that the simple_evals package can be installed
and properly imported after installation.
"""

import os
import sys
import subprocess
import tempfile
import shutil
import pytest

def run_command(cmd, cwd=None):
    """Run a command and return the output."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error: Command failed with exit code {result.returncode}")
        print(f"Stdout: {result.stdout}")
        print(f"Stderr: {result.stderr}")
        return False, result.stderr

    return True, result.stdout

@pytest.fixture
def temp_test_dir(tmp_path):
    """Create a temporary directory for testing."""
    return tmp_path

def test_install_and_import_with_uv(temp_test_dir, monkeypatch):
    """Test installing the package in a UV virtual environment and importing it."""
    # Create a virtual environment using UV
    venv_path = temp_test_dir / "venv"
    success, output = run_command(["uv", "venv", str(venv_path)])
    assert success, "Failed to create virtual environment with UV"

    # Get the path to the python executable in the virtual environment
    if sys.platform == "win32":
        python_path = venv_path / "Scripts" / "python.exe"
    else:
        python_path = venv_path / "bin" / "python"

    # Get the absolute path to the current directory (where the package is)
    pkg_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Install the package with UV
    success, output = run_command(["uv", "pip", "install", pkg_dir], cwd=str(temp_test_dir))
    assert success, f"Failed to install the package with UV: {output}"

    # Create a simple test script to verify imports
    test_script_path = temp_test_dir / "test_import.py"
    with open(test_script_path, "w") as f:
        f.write("""
# Test both import methods
import simple_evals
from simple_evals import sampler

# Test direct imports from the package
print(f"Import main: {'main' in dir(simple_evals)}")
print(f"Import SimpleQAEval: {'SimpleQAEval' in dir(simple_evals)}")
print(f"Import ClaudeSampler: {'ClaudeSampler' in dir(sampler)}")

# Test bridge module
print("All bridge module imports successful!")

print("All imports successful!")
""")

    # Run the test script with the Python from the virtual environment
    success, output = run_command(["uv", "run", str(test_script_path)], cwd=str(temp_test_dir))
    assert success, f"Failed to import the package: {output}"

    print(output)
    assert "All imports successful!" in output

if __name__ == "__main__":
    # When running as a script, use pytest to execute the test
    exit_code = pytest.main(["-xvs", __file__])
    sys.exit(exit_code)