from EXAM_PREPAR_II_1_08_24_Python_OOP_06_2024.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.0

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage: float):
        percentage_used = round((mileage / self.max_mileage) * 100)
        self.battery_level = max(self.battery_level - percentage_used - 5, 0)
