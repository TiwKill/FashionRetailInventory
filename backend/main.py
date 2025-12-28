from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import uvicorn

from routers import simulation
from services.data_service import init_data, get_historical_data, get_brand_parameters, get_supported_brands
from utils.helpers import clean_data_for_json
from utils.constants import SEASON_MAPPING, FESTIVALS
from models.pydantic import SeasonInfo, FestivalInfo, SeasonFestivalResponse

app = FastAPI(title="Inventory Simulation API")

# Enable CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(simulation.router)


# ============================================================
# Root Endpoints
# ============================================================

@app.get("/")
def read_root() -> Dict[str, Any]:
    """Root endpoint with API information."""
    return {
        "message": "Inventory Simulation API with Season & Festival Analysis",
        "version": "2.0.1",
        "data_loaded": get_historical_data() is not None,
        "brands_available": list(get_brand_parameters().keys()) if get_brand_parameters() else [],
        "endpoints": {
            "POST /simulate": "Run inventory simulation",
            "GET /health": "Health check",
            "GET /brand-params": "Get calculated brand parameters",
            "GET /seasons-festivals": "Get season and festival information",
            "GET /available-brands": "Get available brands list"
        },
        "fixes": [
            "✅ Fixed date range handling for start_day and end_day",
            "✅ Best selling products now filtered by simulation date range",
            "✅ Monthly data correctly mapped to simulation months"
        ]
    }


@app.get("/health")
def health_check() -> Dict[str, bool]:
    """Check if the API is healthy and data is loaded."""
    return {"status": "healthy", "data_loaded": get_historical_data() is not None}


@app.get("/brand-params")
def get_brand_parameters_endpoint() -> Dict[str, Any]:
    """Get calculated parameters from historical data."""
    params = get_brand_parameters()
    if not params:
        raise HTTPException(status_code=404, detail="No historical data available")
    return clean_data_for_json(params)


@app.get("/seasons-festivals")
def get_seasons_and_festivals() -> SeasonFestivalResponse:
    """Get all season and festival information."""
    seasons = [
        SeasonInfo(
            month=month,
            season_name=data["name"],
            quarter=data["quarter"],
            season_type=data["type"]
        )
        for month, data in SEASON_MAPPING.items()
    ]

    festivals = [
        FestivalInfo(
            festival_id=festival_id,
            name=data["name"],
            month=data["month"],
            days=data["days"],
            demand_multiplier=data["multiplier"]
        )
        for festival_id, data in FESTIVALS.items()
    ]

    return SeasonFestivalResponse(seasons=seasons, festivals=festivals)


@app.get("/available-brands")
def get_available_brands() -> Dict[str, Any]:
    """Get list of available brands from historical data."""
    brands = get_supported_brands()
    if not brands:
        raise HTTPException(status_code=404, detail="No historical data available")
    
    return {
        "brands": brands,
        "count": len(brands),
        "main_brands": brands.copy()
    }


# ============================================================
# Startup Event
# ============================================================

@app.on_event("startup")
async def startup_event():
    """Initialize data on startup."""
    init_data()


if __name__ == "__main__":
    print("🚀 Starting Inventory Simulation API with Season & Festival Analysis...")
    print("📍 API will be available at: http://localhost:8000")
    print("📖 API docs available at: http://localhost:8000/docs")
    print("\n🌦️ Season & Festival Features:")
    print(" - 12 months mapped to quarters and season types")
    print(" - 14 major festivals/holidays tracked")
    print(" - Festival multipliers affect daily demand (1.2x - 2.2x)")
    print(" - All data includes season and festival information")
    print("\n🔧 Date Range Handling:")
    print(" - start_day: Day of year (0=Jan 1, 31=Feb 1, 59=Mar 1, etc.)")
    print(" - end_day: Optional end day of year")
    print(" - Example: start_day=31, end_day=100 → Feb 1 to Apr 10")
    uvicorn.run(app, host="0.0.0.0", port=8000)