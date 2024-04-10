from weapon import fists

class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.max_health = health

        self.weapon = fists

    def attack(self, target) -> None:
       target.health -= self.weapon.damage 
       target.health = max(target.health, 0)
       print(f"{self.name} dealt {self.weapon.damage} to {target.name} with {self.weapon.name}")

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} has equipped a(n) {weapon.name}!")

    def drop(self) -> None:
        print(f"{self.name} dropped the {self.weapon}!")
        self.weapon = self.default_weapon

class Hero(Character):
    def __init__(self, name:str, health: int) -> None:
        super().__init__(name=name, health=health)

        self.default_weapon=self.weapon

class Enemy(Character):
    def __init__(self, name:str, health: int, weapon) -> None:
        super().__init__(name=name, health=health)
        self.weapon=weapon


