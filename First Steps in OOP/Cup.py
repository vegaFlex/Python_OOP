class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        if self.status() >= milliliters:
            self.quantity += milliliters

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())


# CORRECT:_________________
# class Cup:
#     def __init__(self, size, quantity):
#         self.size = size
#         self.quantity = min(quantity, size)  # Ensure quantity doesn't exceed cup size
#
#     def fill(self, quantity):
#         space_left = self.size - self.quantity
#         if quantity <= space_left:
#             self.quantity += quantity
#
#     def status(self):
#         return self.size - self.quantity


# CORRECT:_________________
# class Cup:
#     def __init__(self, size, quantity):
#         self.size = size
#         self.quantity = quantity
#
#     def fill(self, qty):
#         free_space = self.size - self.quantity
#         if qty <= free_space:
#             self.quantity += qty
#
#     def status(self):
#         return self.size - self.quantity

