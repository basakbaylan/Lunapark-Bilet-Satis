def bilgiler():
    boy = int(input("Boyunuzu santimetre cinsinden giriniz \n"))
    if boy >= 120:
        yas = int(input("Yaşınızı giriniz\n"))
        if yas < 12:
            print("Bilet Ücretiniz 15 TL")
        elif yas <= 18:
            print("Bilet Ücretiniz 25 TL")
        elif yas >= 19:
            print("Bilet Ücretiniz 35 TL")
    else:
        print("Boy sınırın altında kaldınız maalesef bilet alamazsınız.")


while True:
    print("<<<<<BEYBİ LUNAPARK>>>>>\nLütfen Seçim Yapın")
    print(" 1-Oyuncaklar\n 2-Bilet Satın Alma \n 3-Kurallar")
    secim=int(input("Lütfen Seçim Yapınız\n Seçim:"))

    if secim==1:
        print("<<<Beybi Lunapark oyuncaklar listesi>>>\n*Dönme Dolap\n*Çarpışan Arabalar\n*Hız Treni")

    elif secim==2:
        print("<<<Bilet Satın Alma Sayfasına Hoşgeldiniz>>>")
        biletal=int(input("Bilet almak istediğiniz oyuncağı seçin.\n1-Dönme Dolap\n2-Çarpışan Araba\n"
                          "3-Hız Treni\nSeçim:"))
        if biletal==1:
            bilgiler()

        elif biletal==2:
            bilgiler()
        elif biletal==3:
            bilgiler()
        else:
            print("HATALI TUŞLAMA YAPTINIZ LÜTFEN YENİDEN DENEYİM")
            continue

    elif secim==3:
        print("<<<KURALLAR>>>\n-Değerli eşyaların sorumluluğu sahibine aittir."
              " Ücretli kilitli emanet dolapları mevcuttur.\n"
              "-Satılan bir bilet başkasına devredilemez ve tekrar satılamaz.\n"
              "-Evcil hayvan getirmek yasaktır.")



    else:
        print("HATALI TUŞLAMA YAPTINIZ LÜTFEN YENİDEN DENEYİN")
        continue







