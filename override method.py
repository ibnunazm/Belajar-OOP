class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("showInfo di class Hero")
        print("{}\n\thealth: {}\n".format(self.name, self.health))

class Hero_mage(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
    
    def showInfo(self):
        print("showInfo di subclass Hero_mage")
        print("{} \n\ttipe: magic \n\thealth: {}\n".format(self.name, self.health))
    

class Hero_fighter(Hero):
    def __init__(self, name):
        super().__init__(name, 200)

eudora = Hero_mage("eudora")
balmond = Hero_fighter("balmond")

eudora.showInfo()
balmond.showInfo()