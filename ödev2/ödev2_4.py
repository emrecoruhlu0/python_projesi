import random

sayilar = []
ardisiklar_uzun = []
ardisiklar_temp = []
uzunluk = 100
indeks = 0

#rastgele dizi oluşturulur
for i in range(uzunluk):
    sayilar.append(random.randrange(1,10))

#sayıların indeksleriyle beraber görünebilmesi için görselleştirme
for i in range(len(sayilar)):
    print(f"{i:>5}", end="")
print()
for i in sayilar:
    print(f"{i:>5}", end="")

for i in range(uzunluk - 1):
    #eğer ardışık sayılar varsa ve ardışık sayıların listesi ilk kez oluşturulmaya başlanmışsa ilk iki ardışık ekler
    if sayilar[i+1] == sayilar[i] + 1:
        if len(ardisiklar_temp) == 0:
            ardisiklar_temp.append(sayilar[i])
            ardisiklar_temp.append(sayilar[i + 1])
            indeks = i
            #sonrasında ardışıklığın nerden başladığını görmek için indeks değişkeni
        else:
            ardisiklar_temp.append(sayilar[i + 1])
    else:
        #daha uzun veya eşit uzunlukta ardışık sayılar dizisi bulunursa ardisiklar_uzuna sayılar aktarılır
        if len(ardisiklar_temp) >= len(ardisiklar_uzun):
            ardisiklar_uzun = ardisiklar_temp
            baslangic = indeks
            ardisiklar_temp = []
        else:
            #eğer uzun veya eşit uzunlukta dizi bulunmazsa geçici dizi sıfırlanır
            ardisiklar_temp = []
print(f"\nardışık alt dizi: {ardisiklar_uzun}")
print(f"alt dizinin başladığı index: {baslangic}")