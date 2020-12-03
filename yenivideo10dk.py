
import traceback
import urllib3
import xmltodict
import pymysql as MySQLdb
from datetime import datetime, timedelta


db = MySQLdb.connect("ip", "user", "password", "db_name")




def getxml(channel_id):
    url = "https://www.youtube.com/feeds/videos.xml?channel_id=" + channel_id

    http = urllib3.PoolManager()

    response = http.request('GET', url)
    try:
        data = xmltodict.parse(response.data)
        video = data["feed"]["entry"]
        videoID = video[0]['yt:videoId']
        videoad = video[0]['title']

        tarih = video[0]['published']
        gun= tarih.split("T")
        saat = gun[1].split("+")
        saat2 = saat[0].split(":")
        saat3 = int(saat2[0]) + 3
        saat = f"{saat3}:{saat2[1]}"
        print(saat)
        print(videoID)
        print(gun[0])
        print(saat[0])
        query = f"insert into videoliste(videoID,kanal_ID) values ('{videoID}','{channel_id}')"
        cursor.execute(query)
        durum="Beklemede"
        print(videoad)
        query = f"insert into yenivideo(videoID,kanal_ID,tarih,saat,durum,ad) values ('{videoID}','{channel_id}','{gun[0]}','{saat}','{durum}','{videoad}')"
        cursor.execute(query)
        query = f"insert into saatlik(videoID,kanal_ID,goruntulenme,begenme,begenmeme,yorum,tarih,saat) values ('{videoID}','{channel_id}',0,0,0,0,'{gun[0]}','{saat}')"
        cursor.execute(query)
        
    except Exception as e:
        print("Videolistede bulunuyor" )
        print(e)
        return 0



cursor = db.cursor()
query="SELECT * FROM kanal"
cursor.execute(query)
kanallar = cursor.fetchall()
kanal_list=[]
for i in kanallar:
    kanal_list.append(i[0])

for i in kanal_list:
    getxml(i)



cursor.close()
db.commit()
db.close()
