class Garage:
    def __init__(self):
        self.vehicle = None

    def setVehicle(self, vehicle_parked):
        # parking the vehicle in the garage
        self.vehicle = vehicle_parked

    def toString(self):
        return f'Description of the parked vehicle: \n{self.vehicle.toString()}'

