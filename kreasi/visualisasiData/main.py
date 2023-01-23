import matplotlib.pyplot as plt

buku_bacaan = {
    "Januari":2,
    "Febuari":3,
    "Maret":4,
    "April":8,
    "Mei":2,
    "Juni":5,
    "Juli":4,
    "Agustus":5,
    "September":5,
    "Oktober":9,
    "November":3,
    "Desember":2
}

# bulan = [i for i in buku_bacaan]
# jml_buku = [buku_bacaan[i] for i in buku_bacaan]
# plt.title("Jumlah Buku Yang dibaca")
# plt.bar(x=bulan,height=jml_buku)


lol = [f"{i}" for i in range(20)]
y = [2*i+5 for i in range(20)]
plt.bar(x=lol,height=y,width=.5,)
plt.show()
