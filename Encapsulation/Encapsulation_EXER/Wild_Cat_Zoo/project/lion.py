from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Animal


class Lion(Animal):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, 50)