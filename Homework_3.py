
from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Hello, I am {self.name}, my level is {self.level}")

    def rest(self):
        print(f"{self.name} is resting")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def attack(self):
        print("Warrior attacks with a sword!")


class Mage(Hero):
    def attack(self):
        print("Mage uses magic!")


class Assassin(Hero):
    def attack(self):
        print("Assassin attacks from the shadows!")


warrior = Warrior("Arthur", 10, 100, 50)
mage = Mage("Merlin", 15, 80, 40)
assassin = Assassin("Shadow", 12, 90, 60)



warrior.greet()
warrior.attack()
warrior.rest()

print()

mage.greet()
mage.attack()
mage.rest()

print()

assassin.greet()
assassin.attack()
assassin.rest()

