ABJAD = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
         "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ABJAD_REVERSE = ABJAD.copy()
ABJAD_REVERSE.reverse()


def filter(word):
    if word == " ":
        return " "
    else:
        return ABJAD_REVERSE[ABJAD.index(word)]


def get_pass(text):
    row_sandi = list(map(filter, text))
    result = ''.join(row_sandi)
    return result


massage = input("Masukan Pesannya : ")
massage.upper()
sandi = get_pass(massage)
print(f"sandi saya = {sandi}")
