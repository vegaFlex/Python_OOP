from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name


fruit = Fruit('apple', '2020-01')
a = 5
