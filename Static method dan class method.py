class Hero:

    #private class variable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    #method ini hanya berlaku untuk objek
    def getjumlah(self):
        return Hero.__jumlah

    #method ini tidak berlaku untuk objek tapi berlaku untuk class
    def getjumlah1():
        return Hero.__jumlah

    #method static nempel pada objek dan class
    @staticmethod
    def getjumlah2():
        return Hero.__jumlah

    @classmethod
    def getjumlah3(cls):
        return cls.__jumlah

sniper = Hero("sniper")
print(sniper.getjumlah())
print(Hero.getjumlah1())
rikimari = Hero("rikimaru")
print(Hero.getjumlah2())
print(sniper.getjumlah2())
print(Hero.getjumlah3())
print(sniper.getjumlah3())