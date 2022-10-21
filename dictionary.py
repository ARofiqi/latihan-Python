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
print("no  nama \t\t nim \t\t\t\t prodi \t\t\t kelas")
for n in mhs:
    i+=1
    print("{}. {} \t ({}) \t {} \t {}".format(i,n,mhs[n]["nim"],mhs[n]["jurusan"],mhs[n]["kelas"]))
    
