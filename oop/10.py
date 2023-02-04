# Method Resolution Order

class A:
    def show(self):
        print("Ini Method A")


class B:
    def show(self):
        print("Ini Method B")


class C(A, B):
    pass


objek = C()

objek.show()
# help(objek)
"""
class C(A, B)
 |  Method resolution order:
 |      C
 |      A
 |      B
 |      builtins.object
 |  
 |  Methods inherited from A:
 |  
 |  show(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from A:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined) 
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
"""
