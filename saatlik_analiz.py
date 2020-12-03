import pandas as pd
import matplotlib.pyplot as plt
import pymysql as MySQLdb
from datetime import datetime, timedelta
import locale
from PIL import Image
from instabot import Bot
import os
import time




db = MySQLdb.connect("ip", "user", "password", "db_name")
cursor = db.cursor()
query="SELECT * FROM saatlik "


df = pd.read_sql(query, con=db)

videoID_list = df["videoID"].unique() 


yenivideo_list=[]
for j in videoID_list:
    query=f"SELECT * FROM yenivideo where videoID='{j}' AND durum= 'Veri çekildi' "
    cursor.execute(query)
    for j in cursor.fetchall():
        yenivideo_list.append(j[0])

bot = Bot()
bot.login(username="username",password="password")

for i in yenivideo_list:
    fotolar=[]
    query=f"SELECT yenivideo.ad,saatlik.tarih,videoliste.kanal_ID,kanal.tag,kanal.user_id FROM videoliste,saatlik,kanal,yenivideo where videoliste.videoID= '{i}' AND saatlik.videoID= '{i}' AND videoliste.kanal_ID=kanal.ID and yenivideo.videoID='{i}'"
    cursor.execute(query)
    video = cursor.fetchall()
    videoad= video[0][0]
    videoaduzun = videoad
    tarih = video[0][1]
    tarih = tarih.strftime("%Y/%m/%d")
    videoad = videoad[:55]
    kanalID= video[0][2]
    videoID=i
    tag = video[0][3]
    user_id=video[0][4]


    saat_list=[]
    print(i)
    query=f"SELECT * FROM saatlik where videoID='{i}'"
    cursor.execute(query)
    video = cursor.fetchall()
    df = pd.read_sql(query, con=db)

    saat_list = df["saat"]

    goruntulenme= df["goruntulenme"]
    begenme= df["begenme"]
    begenmeme= df["begenmeme"]
    yorum= df["yorum"]


    yenisaat=[]
    saat_izlenme=[]
    saat_begenme=[]
    saat_begenmeme=[]
    saat_yorum=[]
    saat_saat=[]
    for x in saat_list:
        kelime =str(x)
        saat_duzenle = kelime.split(" ")
        saat_duzenle = saat_duzenle[2]
        saat_duzenle = saat_duzenle.split(":")
        saat = f"{saat_duzenle[0]}:{saat_duzenle[1]}"
        print(saat)
        yenisaat.append(saat) 

    for j in range(1,len(yorum)):
            
        a2 = goruntulenme[j]
        b2 = goruntulenme[j-1]
        izlenme= a2-b2
        saat_izlenme.append(izlenme)


        a2 = begenme[j]
        b2 = begenme[j-1]
        izlenme= a2-b2
        saat_begenme.append(izlenme)

        a2 = begenmeme[j]
        b2 = begenmeme[j-1]
        izlenme= a2-b2
        saat_begenmeme.append(izlenme)
            

        a2 = yorum[j]
        b2 = yorum[j-1]
        izlenme= a2-b2
        saat_yorum.append(izlenme)

        a2 = yenisaat[j-1]
        b2 = yenisaat[j]
        saat_saat.append(f"{a2}\n{b2}")
    

    print(len(saat_begenme))
    yarisi = int(len(saat_begenme)/2)
    sayac = 0
    def analiz_yap(tabload,liste,renkno,ad,sayac):  
        for sayi in range(0,2):

            if sayi == 0:
                plotdata = pd.DataFrame({tabload:liste[:yarisi],},index=saat_saat[:yarisi])
            else:
                plotdata = pd.DataFrame({tabload:liste[yarisi:len(saat_begenme)],},index=saat_saat[yarisi:len(saat_begenme)])
            
            plt.style.use("dark_background")
            for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
                plt.rcParams[param] = '0.9'  # very light grey
            for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
                plt.rcParams[param] = '#212946'  # bluish dark grey
            colors = [
                '#01BABE',  # teal/cyan
                '#80FF80', # matrix green
                '#8B8B8B',  # pink
                '#FFFF80', # yellow
                     
            ]
            plotdata.plot(kind="bar",fontsize=20, color=colors[renkno])

            figure = plt.gcf()  # get current figure
            figure.set_size_inches(18, 9) 
            plt.legend(fontsize=20)
            plt.xticks(rotation=0, horizontalalignment="center",fontsize=20)
            plt.title(f"{videoad}\n{tarih}\nVideonun Saatlik {ad} Verileri ",fontsize=25)
           # plt.xlabel(ad,fontsize=20)
            #plt.ylabel("Saat",fontsize=20)
            plt.savefig(f'saatlik.jpg',bbox_inches='tight') 
            #plt.show()

            def watermark_photo(input_image_path,
                                output_image_path,
                                watermark_image_path,
                                position):
                base_image = Image.open(input_image_path)
                watermark = Image.open(watermark_image_path)
                # add watermark to your image
                base_image.paste(watermark, position)
                base_image.save(output_image_path)
            img = '/home/yonetici/verianaliz/arkaplan.jpg'
            watermark_photo(img, f'{sayac}{sayi}.jpg',
                                    'saatlik.jpg', position=(85,50))

            fotolar.append(f'{sayac}{sayi}.jpg')

            plt.close()

            #db.commit()

    analiz_yap("goruntulenme",saat_izlenme,0,"Görüntülenme",sayac)
    sayac += 1
    analiz_yap("begenme",saat_begenme,1,"Begenme",sayac)
    sayac += 1
    analiz_yap("begenmeme",saat_begenmeme,2,"Begenmeme",sayac)
    sayac += 1
    analiz_yap("Yorum",saat_yorum,3,"Yorum",sayac)
    print(fotolar)

    users_to_tag = []
    x = 0.5
    y = 0.1
    print(tag)
    if len(user_id.split(","))!=1:
        user = user_id.split(",")
        for i2 in user:
            print(i2)
            s = {'user_id': i2, 'x': x, 'y': y}
            users_to_tag.append(s)
            x += 0.1
            y += 0.1
    else:
        s = {'user_id': user_id, 'x': x, 'y': y}
        users_to_tag.append(s)  

    try:
        bot.upload_album(fotolar,user_tags = users_to_tag,caption=f"\n{videoaduzun} \nVideonun Saatlik İstatistik Verileri \n{tag}\n\n\n#youtube #youtubetürkiye #enesbatur #basakkarahan #delimine #reynmen #orkunışıtmak #twitchturkiye #wtcnn #hazretiyasuo #hzyasuo #evonmoss #twitch #kafalar #alibicim #mesutcantomay #babala #oguzhanugur #magazin #youtubemagazin") 
        os.remove("00.jpg.REMOVE_ME")
        os.remove("01.jpg.REMOVE_ME")
        os.remove("10.jpg.REMOVE_ME")
        os.remove("11.jpg.REMOVE_ME")
        os.remove("20.jpg.REMOVE_ME")
        os.remove("21.jpg.REMOVE_ME")
        os.remove("30.jpg.REMOVE_ME")
        os.remove("31.jpg.REMOVE_ME")
    except Exception as e:
        print(e)

    query =f"UPDATE yenivideo SET Durum ='Paylasildi' where videoID= '{i}' "
    print(query)
    cursor.execute(query)
    db.commit()

db.commit()
cursor.close()
db.close()
