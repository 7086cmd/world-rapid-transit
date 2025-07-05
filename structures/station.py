from enum import Enum
from pydantic import BaseModel

class StationType(str, Enum):
    """
    Enum representing different types of stations.
    """
    AIRPORT = "airport"
    TRAIN = "train"
    METRO = "metro"
    BUS = "bus"
    PORT = "port"

class Station(BaseModel):
    """
    Model representing a transportation station.
    """
    name: str # Name of the station
    type: StationType # Type of the station (e.g., airport, train, metro, etc.)
    latitude: float # Latitude coordinate of the station
    longitude: float # Longitude coordinate of the station
    city: str # City where the station is located
    country: str # Country where the station is located
