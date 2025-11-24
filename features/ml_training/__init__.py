"""ML training feature package."""
from .trainer import train_model, compare_all_models
from .evaluator import evaluate_model

__all__ = [
    'train_model',
    'compare_all_models',
    'evaluate_model'
]
