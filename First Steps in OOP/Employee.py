class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        return self.salary * 12

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary


employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())

# employee1 = Employee(1234, "Veg", "Fleg", 10)
# print(employee1.get_full_name())
# print(employee1.raise_salary(50))
# print(employee1.get_annual_salary())
