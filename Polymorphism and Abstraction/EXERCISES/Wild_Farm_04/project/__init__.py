from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Owl
from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Meat, Vegetable

owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)

# hen = Hen("Harry", 10, 10)
# veg = Vegetable(3)
# fruit = Fruit(5)
# meat = Meat(1)
# print(hen)
# print(hen.make_sound())
# hen.feed(veg)
# hen.feed(fruit)
# hen.feed(meat)
# print(hen)
