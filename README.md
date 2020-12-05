# What is it ?

  
This program obtains hourly statistical data of newly uploaded videos of youtube channels in the database, analyzes, visualizes and shares them on the instagram page.


![enter image description here](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/photo/post.PNG?raw=true)


# How does it work
It checks the new videos of all channels every 10 minutes, if there is a new video, it adds it to both the 'videoliste' table and the 'yenivideo' table.

 - [yenivideo10dk.py
](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/yenivideo10dk.py)


It checks if a new video is added to the new video table every 5 minutes. If new video is available, it runs the saatlik.py program.

 - [yenivideo_kontrol5dk.py](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/yenivideo_kontrol5dk.py)

It pulls the statistics data of the newly posted video for 24 hours per hour and adds this data to the 'saatlik' table.

 - [saatlik.py](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/saatlik.py)

![enter image description here](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/photo/veri_cekiliyor.PNG?raw=true)

![enter image description here](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/photo/veri_istatistik.PNG?raw=true)

Runs the saatlik_analiz.py file if 24-hour data of a newly posted video is captured.

 - [saatlik_analiz_kontrol10dk.py](https://github.com/MrSipahi/Youtube_hourly_analysis/blob/main/saatlik_analiz_kontrol10dk.py)

It analyzes the statistical data of the 24-hour video according to the hours, visualizes this data and shares it on the Instagram page.

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

 

