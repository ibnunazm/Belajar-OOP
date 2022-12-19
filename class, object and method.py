class Hero:
    #class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1
        print("Membuat hero dengan nama", inputName)

        #variable instance private
        self.__private = "private"

        #variable instance protected
        self.protected = "protected"

    def siapa(self):
        print("print namaku adalah", self.name)

    def healthUp(self, up):
        self.health += up

    def getHealth(self):
        return self.health

hero1 = Hero("Betrix", 800, 200, 50)
print("Hero saat ini ada : ", Hero.jumlah_hero)
hero2 = Hero("Hylos", 3500, 30, 150)
print("Hero saat ini ada : ", Hero.jumlah_hero)
hero3 = Hero("Lesley", 900, 70, 40)
print("Hero saat ini ada : ", Hero.jumlah_hero)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

hero1.siapa()
hero1.healthUp(50)
print(hero1.__dict__)
print(hero1.getHealth())