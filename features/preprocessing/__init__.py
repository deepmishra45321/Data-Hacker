"""Preprocessing feature package."""
from .cleaner import (
    remove_duplicates,
    handle_missing_values,
    drop_columns,
    get_column_types
)
from .encoder import encode_categorical
from .scaler import scale_features
from .splitter import split_dataset

__all__ = [
    'remove_duplicates',
    'handle_missing_values',
    'drop_columns',
    'get_column_types',
    'encode_categorical',
    'scale_features',
    'split_dataset'
]
