import pymysql

db = pymysql.connect("Localhost","root","root","foodmarket")
cursor = db.cursor()
cursor.execute("SELECT VERTION()")
data = cursor.fetchone()
print("Versi Database : %s" %data)
db.close()