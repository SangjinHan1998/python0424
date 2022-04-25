# item  --> name, price, weight, sell, dump
# equipment --> put_on_effect, put_on
# supply --> use_effect, use

class Item: 
    def __init__(self, name, price, weight, sell, dump):
        self.name = name
        self.price = price
        self.weight = weight
        self.sell = sell
        self.dump = dump
    def item1(self):
        print(f"[{self.name}] is good pen [{self.weight} is pen weight]")
    
    def dump1(self):
        print(f"[{self.name}] is discarded. Your wealth subtract [{self.price}] ")
        

class Black_pen(Item):  # equipment
    def __init__(self, name, price, weight, sell, dump):
        super().__init__(name, price, weight, sell, dump)
        self.put_on_effect = ("knowledge + 3")
        self.put_on = ("OK. I got it.")

black_pen = Black_pen("smart Black-pen", 1200, "15g", "ok", "ok")
black_pen.item1()
black_pen.dump1()

    
    
class Hot6(Item):   # supply
    def __init__(self, name, price, weight, sell, dump):
        super().__init__(name, price, weight, sell, dump)
        self.use_effect = ("movement + 3")
        self.put_on = ("Let's Drink")
     
    def item2(self):
        print(f"[{self.name}] is energy drinks. [{self.use_effect}] makes you more healthy.")
       
hot6 = Hot6("Energy Drinks", 450, "30g", "OK", "OK")
hot6.item2()
    

