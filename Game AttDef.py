class Hero:

    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

    def serang(self, musuh):
        print(self.name + " menyerang " + musuh.name) 
        musuh.diserang(self, self.attack)

    def diserang(self, musuh, attack_lawan):
        print(self.name + " diserang " + musuh.name)
        attack_diterima = 2*attack_lawan/self.armor
        print("serangan terasa: " + str(attack_diterima))
        self.health -= attack_diterima
        print("darah " +self.name+ " tersisa " + str(self.health))


lesley = Hero("lesley", 100, 10, 5)
hayabusa = Hero("hayabusa", 100, 20, 2)

lesley.serang(hayabusa)
print("\n")
hayabusa.serang(lesley)

print(lesley.health)