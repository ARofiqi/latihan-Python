mhs = {
       "Rofiqi":{
           "nim":"20220040159",
           "jurusan":"Teknik Informatika",
           "kelas":"TI22E"
           },
       "Dodi":{
           "nim":"20220040158",
           "jurusan":"Teknik sipil",
           "kelas":"TI22E"
           },
       "Rudi":{
           "nim":"20223040358",
           "jurusan":"Hukum",
           "kelas":"TI22E"
           },
       }

for index,nama in enumerate(mhs):
    no = index+1
    nim = mhs[nama]['nim']
    jrs = mhs[nama]['jurusan']
    kls = mhs[nama]['kelas']
    print(f"{no} {nama.ljust(10)} {nim.ljust(15)} {jrs.ljust(20)} {kls.ljust(6)}")