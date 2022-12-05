teman_teman = {
    "Rofiqi":"Informatika",
    "Andika":"Sipil",
    "abdullah":"matematika"
}

print(f"{'Nama':<15} {'jurusan':20}")
print('='*35)
for nama,jrs in teman_teman.items():
    print(f"{nama:<15} {jrs:20}")