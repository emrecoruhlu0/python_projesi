print("metin giriniz:")

metin = input("metin: ").lower()
"""girilen metnin harflerinin hepsini küçük harf yapar"""

harfler = {}
"""harfler diye sözlük oluşturulur"""

for i in metin:
    if i not in harfler:
        harfler[i] = 1
        """eğer metnin harfi sözlükte yoksa başlangıç değeri 1 yapılır"""
    else:
        harfler[i] += 1
        """eğer metnin harfi sözlükte varsa değeri bir arttırılır"""
print(harfler)
