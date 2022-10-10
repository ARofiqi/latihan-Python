nama = ["Rofiqi",]
jrs = ["TI"]
ipk = [4.0]

def add_mhs(new_nama,new_jrs,new_ipk):
    nama.append(new_nama)
    jrs.append(new_jrs)
    ipk.append(new_ipk)

def add_mhs_1():
    nama.append(input("Nama :"))
    jrs.append(input("Jurusan :"))
    ipk.append(input("IPK :"))

def tampilkan_tabel():
    print("\n","="*10,"Tabel Mahasiswa","="*10)
    print("no nama jurusan ipk")
    for i in range(len(nama)):
        print(i+1,".",nama[i],jrs[i],ipk[i])

def tool_tambah():
    edit = input("Tambah Mahasiswa baru (y/n):")
    while(edit=='y'):
        if edit=='y':
            add_mhs_1()
            tampilkan_tabel()
            edit = input("Tambah Lagi(y/n):")
        else:
            break

def tool_delete():
    no = int(input("Hapus baris Ke :"))
    no-=1
    del nama[no]
    del jrs[no]
    del ipk[no]
    tampilkan_tabel()

tampilkan_tabel()
