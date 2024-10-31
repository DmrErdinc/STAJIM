
##Modüller
import math

print(math.sqrt(16))     
print(math.factorial(5)) 
print(math.pi)           

import random

print(random.randint(1, 10))  
print(random.random())       

import datetime

bugun = datetime.date.today()
print("Bugünün tarihi:", bugun)

simdi = datetime.datetime.now()
print("Şu anki zaman:", simdi)

import os

print(os.getcwd())  # Geçerli çalışma dizinini döner
os.mkdir("yeni_klasor")  # "yeni_klasor" adında yeni bir klasör oluşturur

from math import sqrt, pi

print(sqrt(25))  
print(pi)        