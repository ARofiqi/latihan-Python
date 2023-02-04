# Diamond Problem

class A:
    def show(self):
        print("Ini Method A")


class B(A):
    def show(self):
        print("Ini Method B")


class C(A):
    def show(self):
        print("Ini Method C")


class D(B, C):
    pass


objek = D()

objek.show()
# help(objek)