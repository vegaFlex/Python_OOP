class Circle:
    # Class attribute
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    # Instance method to set a new radius
    def set_radius(self, new_radius):
        self.radius = new_radius

    # Instance method to calculate and return the area of the circle
    def get_area(self):
        area = self.pi * (self.radius ** 2)
        return round(area, 2)

    # Instance method to calculate and return the circumference of the circle
    def get_circumference(self):
        circumference = 2 * self.pi * self.radius
        return round(circumference, 2)


# Example usage:
circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())  # Output: 452.16
print(circle.get_circumference())  # Output: 75.36
