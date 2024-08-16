from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
