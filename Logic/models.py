import dataclasses
import math

from . import constants as C


@dataclasses.dataclass
class Coordinates:
    x: float
    y: float


@dataclasses.dataclass
class Driver:
    id: str
    location: Coordinates
    is_available: bool = False


@dataclasses.dataclass
class Rider:
    id: str
    location: Coordinates
    is_riding: bool = False


@dataclasses.dataclass
class Distance:
    rider_location: tuple
    driver_location: tuple

    def __post_init__(self):
        self.distance = math.sqrt((self.rider_location[0] - self.driver_location[0]) ** 2 +
                                  (self.rider_location[1] - self.driver_location[1]) ** 2)
        self.distance = "{:.2f}".format(self.distance)
        return self.distance


@dataclasses.dataclass
class GenerateBill:
    rider_location: Coordinates
    destination: Coordinates
    time_taken: int

    def __post_init__(self):
        self.distance = math.sqrt((self.rider_location.x - self.destination.x) ** 2 +
                                  (self.rider_location.y - self.destination.y) ** 2)
        self.distance = "{:.2f}".format(self.distance)
        # print(C.CHARGE_SHEET["DISTANCE_CHARGE"], self.distance)
        bill = C.CHARGE_SHEET["BASE"] + (float(self.distance) * C.CHARGE_SHEET["DISTANCE_CHARGE"]) + \
                    (self.time_taken * C.CHARGE_SHEET["TIME_TAKEN"])
        service_tax = bill * C.CHARGE_SHEET["SERVICE_TAX"]
        self.total_bill = "{:.2f}".format((bill + service_tax))
        return float(self.total_bill)
