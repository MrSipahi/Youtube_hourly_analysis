import pymysql as MySQLdb
import os
from time import sleep

db = MySQLdb.connect("ip", "user", "password", "db_name")
cursor = db.cursor()

query = "SELECT * FROM yenivideo where durum= 'Veri çekildi' "
cursor.execute(query)
sayac = 0
for j in cursor.fetchall():
    os.system("python3 /home/yonetici/verianaliz/saatlik_analiz.py")
    sleep(30)
