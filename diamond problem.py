#diamond problem

class A:
    
    def show(self):
        print("ini adalah show A")

class B(A):
    pass
    # def show(self):
    #     print("ini adalah show B")

class C(A):
    pass
    # def show(self):
    #     print("ini adalah show C")

class D(B, C):
    pass

objek = D()
objek.show()
help(objek)