from datetime import datetime
from typing import Any, Dict, Tuple, Optional
import pandas as pd
import numpy as np

from utils.constants import SEASON_MAPPING, FESTIVALS


def get_season_info(date: datetime) -> Dict[str, str]:
    """
    Get season information for a given date.
    
    Args:
        date: The date to get season info for
        
    Returns:
        Dict containing 'season', 'quarter', and 'season_type'
    """
    month = date.month
    season_data = SEASON_MAPPING.get(month, {})
    return {
        "season": season_data.get("name", "Unknown"),
        "quarter": season_data.get("quarter", "Unknown"),
        "season_type": season_data.get("type", "Medium Season")
    }


def get_festival_info(date: datetime) -> Tuple[str, float]:
    """
    Check if a date falls on a festival and return festival details.
    
    Args:
        date: The date to check
        
    Returns:
        Tuple of (festival_name, demand_multiplier). Returns ("", 1.0) if no festival.
    """
    month = date.month
    day = date.day
    for festival_id, festival_data in FESTIVALS.items():
        if festival_data["month"] == month and day in festival_data["days"]:
            return festival_data["name"], festival_data["multiplier"]
    return "", 1.0


def calculate_trend(
    sales: int,
    baseline: float,
    prev_sales: Optional[int] = None
) -> Tuple[str, float, float, Optional[float]]:
    """
    Calculate trend label and score from sales data.
    
    This function centralizes the trend calculation logic used by both
    brand_simulation and simulation_service modules.
    
    Args:
        sales: Current period sales (units)
        baseline: Expected baseline sales for comparison
        prev_sales: Previous period sales for month-over-month growth
        
    Returns:
        Tuple of (trend_label, trend_score, growth_vs_baseline, mom_growth)
        - trend_label: "uptrend", "downtrend", or "sideways"
        - trend_score: Combined score (-1 to +1 range)
        - growth_vs_baseline: Percentage growth vs baseline
        - mom_growth: Month-over-month growth (None if prev_sales not provided)
    """
    # Calculate growth vs baseline
    growth_vs_baseline = 0.0
    if baseline > 0:
        growth_vs_baseline = (sales - baseline) / baseline
    
    # Calculate month-over-month growth
    mom_growth: Optional[float] = None
    if prev_sales is not None and prev_sales > 0:
        mom_growth = (sales - prev_sales) / prev_sales
    
    # Determine trend label
    up_cond = (growth_vs_baseline >= 0.15) or (mom_growth is not None and mom_growth >= 0.10)
    down_cond = (growth_vs_baseline <= -0.10) or (mom_growth is not None and mom_growth <= -0.10)
    
    if up_cond and not down_cond:
        trend_label = "uptrend"
    elif down_cond and not up_cond:
        trend_label = "downtrend"
    else:
        trend_label = "sideways"
    
    # Calculate trend score
    trend_score = 0.7 * growth_vs_baseline + 0.3 * (mom_growth if mom_growth is not None else 0.0)
    
    return trend_label, trend_score, growth_vs_baseline, mom_growth


def clean_data_for_json(data: Any) -> Any:
    """
    Clean data for JSON serialization by converting NumPy and Pandas types.
    
    Handles: numpy floats/ints, pandas Timestamp, NaN values, booleans.
    
    Args:
        data: Any data structure (dict, list, or primitive)
        
    Returns:
        JSON-serializable version of the data
    """
    if isinstance(data, dict):
        return {k: clean_data_for_json(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_data_for_json(item) for item in data]
    elif isinstance(data, np.floating):
        return float(data) if not np.isnan(data) else 0.0
    elif isinstance(data, np.integer):
        return int(data)
    elif isinstance(data, (np.bool_, bool)):
        return bool(data)
    elif isinstance(data, (pd.Timestamp, datetime)):
        return data.strftime('%Y-%m-%d')
    elif data is None:
        return None
    elif pd.isna(data):
        return 0.0
    else:
        return data