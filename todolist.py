gorevler = []
while True:
    print("\n1- görev ekle")
    print("2-görevleri göster")
    print("3- cikis")

    secim = input("secim yap:")

    if secim == "1":
        gorev = input("yeni görev gir:")
        gorevler.append(gorev)
        print("gorev eklendi")

    elif secim == "2":
        print("yapilacaklar:")
        for i, gorev in enumerate(gorevler,1):
            print(i, "-",gorev)
    elif secim == "3":
     print("progrem kapatiliyor..")
    break
else:
 print("gecersiz secim")