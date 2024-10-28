import random


def kb_sirala(dizi):
    sayim = 0
    ii = 0
    while sayim < len(dizi) - 1:
        if dizi[ii] > dizi[ii + 1]:
            dizi[ii], dizi[ii + 1] = dizi[ii + 1], dizi[ii]
            sayim = 0
        else:
            sayim += 1
        ii += 1
        if ii == len(dizi) - 1:
            ii = 0
    return dizi


dizi1 = []
dizi2 = []
u = 20
uzunluk1 = u
uzunluk2 = u
"""rastgele elamanlı diziler oluşturulur"""
for i in range(uzunluk1):
    dizi1.append(random.randrange(1, 50))
    dizi2.append(random.randrange(1, 50))
print("dizilerin ilk halleri:")
print(dizi1)
print(dizi2)
print()
i = 0
j = 0
kosul = 0
"""kosul değişkeni ortak eleman bulunduğunda 1 olur eğer ortak eleman
    bulunamadıysa sıfır kalır"""

"""dizilerin uzunlukları değişiceği için while döngüsüyle
    dizilerde gezinip ortak elemanlar kontrolü yapılır"""
while i < uzunluk1:
    while j < uzunluk2:
        """ikinci dizinin son elemanına gelindiğinde ilk dizideki
        silinmesi gereken ortak elemanlar silinmesi için ilk dizide
        döngü başlar"""
        if j == uzunluk2 - 1 and kosul == 1:
            k = i + 1
            while k < uzunluk1:
                if dizi1[i] == dizi1[k]:
                    dizi1.pop(k)
                    uzunluk1 -= 1
                else:
                    k += 1
            """son elemana gelindiğinde 46. satırdaki else'e giremediği için
             eğer ki ortak sayı ikinci dizinin son elemanında da var ise diye 
             aynı koşul tekrar kurulur"""
            if dizi1[i] == dizi2[j]:
                dizi2.pop(j)
                uzunluk2 -= 1
                j += 1
            else:
                j += 1
            dizi1.pop(i)
            uzunluk1 -= 1
            """eğer son elemanda değilse ortak elemanlar bulunup silinir ve uzunluk bir eksilir"""
        else:
            if dizi1[i] == dizi2[j]:
                kosul = 1
                dizi2.pop(j)
                uzunluk2 -= 1
            else:
                j += 1
    j = 0
    """eğer ortak eleman bulunmadıysa i bir arttırılarak ilk dizide gezilmeye devam edilir"""
    if kosul != 1:
        i += 1
    else:
        kosul = 0
print("ortak elemanların çıkarılmış halleri:")
print(dizi1)
print(dizi2)
print()
"""sadece append fonksiyonu kullanılabilir dendiği için append kullandım"""
for i in range(uzunluk1):
    dizi2.append(dizi1[i])
print("dizilerin birleştirilmiş hali")
print(dizi2)
print(kb_sirala(dizi2))
