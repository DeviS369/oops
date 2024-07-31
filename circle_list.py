class Circle:
    def __init__(self, radius):
        if isinstance(radius, list):
            self.radius = radius
        else:
            raise ValueError("The argument must be a list")

    def get_radius(self):
        return self.radius

# Example usage:
circle = Circle([10, 501, 22, 37, 100, 999, 87, 351])
print(circle.get_radius())
