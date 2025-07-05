from datetime import time
from enum import Enum
from pydantic import BaseModel

from structures.station import Station


class AirportType(str, Enum):
    """
    Enum representing different types of airports.
    """
    INTERNATIONAL = "international"
    DOMESTIC = "domestic"
    REGIONAL = "regional"

class Airport(BaseModel):
    """
    Model representing an airport station.
    """
    code: str # IATA code of the airport
    airport_type: 'AirportType' # Type of the airport
    mixed_use: bool = False # Whether the airport has mixed-use facilities (i.e., both civilian and military operations)
    name: str # Name of the airport (English name, e.g., "John F. Kennedy International Airport")
    operating_city: str # IATA city name where the airport is classified in IATA. For example, we should fill "NYC" here for Newark Liberty Airport (EWR)
    id: str # Unique identifier for the airport
    station: 'Station'

class Flight(BaseModel):
    """
    Model representing a flight.
    """
    flight_number: str # Flight number, e.g., "AA100"
    airline: 'Airline' # Airline operating the flight, e.g., "American Airlines"
    departure_airport: Airport # Departure airport
    arrival_airport: Airport # Arrival airport
    departure_time: time # Departure time in ISO 8601 format (estimated)
    arrival_time: time # Arrival time in ISO 8601 format (estimated)
    duration: int # Duration of the flight in minutes
    stops: list['Airport'] = [] # List of stopover airports, if any
    international: bool = False # Whether the flight is international (i.e., crossing country borders)
    codeshared: 'Flight' = None # Codeshare flight if this flight is a codeshare,
    # or leave `None` if this flight is not a codeshare.

class Airline(BaseModel):
    """
    Model representing an airline.
    *Hereby examples are from my favorite airlines, so they may not be the most popular airlines in the world.*
    """
    name: str # Name of the airline, e.g., "Singapore Airlines" or "Cathay Pacific Airways"
    code: str # IATA code of the airline, e.g., "SQ" for Singapore Airlines or "CX" for Cathay Pacific Airways
    id: str # Unique identifier for the airline
    country: str # Country where the airline is based
    hub_airports: list['Airport'] = [] # List of hub airports for the airline
    lcc: bool = False # Whether the airline is a low-cost carrier (LCC) (i.e., budget airline)
    parent_airline: 'Airline' = None # Parent airline if this is a subsidiary or part of a larger airline group, e.g.,
    # "Scoot" is a subsidiary of "Singapore Airlines," whereas "HK Express" is a subsidiary of "Cathay Pacific Airways."
    # If this is not a subsidiary, this field should be None.
    alliance: 'Alliance' = None # Airline alliance this airline is part of, e.g., "Star Alliance," "Oneworld," or
    # "SkyTeam." It can also be regional, e.g., "Vanilla Alliance."
    website: str = None # Website of the airline, e.g., "https://www.singaporeair.com" or "https://www.cathaypacific.com"

class Alliance(BaseModel):
    """
    Model representing an airline alliance.
    """
    name: str # Name of the alliance, e.g., "Star Alliance"
    id: str # Unique identifier for the alliance
    worldwide: bool = False # Whether the alliance is a worldwide alliance
    # (limited to: "Star Alliance," "Oneworld," or "SkyTeam")
    website: str = None # Website of the alliance, e.g., "https://www.staralliance.com," "https://www.oneworld.com," or "https://www.skyteam.com."
