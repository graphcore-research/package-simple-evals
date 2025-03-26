# Copyright (c) 2025 Graphcore Ltd. All rights reserved.
"""
simple_evals - A lightweight library for evaluating language models.
"""

__version__ = "0.1.0"

# Import key modules and functions
from simple_evals.simple_evals import main  # noqa: F401
from simple_evals.common import *  # noqa: F403
from simple_evals.types import *  # noqa: F403

# Import all evaluation classes
from simple_evals.simpleqa_eval import SimpleQAEval  # noqa: F401
from simple_evals.mmlu_eval import MMLUEval  # noqa: F401
from simple_evals.mgsm_eval import MGSMEval  # noqa: F401
from simple_evals.math_eval import MathEval  # noqa: F401
from simple_evals.humaneval_eval import HumanEval  # noqa: F401
from simple_evals.gpqa_eval import GPQAEval  # noqa: F401
from simple_evals.drop_eval import DropEval  # noqa: F401

# Import samplers
from simple_evals.sampler import *  # noqa: F403
