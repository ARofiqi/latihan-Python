# Looping list dan enumarate
numbers = [3,4,6,2,4,6,7]

# for loop
print("============ for loop ============")
for num in numbers:
    print(f"number = {num}")

# for loop dan range
p = len(numbers)
print("\n============ for loop dan range ============")
for n in range(p):
    print(f"number = {numbers[n]}")

# while
i = 0
print("\n============ while ============")
while i < p:
    print(f"number = {numbers[i]}")
    i += 1

# while referse
p = len(numbers)
print("\n============ while referse ============")
while p > 0:
    p -= 1
    print(f"number = {numbers[p]}")

# list comprehension
print("\n============ list comprehension ============")
data = ["ucup",1,2,3,"otong"]
[print(f"data = {i}") for i in data]
[print(f"kuadrat dari {i} = {i**2}") for i in numbers]

# enumerate
print("\n============ enumerate ============")
data = ["ucup",1,2,3,"otong"]
for index,data in enumerate(data):
    print(f"index = {index}, data = {data}")    
