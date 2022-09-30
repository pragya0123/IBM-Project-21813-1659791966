Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... temperature=random.randint(20,100)
... humidity=random.randint(30,50)#normal humidity range:30 to 50 %
... print("The Temperature is", temperature)
... print("The humidity is",humidity)
... if(temp>30):#normal room temp=20 to 30 (degree celsius)
...  print("HIGH TEMPERATURE IS DETECTED!")
... else:
