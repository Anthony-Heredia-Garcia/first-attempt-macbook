class Weapon:
    def __init__(self, name:str, weapon_type:str, damage:int, value:int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

iron_sword = Weapon(name="Iron Sword", weapon_type="Slashing", damage=5, value=10)
short_bow = Weapon(name="Shortbow", weapon_type="Ranged", damage=4, value=8)
fists = Weapon(name="Fists", weapon_type="Unarmed", damage=3, value=0)
