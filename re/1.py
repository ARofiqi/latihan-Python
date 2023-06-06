import re

pattern = r"spam"

# if re.match(pattern, "spamspamspam"):
#     print("Match")
# else:
#     print("No match")

# re.match -> mencocokan kata pertama yang dengan pettern
# if re.match(pattern, "spameggspamsausagespam"):
#     print("Match")
# else:
#     print("No match")

# re.search -> mencari apakah pattern ada pettern ada di kalimat atau tidak
# if re.search(pattern, "egspam"):
#     print("Match")
# else:
#     print("No match")

# re.findall -> mengumpulkan semua kata pettern yang ada dikalimat dan disatukan dalam list
# print(re.findall(pattern, "eggspamsausagespamspamspamspamspamspamspamspam"))

kata = "eggspamsausage"
match = re.search(pattern, kata)
if match:
    print(match.group())
    # print(match.groupdict())
    # print(match.groups())
    print(match.start())
    print(match.end())
    print(match.span())
    print(kata[int(match.start()):int(match.end())])

