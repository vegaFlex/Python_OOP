from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Child
from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Person

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)

