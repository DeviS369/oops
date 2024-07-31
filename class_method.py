"""
Program 3 :From the given list create two class Methods Area and Perimeter 
which will be going to the Area and Perimeter 
"""
class Circle:
    __pi = 3.141  # Private class variable

    @classmethod
    def area(cls, radii):
        #Calculate the area for each radius in the list.
        return [cls.__calculate_area(radius) for radius in radii]

    @classmethod
    def perimeter(cls, radii):
        #Calculate the perimeter for each radius in the list.
        return [cls.__calculate_perimeter(radius) for radius in radii]

    @classmethod
    def __calculate_area(cls, radius):
        return cls.__pi * (radius ** 2)

    @classmethod
    def __calculate_perimeter(cls, radius):
        return 2 * cls.__pi * radius

# Example usage:
radii = [10, 501, 22, 37, 100, 999, 87, 351]
areas = Circle.area(radii)
perimeters = Circle.perimeter(radii)

print("Radii:", radii)
print("Areas:", areas)
print("Perimeters:", perimeters)
