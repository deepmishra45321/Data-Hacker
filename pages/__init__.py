"""Pages package."""
from .home import render_home_page
from .preprocessing_page import render_preprocessing_page
from .eda_page import render_eda_page
from .ml_training_page import render_ml_training_page
from .dl_training_page import render_dl_training_page
from .prediction_page import render_prediction_page
from .report_page import render_report_page
from .about_page import render_about_page

__all__ = [
    'render_home_page',
    'render_preprocessing_page',
    'render_eda_page',
    'render_ml_training_page',
    'render_dl_training_page',
    'render_prediction_page',
    'render_report_page',
    'render_about_page'
]
