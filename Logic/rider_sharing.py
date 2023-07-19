from . import constants as C
from . import models

drivers = {}
riders = {}
matches = {}
rides_details = {}
generated_bill = {}


def add_driver(driver_id: str, x_coordinate: float, y_coordinate: float) -> None:
    if drivers.get(driver_id):
        print(C.INVALID_RIDE)
        return

    new_driver = models.Driver(id=driver_id,
                               location=models.Coordinates(x=x_coordinate, y=y_coordinate),
                               is_available=True)

    drivers[new_driver.id] = [(new_driver.location.x, new_driver.location.y), new_driver.is_available]


def add_rider(rider_id: str, x_coordinate: float, y_coordinate: float) -> None:
    if riders.get(rider_id):
        print(C.INVALID_RIDE)
        return

    new_rider = models.Rider(id=rider_id,
                             location=models.Coordinates(x=x_coordinate, y=y_coordinate),
                             is_riding=False)

    riders[new_rider.id] = [(new_rider.location.x, new_rider.location.y), new_rider.is_riding]


def match(rider_id: str) -> None:
    if len(drivers) == 0:
        print(C.NO_DRIVERS_AVAILABLE)
        return

    rider_location = riders.get(rider_id)
    if rider_location is None:
        print(C.INVALID_RIDE)
        return

    available_driver = []
    for driver_id, driver_location in drivers.items():
        # print(driver_location)
        if driver_location[-1]:
            distance = models.Distance(driver_location=driver_location[0],
                                       rider_location=rider_location[0])

            if float(distance.distance) <= 5:
                available_driver.append((driver_id, distance.distance))

    if not available_driver:
        print(C.NO_DRIVERS_AVAILABLE)
        return

    available_driver.sort(key=lambda x: [x[1], x[0]])
    matched_driver = [driver_id for driver_id, _ in available_driver[:5]]
    matches[rider_id] = matched_driver
    print(C.DRIVERS_MATCHED, ' '.join(matched_driver))


def start_ride(ride_id: str, n: int, rider_id: str) -> None:
    # print(drivers, riders, rides_details)
    if ride_id in rides_details:
        print(C.INVALID_RIDE)
        return

    matched_drivers = matches.get(rider_id)
    if not matched_drivers or n > len(matched_drivers):
        print(C.INVALID_RIDE)
        return

    driver_id = matched_drivers[n - 1]
    driver = drivers[driver_id]
    driver[-1] = False
    matches[rider_id] = driver_id
    rides_details[ride_id] = [rider_id, driver_id, "STARTED"]
    print(C.RIDE_START, f" {ride_id}")


def stop_ride(ride_id: str,
              destination_x_coordinate: float,
              destination_y_coordinate: float,
              time_taken: int) -> None:
    ride_detail = rides_details.get(ride_id)
    if not ride_detail or ride_detail[-1] == "STOPPED":
        print(C.INVALID_RIDE)
        return

    print(C.RIDE_STOP, f" {ride_id}")
    ride_detail[-1] = "STOPPED"
    rider = riders.get(ride_detail[0])[0]
    gen_bill = models.GenerateBill(rider_location=models.Coordinates(x=rider[0], y=rider[1]),
                                   destination=models.Coordinates(x=destination_x_coordinate,
                                                                  y=destination_y_coordinate),
                                   time_taken=time_taken)
    generated_bill[ride_id] = [ride_id, ride_detail[1], gen_bill.total_bill]
    # print("Total Bill Generated:: ", generated_bill[ride_id])


def bill(ride_id: str) -> None:
    ride_detail = rides_details.get(ride_id)
    if not ride_detail:
        print(C.INVALID_RIDE)
        return

    if ride_detail[-1] == "STARTED":
        print(C.RIDE_NOT_COMPLETED)
        return

    print(f"BILL {ride_id} {generated_bill[ride_id][1]} {generated_bill[ride_id][2]}")
