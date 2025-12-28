"""
Routers package - FastAPI route handlers.

Contains API endpoint definitions:
- simulation: Simulation endpoint
"""

from routers.simulation import router as simulation_router

__all__ = ["simulation_router"]
