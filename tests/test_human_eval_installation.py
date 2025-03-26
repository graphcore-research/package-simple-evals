# Copyright (c) 2025 Graphcore Ltd. All rights reserved.
import os
import pytest
import importlib.util
from pathlib import Path


def test_human_eval_package_installed():
    """Test that human_eval package is properly installed."""
    # Check if human_eval module can be imported
    assert importlib.util.find_spec("human_eval") is not None, "human_eval package is not installed"


def test_human_eval_data_files_accessible():
    """Test that the data files required by human_eval are accessible."""
    # Import the module that uses the data files
    from human_eval.data import read_problems, HUMAN_EVAL

    # Check if the data file exists
    assert os.path.exists(HUMAN_EVAL), f"Data file does not exist at {HUMAN_EVAL}"

    # Try to read the problems from the data file
    problems = read_problems()

    # Verify that problems are loaded correctly
    assert len(problems) > 0, "No problems were loaded from the data file"

    # Check a few expected task IDs are present
    sample_tasks = ["HumanEval/0", "HumanEval/1", "HumanEval/2"]
    for task in sample_tasks:
        assert task in problems, f"Expected task {task} not found in problems"

    # Check that problem fields are as expected
    example_problem = problems["HumanEval/0"]
    required_fields = ["task_id", "prompt", "entry_point", "test"]
    for field in required_fields:
        assert field in example_problem, f"Required field '{field}' missing from problem"


if __name__ == "__main__":
    # This allows running the tests directly from this file
    pytest.main(["-xvs", __file__])