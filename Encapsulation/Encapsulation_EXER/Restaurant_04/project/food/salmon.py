from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name, price):
        super().__init__(name, price, Salmon.GRAMS)

