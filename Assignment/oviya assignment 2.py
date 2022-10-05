Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
... import random
... i=0
... while(i<=2000):
...     i=i+1
...     time.sleep(5):
...     temp=random.randint(0,30)
...     humid=random.randint(1,100)
...     if temp<=15:
...         print(temp,"the temperature is low")
...     elif temp<=25:
...         print(temp,"the temperature is normal")
...     else:
...         print(temp,"the temperature is high")
...     if humid<=15:
...         print(humid,"the humidity is low")
...     elif humid<=80:
...         print(humid,"the humidity is normal")
...     else:
