from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Mammal


class Mouse(Mammal):
    ALLOWED_FOODS = ['Vegetable', 'Fruit']
    WEIGHT_INCREMENTAL = 0.1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREMENTAL = 0.4

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    ALLOWED_FOODS = ['Vegetable', 'Meat']
    WEIGHT_INCREMENTAL = 0.3

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREMENTAL = 1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"
