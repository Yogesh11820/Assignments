class Animals:
    def __init__(self, name,color,age):
        self.name = name
        self.color = color
        self.age = age

class Cow(Animals):
    def __init__(self, name):
        super().__init__(name,'Brown',10)

class Horse(Animals):
    def __init__(self, name):
        super().__init__(name,'White',15)

class Dog(Animals):
    def __init__(self, name):
        super().__init__(name,'Black',5)

c = Cow("Bella")
print(f'{c.name} is {c.age} years old and his color is {c.color} ')

h = Horse("Chetak")
print(f'{h.name} is {h.age} years old and his color is {h.color} ')

d = Dog("Brian")
print(f'{d.name} is {d.age} years old and his color is {d.color} ')
