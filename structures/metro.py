from pydantic import BaseModel
from enum import Enum
from datetime import time

from structures.plane import Airport
from structures.station import Station
from structures.train import TrainStation


class MetroType(str, Enum):
    """
    Enum representing different types of metro systems.
    Compared to `train`, metro systems do not have a fixed schedule, so passengers can board at any time without
    prepurchasing a ticket.
    """
    SUBWAY = "subway" # Underground metro system, which is the most common type of metro system, e.g., the MTR in
    # Hong Kong, MRT in Singapore.
    LIGHT_RAIL = "light_rail" # Light rail system
    TRAM = "tram" # Tram system, like The Tram in Hong Kong, or the Tram in Melbourne
    MAGLEV = "maglev" # Magnetic levitation train system
    EXPRESS = "express" # Typically with fewer stops but have separate tracks from local trains, and often have more
    # expensive fares, e.g., AirPort Express in Hong Kong, or Airport Link in Shanghai.
    CABLE_CAR = "cable_car" # Cable car system, e.g., San Francisco's cable cars, or the Ngong Ping 360 in Hong Kong.

class MetroStation(BaseModel):
    """
    Model representing a metro station.
    """
    code: str # Code of the metro station
    name: str # Name of the metro station, native name in the local language, e.g., "中環" (Central) in Hong Kong.
    name_en: str = None # Name of the metro station in English, e.g., "Central" in Hong Kong
    id: str # Unique identifier for the metro station
    station: 'Station' # Basic information about the metro station, such as its location, type, etc.
    metro_type: MetroType = MetroType.SUBWAY # Type of the metro system, default is SUBWAY
    transfer: bool = False # Whether this station is a transfer station (i.e., where multiple metro lines intersect)
    connect_airport: 'Airport' = None # Airport connected to this metro station, if any (e.g., Hong Kong Airport Express)
    connect_train: 'TrainStation' = None # Train station connected to this metro station, if any (e.g., Hong Kong Airport Express)

class MetroLine(BaseModel):
    """
    Model representing a metro line.
    """
    name: str # Name of the metro line (official, native), e.g., "Red Line,"
    # "港島綫" (Island Line), "1 号线" (Line 1), etc.
    name_en: str = None # Name of the metro line in English, e.g., "Red Line," "Island Line," "Line 1," etc.
    alias: str = None # Alias of the metro line, e.g., "Red Line" or "Blue Line"
    id: str # Unique identifier for the metro line
    color: str = None # Color of the metro line, e.g., "#FF0000" for red
    metro_type: MetroType = MetroType.SUBWAY
    branches: list['MetroLineBranch'] = [] # List of branches for this metro line. If it's `Y`-shaped,
    # it will have multiple branches. Each branch contains a full list of stations and periods, even if duplicated.

class MetroLineBranch(BaseModel):
    """
    Model representing a branch of a metro line.
    """
    line: MetroLine # The main metro line this branch belongs to
    branch_name: str # Name of the branch, e.g., "Branch A"
    stations: list[MetroStation] # List of stations on this branch
    periods: list[tuple[MetroStation, MetroStation, time, time, float]] = [] # List of periods with start and end times, and frequency in minutes.
    # Each tuple contains (start_station, end_station, start_time, end_time, frequency)
