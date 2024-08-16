from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name):
        super().__init__(name, Cake.PRICE, Cake.GRAMS, Cake.CALORIES)
        # True:
        # super().__init__(name, self.PRICE, self.GRAMS, self.CALORIES)
