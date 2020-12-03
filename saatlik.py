# -*- coding: utf-8 -*-
import urllib 
import urllib3
import requests
import json 
from datetime import datetime
import locale
import time
import pymysql as MySQLdb

locale.setlocale(locale.LC_ALL, "")
moment = datetime.now()

db = MySQLdb.connect("ip", "user", "password", "db_name")
cursor = db.cursor()

keys = ["API_KEY"]

key_numara = 0
API_KEY = keys[key_numara] 



def veri_cek(saat,metadata,kanalid):

    print ("https://www.youtube.com/watch?v="+metadata)  
    try:
        SpecificVideoID = metadata
        SpecificVideoUrl = 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id='+SpecificVideoID+'&key='+API_KEY
        response = urllib.request.urlopen(SpecificVideoUrl) 
    except Exception as e: 
        return 1

    videos = json.load(response) 


    for video in videos['items']: 
        if video['kind'] == 'youtube#video':
            try:
                ad = video["snippet"]["title"]
                ad = ad.replace("'","-")
                goruntulenme= video['statistics']['viewCount']
                begenme = video["statistics"]["likeCount"]
                begenmeme=video["statistics"]["dislikeCount"]
                yorum = video['statistics']['commentCount']

                a = video['snippet']['publishedAt']
                b = a.split("T")
                c = b[1].split(".")
                yuklenme_tarihi = b[0]
                yuklenme_saati = c[0]
                tarih = moment.strftime("%Y-%m-%d")
                    
                query = f"insert into saatlik(videoID,kanal_ID,goruntulenme,begenme,begenmeme,yorum,tarih,saat) values ('{metadata}','{kanalid}',{goruntulenme},{begenme},{begenmeme},{yorum},'{yuklenme_tarihi}','{saat}')"
                cursor.execute(query)
                db.commit()
            except Exception as a:
                return 1
                continue
                print(a)
                


      




query="SELECT DISTINCT videoID,kanal_ID FROM yenivideo where durum= 'Beklemede' "
cursor.execute(query)
sayac = 0
for j in cursor.fetchall():
        if sayac==24:
            break
        elif j[0]!=None:
            query =f"UPDATE yenivideo SET durum ='Veri Çekiliyor' where videoID= '{j[0]}' "
            cursor.execute(query)
            db.commit()
            saat = moment.strftime("%H:%M")
            while True:
                moment = datetime.now()
                saat = moment.strftime("%H:%M")
                veri_alma = moment.strftime("%M")
                if veri_alma == "00":
                    a= veri_cek(saat,j[0],j[1])
                    sayac = sayac + 1
                    if a==1:
                        key_numara += 1
                        if key_numara == 8:
                            key_numara = 0
                        API_KEY = keys[key_numara]
                        veri_cek(saat,j[0],j[1])
                print(veri_alma)
                if(sayac==24):
                    query =f"UPDATE yenivideo SET durum ='Veri çekildi' where videoID= '{j[0]}' "
                    cursor.execute(query)
                    db.commit()
                    break
                time.sleep(60)


cursor.close()
db.commit()
db.close()
