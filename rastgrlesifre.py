import random
import string 
uzunluk = int(input("sifre uzunlugu:"))
karakterler = string.ascii_letters + string.digits
sifre = ""

for i in range(uzunluk):
    sifre += random.choice(karakterler)
    
    print("olusturulan sifre:", sifre)