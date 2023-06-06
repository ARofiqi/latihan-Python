# 1. Percobaan Ternari Oeprator
# status = 1
# msg = "Loguot" if status == 1 else "Login"
# print(msg)

# 2. Else Pada for atau while
# for i in range(10):
#     if i == 999:
#         break
# else:
#     print("Unbroken 1")

# for i in range(10):
#     if i == 5:
#         break
# else:
#     print("Unbroken 2")

# 3. else pada try except
# try:
#     print(1)
# except ZeroDivisionError:
#     print(2)
# else:
#     print(3)

# try:
#     print(1/0)
# except ZeroDivisionError:
#     print(4)
# else:
#     print(5)
for i in range(10):
  try: 
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)
