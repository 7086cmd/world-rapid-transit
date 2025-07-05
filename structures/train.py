from pydantic import BaseModel
from enum import Enum
from datetime import time
from structures.station import Station


class TrainStation(BaseModel):
    """
    Model representing a train station.
    """
    code: str # Code of the train station
    name: str # Name of the train station, native name in the local language, e.g., "東京" (Tokyo) in Japan,
    # or "香港西九龍" (Hong Kong West Kowloon) in Hong Kong.
    name_en: str = None # Name of the train station in English, e.g., "Tokyo" in Japan
    id: str # Unique identifier for the train station
    station: 'Station' # Basic information about the train station, such as its location, type, etc.

class TrainType(str, Enum):
    """
    Enum representing different types of trains.
    """
    HIGH_SPEED = "high_speed" # High-speed train, e.g., Shinkansen in Japan, TGV in France
    REGIONAL = "regional" # Regional train, e.g., Intercity trains
    COMMUTER = "commuter" # Commuter train, e.g., suburban trains

class TrainCarrier(BaseModel):
    """
    Model representing a train carrier.
    """
    name: str # Name of the train carrier, e.g., "Amtrak"
    country: str
    abbr: str = None # Abbreviation of the train carrier, e.g., "AMT" for Amtrak
    parent: 'TrainCarrier' = None # Parent train carrier if this is a subsidiary or part of a larger train group

class Train(BaseModel):
    """
    Model representing a train.
    """
    train_number: str # Train number, e.g., "TGV1234"
    carrier: TrainCarrier # Train carrier operating the train, e.g., "Amtrak"
    region: str # Region where the train operates
    departure_station: TrainStation # Departure train station
    arrival_station: TrainStation # Arrival train station
    departure_time: time # Departure time in ISO 8601 format
    arrival_time: time # Arrival time in ISO 8601 format
    duration: int # Duration of the train journey in minutes
    stops: list[tuple[TrainStation, time]] = [] # List of stopover train stations with their arrival times
    train_type: TrainType = TrainType.REGIONAL # Type of the train, default is REGIONAL
