class Hero:

    #private class variable
    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.health = self.__healthMax

        Hero.__jumlah += 1
    
    @property
    def info(self):
        return "{} level {} exp {}/100 : \n\thealth = {}/{}\n\tattack = {}\n\tarmor  = {}".format(self.__name, self.__level, self.__exp, self.health, self.__healthMax, self.__attPower, self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if self.__exp >=100:
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level
        
    def attack(self, musuh):
        self.gainExp = 30

lesley = Hero("lesley", 100, 11, 10)
balmon = Hero("balmon", 150, 8, 12)
print(lesley.info)
lesley.attack(balmon)
lesley.attack(balmon)
lesley.attack(balmon)
lesley.attack(balmon)
print(lesley.info)
















