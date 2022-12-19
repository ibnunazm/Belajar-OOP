class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

class Hero_mage(Hero):
    pass

class Hero_fighter(Hero):
    pass

cyclops = Hero("cyclops", 100)
eudora = Hero_mage("eudora", 100)
balmond = Hero_fighter("balmond", 200)

print(cyclops.__dict__)
print(eudora.__dict__)
print(balmond.__dict__)

