# string method
txt = "hello, and welcome to my world."
x = txt.capitalize() # Hello, and welcome to my world.

txt = "Hello, and welcome to my world."
x = txt.casefold() # hello, and welcome to my world.

txt = "banana"
x = txt.center(20) #       banana       #

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple") # 2

txt = "My name is Ståle"
x = txt.encode() # b'My name is St\xc3\xa5le'

txt = "Hello, welcome to my world."
x = txt.endswith(".") # True

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2) # H e l l o

txt = "Hello, welcome to my world."
x = txt.find("welcome") # 7

txt = "Hello, welcome to my world."
x = txt.index("welcome") # 7

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple) # John#Peter#Vicky

txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
# print(txt.translate(mytable)) # Hello Pam!

txt = "I like bananas"
x = txt.replace("bananas", "apples") # I like apples

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite") # of all fruits banana is my favorite

print(x)