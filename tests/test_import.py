# Copyright (c) 2025 Graphcore Ltd. All rights reserved.
"""
Test script for importing simple_evals
"""
import pytest


def test_import_simple_evals():
    """Test that simple_evals can be imported successfully with version."""
    try:
        import simple_evals
        assert hasattr(simple_evals, '__version__'), "simple_evals should have a __version__ attribute"
    except Exception as e:
        pytest.fail(f"Failed to import simple_evals: {e}")


def test_main_function_availability():
    """Test that the main function is available in simple_evals."""
    import simple_evals
    assert hasattr(simple_evals, 'main'), "simple_evals should have a 'main' function"


def test_evaluation_classes_exist():
    """Test that evaluation classes exist in simple_evals."""
    expected_classes = ["SimpleQAEval", "MMLUEval", "MGSMEval", "MathEval", "HumanEval", "GPQAEval", "DropEval"]
    import simple_evals
    eval_classes = [attr for attr in dir(simple_evals) if 'Eval' in attr and not attr.startswith('_')]
    assert eval_classes, "simple_evals should have at least one evaluation class with 'Eval' in the name"
    assert set(expected_classes).issubset(eval_classes), f"Some expected classes are missing: {set(expected_classes) - set(eval_classes)}"
