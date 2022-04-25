# item  --> name, price, weight, sell, dump
# equipment --> put_on_effect, put_on
# supply --> use_effect, use

class Item: 
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
        
    def sell(self):
        print(f"[{self.name}]  Prics is [{self.price}]")
        
    def can_dump(self):     # can dump or can't dump
        if self.isdropable:
            print(f"[{self.name}] is disappeard.[{self.price}]  is deleted. ")
            
        else:
            print(f"[{self.name}] is not disappeard.")


class equipment(Item):  # equipment
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def wear(self):
        print(f"[{self.name}] put on!! {self.effect}")

class supply(Item):  # supply
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def use(self):
        print(f"[{self.name}] use!  {self.effect}")

# Make Instance
sword = equipment("BlackSword" , 33333, 3.5, True, "Strike + 100 Health + 400")
sword.wear()
sword.sell()
sword.can_dump()

potion = supply("Corrupting Potion", 500, 0.1, False, "Restore health + 200 mana + 100 All_Ability + 10")
potion.can_dump()
potion.sell()
potion.use()

