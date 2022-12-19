class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        #self.info = "name {} : \n\thealth: {}".format(self.__name, self.__health)
    
    @property
    def info(self):
        return "name {} : \n\thealth : {} \n\tarmor : {}".format(self.name, self.__health, self.__armor)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print("armor sudah didelete")
        self.__armor = None

sniper = Hero("sniper", 100, 10)

print("merubah info")
print(sniper.info)
sniper.name = "lesley"
print(sniper.info)

print("\n\ngetter dan setter untuk armor")
print(sniper.armor)
sniper.armor = 20
print(sniper.armor)
print(sniper.info)

del sniper.armor
print(sniper.__dict__)
