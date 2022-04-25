# Why we use Class???

champ1_name = "Ezreal"
champ1_health = 700
champ1_attack = 90

print(f" Gamer {champ1_name}. Welcome to Summoner's Canyon.")

champ2_name = "Lee Sin"
champ2_health = 900
champ2_attack = 85

print(f" Gamer {champ2_name}. Welcome to Summoner's Canyon.")

def basic_attack(name, attack):
    print(f"{name} basic-attack power {attack}")

basic_attack(champ1_name, champ1_attack)
basic_attack(champ2_name, champ2_attack)

print("============Case in using Class.=========")

class Champion: 
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"Gamer {name}. Welcome to EVERLAND PARK")    
    def basic_attack(self):
        print(f"{self.name} normal strike {self.attack}")

Jayce = Champion("Jayce", 769, 100)
Teemo = Champion("Teemo", 600, 60)
Jhin = Champion("Jhin", 875, 87)
Jayce.basic_attack()
Teemo.basic_attack()
Jhin.basic_attack()

# It's easy to make output





