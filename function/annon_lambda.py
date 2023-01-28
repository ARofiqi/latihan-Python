# lambda function
# cara menulis function pendek menggunakan lambda
# output = lambda argument: expretion
kuadrat = lambda angka: angka**2
print(kuadrat(29))


# annonymous function
# currying <- Haskell Curry

def pangkat(n):
    return lambda num: num**n

pangkat2 = pangkat(2)
print(pangkat2(3))

pangkat_bebas = pangkat(2)(7)
print(pangkat_bebas)