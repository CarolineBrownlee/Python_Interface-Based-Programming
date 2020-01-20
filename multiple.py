# Class Lecture Notes:
# This is object-oriented programming.

class Animal:
    def say_animal (self):
        return "I am an animal"

class AnimalFriend:
    def say_friend (self):
        return "My friend is the farmer."

class Cow(Animal, AnimalFriend):
    def say_cow_thing(self):
        print(f"{self.say_animal()} and {self.say_friend()}")

Bossie = Cow()
Bossie.say_cow_thing()