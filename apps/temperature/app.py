from fastapi import FastAPI, Query
from pydantic import BaseModel
import random
from typing import Dict

app = FastAPI()

ROOM_SENSORS = {
    "Living_Room": "1",
    "Bedroom": "2",
    "Kitchen": "3",
    "Unknown": "0"
}

class TemperatureResponse(BaseModel):
    location: str
    sensorId: str
    temperature: float
    unit: str = "C"

@app.get("/temperature")
async def get_temperature(
    location: str = Query(..., description="Name of room", example="Kitchen")
) -> TemperatureResponse:
    """Return random temperature for room"""
    if location not in ROOM_SENSORS:
        return {"error": "Room not found"}, 404

    return {
        "location": location,
        "sensorId": ROOM_SENSORS[location],
        "temperature": round(random.uniform(17.0, 25.0), 1),
        "unit": "C"
    }