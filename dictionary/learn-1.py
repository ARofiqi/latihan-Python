# pengenalan dictionary
data_dict = {
    "Rofiqi":"Informatika",
    "Andika":"Sipil",
    "abdullah":"matematika"
}

# mengambil data dict
data_1 = data_dict["Rofiqi"]

# mengambil data dengan perulangan for
# [print(f"{i} = {data_dict[i]}") for i in data_dict]

# Operasi Dictionary

print(f"""
data_dict = {data_dict}
panjang dict = {len(data_dict)}
mengecek Rofiqi di data_dict = {"Rofiqi" in data_dict}
mengecek Rizal di data_dict = {"Rizal" in data_dict}
mengakses value Rofiqi = {data_dict.get("Rofiqi")}
mengakses value Rizal = {data_dict.get("Rizal")}
mengakses value Rizal = {data_dict.get("Rizal","Tidak Ada")}

mengupdate data informatika jadi biologi 
di Rofiqi = {data_dict.update({"Rofiqi":"Biologi"})}

jika data yang diupdate tidak ada di dict maka otomatis akan ditambahkan 
mengupdate Rizal : Humas ke data_dict = {data_dict.update({"Rizal":"Humas"})}

data_dict = {data_dict}

menghapus Rofiqi di data_dict
""")

del data_dict["Rofiqi"]
print(data_dict)