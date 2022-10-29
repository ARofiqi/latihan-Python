# contoh dictionary
mhs = {
       "Rofiqi":{
           "nim":20220040159,
           "jurusan":"Teknik Informatika",
           "kelas":"TI22E"
           },
       "Dodi":{
           "nim":20220040158,
           "jurusan":"Teknik Informatika",
           "kelas":"TI22E"
           },
       }



i = 0
for index,nama in enumerate(mhs):
    print(f"{index+1} {nama} {mhs[nama]['nim']} {mhs[nama]['jurusan']} {mhs[nama]['kelas']}")