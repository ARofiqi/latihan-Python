# magic method

class Mangga:

    # magic method
    def __init__(self, nama, jumlah) -> None:
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self) -> str:
        return f"Debug : Mangga {self.nama} dengan jumlah {self.jumlah}"

    def __str__(self) -> str:
        return f"Mangga {self.nama} dengan jumlah {self.jumlah}"
    
    def __add__(self,objek):
        return self.jumlah + objek.jumlah
    
    @property
    def __dict__(self):
        return "Objek ini mempunyai nama dan jumlah"


belanja1 = Mangga("Arumanis", 10)
belanja2 = Mangga("Arumanis", 20)
print(repr(belanja1))
print(belanja1 + belanja2)
print(belanja1.__dict__)
