# Simple-Evals Tests

This directory contains tests for the simple-evals package.

## Testing the Human Eval Installation

The `test_human_eval_installation.py` file contains tests to verify that the `human_eval` package is correctly installed with its data files. These tests check:

1. That the `human_eval` package can be imported
2. That the data files required by `human_eval` are accessible and correctly structured
3. That basic functionality of the `human_eval` package works

## Running the Tests

To run all tests:
```bash
python -m pytest
```

To run just the human eval tests:
```bash
python -m pytest tests/test_human_eval_installation.py
```

To run tests with coverage:
```bash
python -m pytest --cov=simple_evals --cov=human_eval
```

## Adding Tests

When adding new packages or functionality, please add corresponding tests to verify:
1. The package can be imported
2. Required data files are included
3. Basic functionality works correctly 