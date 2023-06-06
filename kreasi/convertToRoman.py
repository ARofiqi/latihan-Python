ROMAN = {
    1: "I", 
    5: "V", #4=IV
    10: "X", #9=IX
    50: "L", #40=XL
    100: "C", #90=XC
    500: "D", #400=CD
    1000: "M", #900=CM
    5000: "_V", #4000=M[_V]
}

def to_roman(num):
    result = []
    number_list = list(map(lambda x : int(x), str(num)))
    for index,item in enumerate(number_list):
        result.append(int(item)*(10**(len(number_list)-index-1)))
    return result

myNum = to_roman(123)
print(myNum)


# NUM_ROMAN = list(reversed(sorted(ROMAN.keys())))

# def to_roman(num):
#     result = ""
#     if (num >= 1 and num <= 8):
#         if (num <= 4):
#             result+=ROMAN[1]
#             if (num == 4 or num == 1):
#                 result+=ROMAN[5]
#             else:
#                 result+=ROMAN[1]*(num-1)
#         else:
#             result+=ROMAN[5]
#             if (num > 5):
#                 result+=ROMAN[1]*(num-5)
#     elif (num >= 9 and num <= 49):
#         pass
#     return result



