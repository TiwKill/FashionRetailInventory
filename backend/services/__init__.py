"""
Services package - Business logic layer.

Contains core business logic:
- data_service: Historical data loading and brand parameter calculation
- simulation_service: SimPy simulation execution and result processing
"""

from services.data_service import (
    init_data,
    get_historical_data,
    get_brand_parameters,
    get_supported_brands
)
from services.simulation_service import run_inventory_simulation

__all__ = [
    "init_data",
    "get_historical_data",
    "get_brand_parameters",
    "get_supported_brands",
    "run_inventory_simulation"
]
