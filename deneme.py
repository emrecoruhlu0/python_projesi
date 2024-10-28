orijinal = {'isim': 'Ali', 'yas': 25, 'adres': {'sehir': 'İstanbul', 'ilce': 'Kadıköy'}}
kopya = orijinal.copy()

# Orijinal sözlükte değişiklik
orijinal['isim'] = 'Veli'
orijinal['adres']['sehir'] = 'Ankara'

print("Orijinal:", orijinal)
print("Kopya:", kopya)  # 'isim' değişmez ama 'adres' aynı referansa sahip olduğu için değişir
