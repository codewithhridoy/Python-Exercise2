#How to create a class
class Dog():
    """docstring for Dog."""
    #Class Object Attribute
    species = 'Mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

mydog = Dog('LAB', 'Sammy')
print(mydog.breed)
print(mydog.name)
print(mydog.species

class Circle():
    pi = 3.1416
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r

myCircle = Circle(3)
myCircle.set_radius((100))
print(myCircle.area())
