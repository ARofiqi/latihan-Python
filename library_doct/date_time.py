import datetime

data_waktu = datetime.datetime.now()
# data_waktu = datetime.datetime.utcnow()
# data_waktu = datetime.datetime.utcfromtimestamp(5.5)

print(f"""
date time now = {data_waktu}
Tahun = {data_waktu.year}
Bulan = {data_waktu.month}
Hari  = {data_waktu.day}

tzone  = {data_waktu.tzname()}
Fold  = {data_waktu.fold}

Hari   = {data_waktu.strftime('%d')}
Bulan  = {data_waktu.strftime('%m')}
Tahun  = {data_waktu.strftime('%Y')}

Jam    = {data_waktu.strftime('%H')}
Menit  = {data_waktu.strftime('%M')}
Detik  = {data_waktu.strftime('%S')}

jam   = {data_waktu.hour}
menit = {data_waktu.minute}
detik = {data_waktu.second}
""")

jam   = data_waktu.hour
menit = data_waktu.minute
detik = data_waktu.second

print(jam,':',menit,':',detik,'WIB')