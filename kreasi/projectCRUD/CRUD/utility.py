import random
import string

def random_string(panjang):
    hasil=''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasil

