from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Dough
from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Pizza
from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Topping


try:
    tomato_topping = Topping("Tomato", 60)
    print(tomato_topping.topping_type)
    print(tomato_topping.weight)

    mushrooms_topping = Topping("Mushroom", 75)
    print(mushrooms_topping.topping_type)
    print(mushrooms_topping.weight)

    mozzarella_topping = Topping("Mozzarella", 80)
    print(mozzarella_topping.topping_type)
    print(mozzarella_topping.weight)

    cheddar_topping = Topping("Cheddar", 150)

    pepperoni_topping = Topping("Pepperoni", 120)

    white_flour_dough = Dough("White Flour", "Mixing", 200)
    print(white_flour_dough.flour_type)
    print(white_flour_dough.weight)
    print(white_flour_dough.baking_technique)

    whole_wheat_dough = Dough("Whole Wheat Flour", "Mixing", 200)
    print(whole_wheat_dough.weight)
    print(whole_wheat_dough.flour_type)
    print(whole_wheat_dough.baking_technique)

    p = Pizza("Margherita", whole_wheat_dough, 2)

    p.add_topping(tomato_topping)
    print(p.calculate_total_weight())

    p.add_topping(mozzarella_topping)
    print(p.calculate_total_weight())

    p.add_topping(mozzarella_topping)

except ValueError as error:
    print(f'ValueError: {error}')

# except ValueError as error:
#     print(error)

