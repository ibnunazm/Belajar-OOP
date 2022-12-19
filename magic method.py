class Mangga:

    #magic method
    def __init__(self, name, jumlah):
        self.name = name
        self.jumlah = jumlah

    def __repr__(self):
        return "Debug - Mangga {} : {}".format(self.name, self.jumlah)

    def __str__(self):
        return "Mangga {} : {}".format(self.name, self.jumlah)

    def __add__(self, objek):
        return self.jumlah + objek.jumlah

    @property
    def __dict__(self):
        return "objek ini mempunyai nama dan jumlah"

belanja1 = Mangga("arumanis", 10)
belanja2 = Mangga("Gedong", 15)
print(belanja1)
print(repr(belanja2))

print(belanja1 + belanja2)
print(belanja1.__dict__)
