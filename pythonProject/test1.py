class fridge:
    def __init__(self,amount):
        self.amount = amount
    def deleteFood(self, count):
        self.amount -= count
    def PlusFood(self, count):
        self.amount += count
class  human:
    def __init__(self,name, hungry, mood, money, health):
        self.name = name
        self.hungry = hungry
        self.mood = mood
        self.money = money
        self.health = health

    def work(self):
        self.mood -= 20
        self.money += 100
        self.hungry -= 25
    def buyFood(self, Count):
        self.money -= 50
        fridge.PlusFood(Count)
    def eat(self):
        if(fridge1.amount == 0):
            self.buyFood(2)
        else:
            self.hungry += 20
            fridge.deleteFood(1)


fridge1 = fridge(0)
human1 = human("anatoliy", 100, 100, 0, 100)
day = 0
while day <= 100:
    day += 1
    print("Health == ",human1.health," Hungry == ",human1.hungry," Mood == ", human1.mood," Money == ",human1.money)
    if(human1.health <= 0):
        print("Вы умерли")
        break
    if(human1.hungry <= 0 or human1.mood <= 0):
        human1.health -= 10

    elif(human1.health <= 25):
        pass
    if(human1.hungry > 0):
        human1.work()
    

