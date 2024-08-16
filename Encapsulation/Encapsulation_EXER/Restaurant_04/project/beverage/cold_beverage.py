from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)