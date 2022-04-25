# 상속
"""
    - Remove overlapping code in Class
    - Make maintenance easily 
"""
"""
    Fruit
    
    Apple, Watermelon , grape  are Fruit. 
    Fruit inherit its nature to  Apple, Watermelon, grape .
"""

import random
# Defining a Parent Class 

# Class Variable 
# Variables shared by all instances


class Monster:
    max_num = 1000  # Maximun Monster 
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1
    def move(self):
        print(f"[{self.name}] Move on the ground.")
        
class Wolf(Monster):    # Wolf is inherit from Monster.
    pass        # Use function definition.

class Shark(Monster):   
    def move(self):
        print(f"[{self.name}] Swim - Swim") # method overriding -> method redefine
        
class Dragon(Monster):
    # constructor overriding
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)  
        # Can bring Parent Class's __init__() method variable.
        # super() : Inherited Parent Class
        self.skills = ("FireBall", "Swing Tales", "Wing Strike")
         
    def move(self):
        print(f"[{self.name}] Fly High")
        
    def skill(self): 
        print(f"[{self.name}] Use Skills -->  {self.skills[random.randint(0,2)]}")
        
wolf = Wolf("der Wolf", 1000, 222)
wolf.move()
print(wolf.max_num)

shark = Shark("Weißer Hai", 2222, 400)
shark.move()
print(shark.max_num)


dragon = Dragon("Drachen.", 7890, 1000) 
# fourth value --> skill name 
dragon.move()
dragon.skill()
print(dragon.max_num)


# Overriding And Class variable

"""
    In Dragon Class, Add 3 skills per instance attribute. 
    
    Dragon uses skill randomly.
"""
