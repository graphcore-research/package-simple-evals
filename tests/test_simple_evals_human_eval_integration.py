import pytest


def test_simple_evals_can_import_human_eval():
    """Test that simple_evals can import human_eval."""
    # Import the integration module from simple_evals that uses human_eval
    from simple_evals import humaneval_eval


def test_human_eval_class_initialization():
    """Test that the HumanEval class from simple_evals can be initialized."""
    
    from simple_evals.humaneval_eval import HumanEval
    
    # Initialize with default parameters
    human_eval_instance = HumanEval(num_examples=None)
    
    # Check that examples were loaded
    assert hasattr(human_eval_instance, 'examples'), "examples attribute missing"
    assert len(human_eval_instance.examples) > 0, "No examples loaded"
    
    # Test with custom number of examples
    custom_human_eval = HumanEval(num_examples=10)
    assert len(custom_human_eval.examples) == 10, f"Expected 10 examples, got {len(custom_human_eval.examples)}"


def test_human_eval_data_path_resolution():
    """Test that the data path is correctly resolved.
    
    This checks that the data that is in human-eval/data/HumanEval.jsonl.gz is accessible.
    from an installed package.
    """
    import importlib.util
    
    # Import the data module to check path resolution
    spec = importlib.util.find_spec("human_eval.data")
    data_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(data_module)
    
    # Check that HUMAN_EVAL is set correctly
    assert hasattr(data_module, 'HUMAN_EVAL'), "HUMAN_EVAL not defined"
    
    # Check that the file exists
    import os
    assert os.path.exists(data_module.HUMAN_EVAL), f"Data file not found at {data_module.HUMAN_EVAL}"


if __name__ == "__main__":
    # This allows running the tests directly from this file
    pytest.main(["-xvs", __file__]) 