import re

# 1. percobaan 1
# pattern = r"[aeiou]"

# if re.search(pattern, "grey"):
#     print("Match 1")

# if re.search(pattern, "qwertyuiop"):
#     print("Match 2")

# if re.search(pattern, "rhythm myths"):
#     print("Match 3")


# 2. percobaan 2
# pattern = r"[A-Z][A-Z][0-9]"

# if re.search(pattern, "LS8"):
#     print("Match 1")

# if re.search(pattern, "E3"):
#     print("Match 2")

# if re.search(pattern, "1ab"):
#     print("Match 3")

# 3. percobaan 3
# pattern = r"[^A-Z]"

# if re.search(pattern, "this is all quiet"):
#     print("Match 1")

# if re.search(pattern, "AbCdEfG123"):
#     print("Match 2")

# if re.search(pattern, "THISISALLSHOUTING"):
#     print("Match 3")

# 4. percobaan 4
# pattern = r"egg(spam)*"

# if re.match(pattern, "egg"):
#     print("Match 1")

# if re.match(pattern, "eggspamspamegg"):
#     print("Match 2")

# if re.match(pattern, "spam"):
#     print("Match 3")

# 5. percobaan 5
# pattern = r"g+"

# if re.match(pattern, "g"):
#     print("Match 1")

# if re.match(pattern, "ggggggggggggg"):
#     print("Match 2")

# if re.match(pattern, "abc"):
#     print("Match 3")

# 6. Percobaan 6
# pattern = r"ice(-)?cream"

# if re.match(pattern, "ice-cream"):
#     print("Match 1")

# if re.match(pattern, "icecream"):
#     print("Match 2")

# if re.match(pattern, "sausages"):
#     print("Match 3")

# if re.match(pattern, "ice--ice"):
#     print("Match 4")

# 7. Percobaan 7
# pattern = r"9{1,3}$"

# if re.match(pattern, "9"):
#     print("Match 1")

# if re.match(pattern, "999"):
#     print("Match 2")

# if re.match(pattern, "9999"):
#     print("Match 3")

# 8. Percobaan 8
# pattern = r"a(bc)(d(e)f)(g(h)i)j"

# match = re.match(pattern, "abcdefghijklmnop")
# if match:
#     print(match.group())
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.groups())

# 9. Percobaan 9
# pattern = r"(?P<first>abc)(?:def)(ghi)"

# match = re.match(pattern, "abcdefghi")
# if match:
#     print(match.group("first"))
#     print(match.groups())

# 10. Percobaan 10
# pattern = r"gr(a|e)y"

# match = re.match(pattern, "gray")
# if match:
#     print ("Match 1")

# match = re.match(pattern, "grey")
# if match:
#     print ("Match 2")    

# match = re.match(pattern, "griy")
# if match:
#      print ("Match 3")

# 11. Percobaan 11
# pattern = r"(.+) \1"

# match = re.match(pattern, "word word ")
# if match:
#     print ("Match 1")

# match = re.match(pattern, "?! ?!")
# if match:
#     print ("Match 2")    

# match = re.match(pattern, "abc def")
# if match:
#     print ("Match 3")

# 12. Percobaan 12
# pattern = r"(\D+\d)"

# match = re.match(pattern, "Hi 999!")
# if match:
#     print("Match 1")

# match = re.match(pattern, "1, 23, 456!")
# if match:
#     print("Match 2")

# match = re.match(pattern, " ! $?")
# if match:
#     print("Match 3")

# 13. Percobaan 13
# pattern = r"\b(cat)\b"

# match = re.search(pattern, "The cat sat!")
# if match:
#     print ("Match 1")

# match = re.search(pattern, "We s>cat<tered?")
# if match:
#     print ("Match 2")

# match = re.search(pattern, "We scattered.")
# if match:
#     print ("Match 3")