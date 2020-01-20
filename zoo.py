from animals import Penguin, PaintedDog
from habitats import Aquarium
from habitats import Habitat


bob = Penguin("Bob")
bob.run()
bob.swim()

Reggie = Penguin("Reggie")
ralph = PaintedDog("Ralph")

# Create a habitat
seaworld = Aquarium("Sea World")
seaworld.add_animal(bob)

Grassmere = Habitat("Grassmere")
Grassmere.add_animal(Reggie)

Home = Habitat("Home")
Home.add_animal(ralph)

for animal in seaworld.animals:
    print(animal)

for animal in Grassmere.animals:
    print(animal)

for animal in Home.animals:
    print(animal)

seaworld.add_swimmer_pythonic(bob)
seaworld.add_swimmer_pythonic(ralph)

for animal in seaworld.animals:
    print(f'{animal} lives in Sea World')






