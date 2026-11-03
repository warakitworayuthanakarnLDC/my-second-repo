import random
#self.attack_power causes damage to hp randomly between 30% to 90% of the initial power set at object creation
class Character:
    def __init__(self, name, hp, attack_power):
        rng_damage_coefficient = random.randint(30,90)
        self.name = name
        self.hp = hp
        self.attack_power = (attack_power/100) * rng_damage_coefficient

    def attack(self, other):
        other.hp -= self.attack_power
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp:.2f} HP"


