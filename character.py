import random
#self.attack_power causes damage to hp randomly between 30% to 90% of the initial power set at object creation
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power 

    def attack(self, other):
        rng_damage = ( self.attack_power / 100 ) * random.randint(30,90)
        other.hp -= rng_damage
        print(f"{self.name} attacks {other.name} for {rng_damage:.2f} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp:.2f} HP"


