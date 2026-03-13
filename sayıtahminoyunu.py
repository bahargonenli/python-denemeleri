import random
sayi = random.randint(1,100)
while True:
     tahmin = int (input("1 ile 100 arasinda bir sayi takmin et:"))
     if tahmin== sayi:
          print("tebrikler dogru tahmin ettin!")
          break
     elif tahmin < sayi:
          print("daha büyük bir sayi söyle")
     else:
          print("daha küçük bir sayi söyle") 