import copy


def artik_yil_mi(yil):
    """yılın artık yıl olup olmadığını 1 veya olucak şekilde döndürür"""
    return yil % 4 == 0 and (yil % 100 != 0 or yil % 400 == 0)


def gun_sayisi_hesapla(t1, t2):
    aylar_gunler1 = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    aylar_gunler2 = copy.deepcopy(aylar_gunler1)
    """iki tane aylar sözlüğü barındırcağım için 
        ve ikisini de kodda yer kaplamasın diye
        deepcopy kullandım. bunun normal eşitlemeden
        farkı ilk sözlükte yapılan değişikliklerin
        diğer sözlüğe aktarılmaması"""

    gun = 0
    yil1, ay1, gun1 = map(int, t1.split("-"))
    yil2, ay2, gun2 = map(int, t2.split("-"))
    """YYYY-MM-DD formatında yazılan tarih bilgisinin
        int değerleri elde etme"""
    if yil1 > yil2:
        return -1
    if artik_yil_mi(yil1):
        aylar_gunler1[2] += 1
    if artik_yil_mi(yil2):
        aylar_gunler2[2] += 1
    """yil1 ve yil2'de artık gün olup olmadığı kontrol edilir
        bu bilgiye göre sözlükteki şubat ayına bir gün eklenir"""

    if yil2 - yil1 > 1:
        """eğer yıllar arasında tam yıllar varsa onlar da artık
            olup olmamalarına göre direkt günleri eklenir"""
        for i in range(yil1, yil2):
            if artik_yil_mi(i):
                gun += 366
            else:
                gun += 365

    elif yil2 - yil1 > 0:
        """eğer yıllar farklıysa"""

        for i in range(ay1 + 1, 13):
            gun += aylar_gunler1[i]
        """ilk tarihin başlangıç ayından yılın 
            sonuna kadarki ayların günleri eklenir"""

        for i in range(1, ay2):
            gun += aylar_gunler2[i]
        """ikinci tarihin yılının başından o tarihe kadarki 
            tam ayların günleri eklenir"""

        for i in range(gun1, aylar_gunler1[ay1] + 1):
            gun += 1
            """ilk tarihin başlangıcından aynın
                sonuna kadarki günler eklenir
                (*)"""

        for i in range(1, gun2):
            gun += 1
            """ikinci tarihin aynın başından
                o tarihin gününe kadarki günler eklenir
                (**)"""

        for i in range(ay1 + 1, ay2):
            gun += aylar_gunler1[i]
            """tarihlerin arasındaki tam ayların günleri eklenir
                (***)"""

    else:
        """eğer tarihler aynı yıl içersindeyse"""
        if ay1 != ay2:
            """farklı aylarsa"""
            for i in range(gun1, aylar_gunler1[ay1] + 1):
                gun += 1
                """bunun (*) aynısı"""
            for i in range(1, gun2):
                gun += 1
                """bunun (**) aynısı"""
            for i in range(ay1 + 1, ay2):
                gun += aylar_gunler1[i]
                """bunun (***) aynısı"""
        else:
            """aynı aylarsa direkt günler çıkarılır"""
            gun = gun2 - gun1
    return gun


def hafta_sayisi_hesapla(t1, t2):
    gun = gun_sayisi_hesapla(t1, t2)
    hafta = gun // 7
    """gün sayısının bölümünü tam sayıya çevirerek yediye bölünür"""
    return hafta


print("tarihler YYYY-MM-DD formatında olmalıdır")

tarih1 = input("baslangic tarihi gir:")
tarih2 = input("bitis tarihi gir:")

gunler = gun_sayisi_hesapla(tarih1, tarih2)
if gunler == -1:
    print("yılları doğru sırayla giriniz.")
haftalar = hafta_sayisi_hesapla(tarih1, tarih2)

print("iki tarih arasındaki gun sayisi: ", gunler)
print("iki tarih arasındaki hafta sayisi: ", haftalar)
