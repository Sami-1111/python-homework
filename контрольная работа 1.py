from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    @abstractmethod
    def action(self):
        pass


class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        print(f"Маг {self.name} кастует заклинание! MP: {self.mp}")


class WarriorHero(MageHero):
    def action(self):
        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl}")


class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name

    def login(self, password):
        return password == self.__password

    @property
    def full_info(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        else:
            raise ValueError("Нельзя сложить счета героев разных классов!")

    def __eq__(self, other):
        return (
            type(self.hero) == type(other.hero)
            and self.hero.lvl == other.hero.lvl
        )


mage1 = MageHero("Merlin", 100, 1000, 150)
mage2 = MageHero("Gandalf", 100, 1000, 200)
warrior = WarriorHero("Conan", 99, 1000, 50)


acc1 = BankAccount(mage1, 5000, "2810", "Simba")
acc2 = BankAccount(mage2, 3000, "6666", "Simba")
acc3 = BankAccount(warrior, 7000, "9999", "Simba")


mage1.action()
warrior.action()


print(acc1)
print(acc2)

print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

print("\n=== Проверка __add__ ===")

print("Сумма счетов двух магов:", acc1 + acc2)

try:
    print("Сумма мага и воина:", acc1 + acc3)
except ValueError as error:
    print("Ошибка:", error)

print("\n=== Проверка __eq__ ===")

print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)