from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Product


class Beverage(Product):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price)
        self.__milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters

