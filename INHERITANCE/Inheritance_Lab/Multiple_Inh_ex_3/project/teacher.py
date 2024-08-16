from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Employee
from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."


pers = Teacher()
print(pers.teach())
print(pers.sleep())
print(pers.get_fired())
