'''
*args pada python

*args --> mengambil semua argument yang ada dikotak argument fungsi dan dijadikan satu dalam tuple

*args tidak mengambil argument yang sudah diambil oleh variabel lain
'''

def rata_rata(*args:int) -> int:
    r = 0
    for i in args:
        r += i
    return r/len(args)

print(rata_rata(2,3,4,5,4,6,7,3))
# out = 4.25

def say(nama,*args):
    print(nama, args)

say("Rofiqi", "rijal", "andika", "salwa", "ucup")
# out = Rofiqi ('rijal', 'andika', 'salwa', 'ucup')