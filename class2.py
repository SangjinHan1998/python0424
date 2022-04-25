class Monster:
    def say(self):
        print("I'm Monster")
        
goblin = Monster()
goblin.say()

# In python, Data type is also CLass
a = 10
b = "문자열객체"
c = True

print(type(a))
print(type(b))
print(type(c))

print(b.__dir__())