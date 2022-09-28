Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
from time import*
flag=True
while(flag):
    Temp=random.randint(0,50)
    Humi=random.randint(10,50)
    if Temp>45 and Humi<30:
        print("Ambient temperature=",Temp,"Ambient Humidity=",Humi)
        print("-----------------Alarm ON------------")
        flag=False
    else:
        print("Ambient Temperature=",Temp,"Ambient Humidity",Humi)
        sleep(0.5);
