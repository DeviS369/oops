"""
Program 2 :Create proper member variables inside the task if required
and usse them when neccessary .For example for this task create 
a class private variable named  pi = 3.141
"""
#ccreate class
class Circle:
    # Private class variable
    __pi = 3.141  

    def __init__(self, radius):
    # Private instance variable
        self.__radius = radius  

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return self.__calculate_area(self.__radius)

    def __calculate_area(self, radius):
        return self.__pi * (radius ** 2)

# Example usage:
circle = Circle(10)
print("Radius:", circle.get_radius())
print("Area:", circle.get_area())

circle.set_radius(501)
print("Radius:", circle.get_radius())
print("Area:", circle.get_area())
