from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Food


class MainDish(Food):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)