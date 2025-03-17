"""
simple_evals - A lightweight library for evaluating language models.
"""

__version__ = "0.1.0"

# Import key modules and functions
from simple_evals.simple_evals import main
from simple_evals.common import *
from simple_evals.types import *

# Import all evaluation classes
from simple_evals.simpleqa_eval import SimpleQAEval
from simple_evals.mmlu_eval import MMLUEval
from simple_evals.mgsm_eval import MGSMEval
from simple_evals.math_eval import MathEval
from simple_evals.humaneval_eval import HumanEval
from simple_evals.gpqa_eval import GPQAEval
from simple_evals.drop_eval import DropEval

# Import samplers
from simple_evals.sampler import * 