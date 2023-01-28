import datetime

data_waktu = datetime.datetime.now()
# data_waktu = datetime.datetime.utcnow()
# data_waktu = datetime.datetime.utcfromtimestamp(5.5)

print(f"date time now = {data_waktu}")

print(f"Tahun = {data_waktu.year}")
print(f"Bulan = {data_waktu.month}")
print(f"Hari  = {data_waktu.day}")

print(f"tzone  = {data_waktu.tzname()}")
print(f"Fold  = {data_waktu.fold}")

print(f"Hari   = {data_waktu.strftime('%d')}")
print(f"Bulan  = {data_waktu.strftime('%m')}")
print(f"Tahun  = {data_waktu.strftime('%Y')}")

print(f"Jam    = {data_waktu.strftime('%H')}")
print(f"Menit  = {data_waktu.strftime('%M')}")
print(f"Detik  = {data_waktu.strftime('%S')}")

print(f"jam   = {data_waktu.hour}")
print(f"menit = {data_waktu.minute}")
print(f"detik = {data_waktu.second}")

jam   = data_waktu.hour
menit = data_waktu.minute
detik = data_waktu.second

print(f"{jam} : {menit} : {detik} WIB")