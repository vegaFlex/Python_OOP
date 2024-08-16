from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Topping


class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        # TRUE:
        # # if self.__toppings_capacity >= topping.weight:
        # if len(self.toppings) < self.__toppings_capacity:
        #     if topping.topping_type not in self.toppings:
        #         self.toppings[topping.topping_type] = 0
        #     self.toppings[topping.topping_type] += topping.weight
        #     # self.__toppings_capacity -= 1
        # else:
        #     raise ValueError("Not enough space for another topping")
        if len(self.toppings) == self.toppings_capacity:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        # sum_toppings_weight = sum([value for value in self.toppings.values()])
        sum_toppings_weight = sum(self.toppings.values())
        result = self.dough.weight + sum_toppings_weight

        return result

