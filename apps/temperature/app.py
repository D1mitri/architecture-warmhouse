from fastapi import FastAPI, Query
from pydantic import BaseModel
import random
from typing import Dict

app = FastAPI()

ROOM_SENSORS = {
    "1": "Living_Room",
    "2": "Bedroom",
    "3": "Kitchen",
    "0": "Unknown"
}

class TemperatureResponse(BaseModel):
    location: str
    sensorId: str
    value: float
    unit: str = "C"

@app.get("/temperature/{sensor_id}")
async def get_temperature(sensor_id: str) -> TemperatureResponse:
    """Return random temperature for room"""

    if sensor_id not in ROOM_SENSORS:
        return {"error": "Room not found"}, 404

    return {
        "location": ROOM_SENSORS[sensor_id],
        "sensorId": sensor_id,
        "value": round(random.uniform(17.0, 25.0), 1),
        "unit": "C"
    }