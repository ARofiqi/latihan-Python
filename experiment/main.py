file = open(r"C:\dev\Latihan Python\experiment\myfile.txt","w")
file_w = file.write("Selamat Datang")
file.close()


# file_r = file.readlines(1)[0]
file = open(r"C:\dev\Latihan Python\experiment\myfile.txt","r")
file_r = file.read()

print("Re-reading\n")

print(file_r)
# print(f"Jumlah Kata adalah {len(file_r)}")

print("\nFinished")

file.close()