from abc import ABC, abstractmethod

from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Food


class Animal(ABC):
    ALLOWED_FOODS = []
    WEIGHT_INCREMENTAL = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        food_type = food.__class__.__name__
        if food_type not in self.ALLOWED_FOODS:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += food.quantity * self.WEIGHT_INCREMENTAL
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
