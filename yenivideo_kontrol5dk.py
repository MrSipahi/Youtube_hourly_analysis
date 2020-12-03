import threading
import pymysql as MySQLdb
from os import system
from time import sleep



db = MySQLdb.connect("ip", "user", "password", "db_name")
cursor = db.cursor()

query = "SELECT * FROM yenivideo where durum= 'Beklemede' "
cursor.execute(query)
sayac = 0


for j in cursor.fetchall():
    system('python3 /home/yonetici/verianaliz/saatlik.py')
    sleep(30)

