# Simple Battle Simulator

This is a basic Python battle simulation between two characters: a heroic Knight and a mischievous Goblin. The game demonstrates object-oriented programming principles such as classes, methods, and interaction between objects.

## File Structure

- `character.py`: Defines the `Character` class with attributes and methods for combat.
- `main.py`: Runs the battle simulation using two instances of `Character`.

## Character Class

Located in `character.py`, the `Character` class includes:

### Attributes
- `name` (str): The character's name.
- `hp` (int): Hit points (health).
- `attack_power` (int): Damage dealt per attack.

### Methods
- `attack(other)`: Reduces the `other` character's HP by `attack_power` and prints an attack message.
- `is_alive()`: Returns `True` if HP is greater than 0.
- `__str__()`: Returns a string representation of the character's current HP.

##  How the Battle Works

The battle logic in `main.py` follows these steps:

1. Create two characters: Knight and Goblin.
2. Print their initial stats.
3. Loop while both are alive:
   - Knight attacks Goblin.
   - If Goblin survives, Goblin attacks Knight.
   - Print updated stats.
4. Declare the winner when one character's HP reaches zero.

##  Running the Game

To run the simulation, execute `main.py`:

```bash
python main.py

##  Student Implementations
Implementations include 
1: Changing the Logical Proposition in the while loop from P^Q^R to P^(Q v R) to prevent the game ending when one enemy has died
2: Adding in random.randint function in charachter.py to randomize a damage coefficient between 30-90%
