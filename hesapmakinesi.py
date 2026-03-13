sayi1= float(input("bir sayiyi gir"))
sayi2= float(input("ikinci sayiyi gir:"))

islem = input("yapmak istedigin islem (+,-,*,/):")
if islem == "+":
 print ("sonuc:", sayi1 + sayi2)
elif islem == "-":
 print ("sonuc:", sayi1 - sayi2)
elif islem == "*":
 print ("sonuc:", sayi1 * sayi2)
elif islem == "/":
 print ("sonuc:", sayi1 / sayi2)
else: 
 print("gecersiz islem")