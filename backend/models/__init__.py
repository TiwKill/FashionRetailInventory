"""
Models package - Pydantic data models.

Contains all Pydantic models for request/response validation:
- Core configs (BrandConfig, SimulationRequest)
- Data models (DailyData, MonthlyData, events)
- Trend models (brand-level and product-level)
- Response models (SimulationResponse, SeasonFestivalResponse)
"""

from models.pydantic import (
    # Configs
    BrandConfig,
    FestivalDemand,
    SimulationRequest,
    # Data models
    DailyData,
    MonthlyData,
    RestockEvent,
    ReorderPointEvent,
    FestivalEvent,
    SeasonEvent,
    BrandSummary,
    # Trend models
    MonthlyTrend,
    TrendEvent,
    MonthlyProductTrend,
    ProductTrendEvent,
    # Responses
    SimulationResponse,
    SeasonInfo,
    FestivalInfo,
    SeasonFestivalResponse
)

__all__ = [
    "BrandConfig",
    "FestivalDemand", 
    "SimulationRequest",
    "DailyData",
    "MonthlyData",
    "RestockEvent",
    "ReorderPointEvent",
    "FestivalEvent",
    "SeasonEvent",
    "BrandSummary",
    "MonthlyTrend",
    "TrendEvent",
    "MonthlyProductTrend",
    "ProductTrendEvent",
    "SimulationResponse",
    "SeasonInfo",
    "FestivalInfo",
    "SeasonFestivalResponse"
]
