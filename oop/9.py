class A:
    def method_A(self):
        print("Ini method A")


class B:
    def method_B(self):
        print("Ini method B")


# Multiple Inheritence
class C(A, B):
    pass


objek = C()

objek.method_A()
objek.method_B()
