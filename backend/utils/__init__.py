"""
Utils package - Shared utility functions and constants.

This package provides common utilities used across the application:
- constants: Season mappings and festival data
- helpers: Data processing and trend calculation functions
"""

from utils.constants import SEASON_MAPPING, FESTIVALS
from utils.helpers import (
    get_season_info,
    get_festival_info,
    calculate_trend,
    clean_data_for_json
)

__all__ = [
    "SEASON_MAPPING",
    "FESTIVALS",
    "get_season_info",
    "get_festival_info",
    "calculate_trend",
    "clean_data_for_json"
]
