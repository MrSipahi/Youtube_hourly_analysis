# What is it ?

  
Bu program veritabanında bulunan youtube kanallarının yeni atılan videosunun saatlik istatistik verilerini elde eder, analiz eder, görselleştirir ve instagram sayfasında paylaşır.


![enter image description here](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/photo/post.PNG?raw=true)


# How does it work
Her 10 dakikada bir bütün kanalların yeni videolarını kontrol eder, eğer yeni atılan bir video varsa hem 'videoliste' tablosuna hem de 'yenivideo' tablosuna ekler.

 - [yenivideo10dk.py
](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/yenivideo10dk.py)


Her 5 dakikada bir yenivideo tablosuna yeni video eklenip eklenmediğini kontrol eder. Eğer yeni video varsa saatlik.py programını çalıştırır.

 - [yenivideo_kontrol5dk.py](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/yenivideo_kontrol5dk.py)

Yeni atılan videonun 24 saat boyunca istatistik verilerini saat başı çeker ve 'saatlik' tablosuna bu verileri ekler.

 - [saatlik.py](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/saatlik.py)

![enter image description here](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/photo/veri_cekiliyor.PNG?raw=true)

![enter image description here](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/photo/veri_istatistik.PNG?raw=true)

Yeni atılan bir videonun 24 saatlik verileri çekilmişse saatlik_analiz.py dosyasını çalıştırır.

 - [saatlik_analiz_kontrol10dk.py](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/saatlik_analiz_kontrol10dk.py)

24 saatlik verileri çekilmiş videonun istatistik verilerini saatlere göre böler, bu verileri görselleştirip instagram sayfasında paylaşır.

 - [saatlik_analiz.py](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/saatlik_analiz.py)

![enter image description here](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/photo/paylasildi.PNG?raw=true)

## Crontab List

    # m h  dom mon dow   command
    */10 * * * * python3 /home/yonetici/verianaliz/yenivideo10dk.py 
    */2 * * * * python3 /home/yonetici/verianaliz/yenivideo_kontrol5dk.py
    */5 * * * * python3 /home/yonetici/verianaliz/saatlik_analiz_kontrol10dk.py

#  Technologies

 - [Mysql](https://www.mysql.com/)
 - [Python](https://www.python.org/)
 - [Pandas](https://pypi.org/project/pandas/)
 - [Matplotlib](https://pypi.org/project/matplotlib/)
 - [Pillow](https://pypi.org/project/Pillow/)
 - [Instabot](https://pypi.org/project/instabot/)
 - [Cron-Job](https://cron-job.org/en/)

 

