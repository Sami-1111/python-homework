
import random


class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Hello, I am {self.name}, my level is {self.level}")

    def attack(self):
        print(f"{self.name} attacks!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} is resting...")
        self.health += 1


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print("Warrior attacks with a sword!")
        self.strength -= 1


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print("Mage casts a spell!")
        self.strength -= 1


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print("Assassin attacks from the shadows!")
        self.strength -= 1


# Creating heroes

warrior = Warrior("Arthur", 10, 100, 50, 80)
mage = Mage("Merlin", 15, 80, 40, 100)
assassin = Assassin("Shadow", 12, 90, 60, 95)


# Calling methods

warrior.greet()
warrior.attack()
warrior.rest()

mage.greet()
mage.attack()
mage.rest()

assassin.greet()
assassin.attack()
assassin.rest()


# Rock, Paper, Scissors game

print("\nChoose your hero:")
print("Warrior")
print("Mage")
print("Assassin")

choice = input("Your choice: ").capitalize()

heroes = {
    "Warrior": warrior,
    "Mage": mage,
    "Assassin": assassin
}

if choice in heroes:
    player = heroes[choice]

    opponents = []

    for hero in heroes.values():
        if hero != player:
            opponents.append(hero)

    enemy = random.choice(opponents)

    print(f"\nYou chose: {player.name}")
    print(f"Opponent: {enemy.name}")

    if choice == "Warrior" and enemy == assassin:
        print("Warrior wins!")
    elif choice == "Assassin" and enemy == mage:
        print("Assassin wins!")
    elif choice == "Mage" and enemy == warrior:
        print("Mage wins!")
    else:
        print(f"{enemy.name} wins!")

else:
    print("Invalid choice! Please choose Warrior, Mage or Assassin.")
