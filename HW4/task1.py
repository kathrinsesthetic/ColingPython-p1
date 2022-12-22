class SpaceObject:
    def __init__(self, name):
        self.name = name

class Planet(SpaceObject):
    def __init__(self, name, population=None):
        super().__init__(name)
        self.population = population or []

    def __str__(self):
        return f"On the planet {self.name} live {len(self.population)} animals:\n" \
        f"{', '.join([animal.name for animal in self.population])}"

class Animal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

    def settle(self, planet):
        planet.population.append(self)

class Dog(Animal):
    def __init__(self, name, color=None, breed=None, host_name=None):
        super().__init__(name)
        self.color = color
        self.breed = breed
        self.host_name = host_name
        self.energy = 0
        self.skills = 0

    def eat(self, amount=10):
        self.energy += amount
        print(f"Dog {self.name} is fed {amount} kg meat")

    def train(self):
        self.skills += 1
        print(f"Dog {self.name} knows now {self.skills} tricks")

class Octopus(Animal):
    def __init__(self, name, color=None):
        super().__init__(name)
        self.eyes = "dark"
        self.color = color

    def joke(self):
        print(f"Octopus {self.name} splashes!")

class Elefant(Animal):
    def __init__(self, name, age=None, food='banana'):
        super().__init__(name)
        self.age = age
        self.food = food
        self.curiosity = False

    def become_curiosity_unit(self):
        self.curiosity = True

    def find(self, food='banana'):
        if self.curiosity:
            print(f"Elephant {self.name} has found {food}")
        else:
            print(f"Elephant {self.name} doesn't have enough strength.")

earth = Planet('Earth')

dogs = [Dog('Corzik', 'beige', 'Bulldog', 'Vasya'),
        Dog('Cake', 'white', 'German Boxer', 'Petya')]
octopuses = [Octopus('Steve'), Octopus('Mark')]
elephants = [Elefant(f'Elephant_{i}', i * 2) for i in range(10)]

animals = [dogs, octopuses, elephants]
for specie in animals:
    for animal in specie:
        animal.settle(earth)

print(earth)