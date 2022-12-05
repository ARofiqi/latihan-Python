import matematika
print(f"""
Hasil Tambah : {matematika.tambah(2,3,4,5,3,67,7)}
Hasil kali : {matematika.kali(2,3,4,5,3,67,7)}
Hasil Tambah : {matematika.pangkat(2)(5)}
""")

from matematika import tambah, kali, pangkat
print(f"""
Hasil Tambah : {tambah(2,3,4,5,3,67,7)}
Hasil kali : {kali(2,3,4,5,3,67,7)}
Hasil Tambah : {pangkat(2)(5)}
""")

import matematika as math
print(f"""
Hasil Tambah : {math.tambah(2,3,4,5,3,67,7)}
Hasil kali : {math.kali(2,3,4,5,3,67,7)}
Hasil Tambah : {math.pangkat(2)(5)}
""")
