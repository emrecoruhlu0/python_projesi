import csv
import json


# CSV'den JSON'a dönüştürme fonksiyonu
def csv_to_json(csv_file_path, json_file_path):
    # CSV dosyasını aç ve oku
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)  # CSV'yi sözlük olarak oku

        # JSON için bir liste oluştur
        json_data = []
        for row in csv_reader:
            json_data.append(row)

    # JSON dosyasına yaz
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)


def add_boolean_key_to_json(json_file_path, output_file_path, new_key, new_value):
    if not isinstance(new_value, bool):
        raise ValueError("new_value sadece True veya False olabilir!")

    # JSON dosyasını oku
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Yeni anahtar ve boolean değeri ekleme
    def add_key(obj):
        if isinstance(obj, list):  # Eğer obje bir listeyse
            return [add_key(item) for item in obj]
        elif isinstance(obj, dict):  # Eğer obje bir sözlükse
            obj[new_key] = new_value  # Yeni anahtar ve değer ekleniyor
            return obj
        return obj  # Diğer türler olduğu gibi bırak

    # Anahtar ekleniyor
    updated_data = add_key(data)

    # Güncellenmiş JSON'u yeni dosyaya yaz
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(updated_data, json_file, indent=4, ensure_ascii=False)

    print(
        f"Yeni boolean anahtar '{new_key}' (Değer: {new_value}) JSON dosyasına eklendi ve sonuç '{output_file_path}' dosyasına kaydedildi.")


def rename_key_in_json(json_file_path, output_file_path, old_key, new_key):
    # JSON dosyasını oku
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Anahtar adını değiştirme
    def update_keys(obj):
        if isinstance(obj, list):  # Eğer obje bir listeyse
            return [update_keys(item) for item in obj]
        elif isinstance(obj, dict):  # Eğer obje bir sözlükse
            return {new_key if k == old_key else k: update_keys(v) for k, v in obj.items()}
        return obj  # Diğer türler olduğu gibi bırak

    # Anahtarlar güncelleniyor
    updated_data = update_keys(data)

    # Güncellenmiş JSON'u yeni dosyaya yaz
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(updated_data, json_file, indent=4, ensure_ascii=False)

    print(f"'{old_key}' anahtarı '{new_key}' olarak değiştirildi ve sonuç '{output_file_path}' dosyasına kaydedildi.")


def limit_values_in_key(json_file_path, output_file_path, target_key, max_values):
    # JSON dosyasını oku
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Değer uzunluğunu kısıtlama işlemi
    def limit_values(obj):
        if isinstance(obj, list):  # Eğer obje bir listeyse
            return [limit_values(item) for item in obj]
        elif isinstance(obj, dict):  # Eğer obje bir sözlükse
            if target_key in obj and isinstance(obj[target_key], list):  # Anahtarın bir liste değeri varsa
                obj[target_key] = obj[target_key][:max_values]  # Yalnızca ilk 'max_values' elemanını sakla
            return {k: limit_values(v) for k, v in obj.items()}
        return obj  # Diğer türler olduğu gibi bırak

    # Güncellenmiş veri
    updated_data = limit_values(data)

    # Güncellenmiş JSON'u yeni dosyaya yaz
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(updated_data, json_file, indent=4, ensure_ascii=False)

    print(
        f"'{target_key}' anahtarındaki değerler '{max_values}' eleman ile sınırlandırıldı ve '{output_file_path}' dosyasına kaydedildi.")


def fix_stars_or_remove(input_file, output_file):
    # JSON dosyasını yükle
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # İşlenebilir sözlükleri saklamak için yeni bir liste
    cleaned_data = []

    for item in data:
        if 'stars' in item:
            try:
                # stars değerini listeye çevir
                item['star'] = json.loads(item['stars'].replace("'", '"'))
                # İşlenebilirse listeye ekle
                cleaned_data.append(item)
            except json.JSONDecodeError:
                print(f"'{item['title']}' için stars alanı işlenemedi. Sözlük siliniyor.")
        else:
            # stars alanı yoksa da listeye eklemiyoruz
            print(f"'{item['title']}' için stars alanı bulunamadı. Sözlük siliniyor.")

    # Güncellenmiş veriyi yeni dosyaya yaz
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(cleaned_data, file, indent=4, ensure_ascii=False)


def convert_genre_to_list(input_file, output_file):
    # JSON dosyasını yükle
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # İşlenebilir sözlükleri saklamak için yeni bir liste
    updated_data = []

    for item in data:
        if 'genre' in item:
            # Virgülle ayrılmış stringi listeye çevir
            item['genre'] = [genre.strip() for genre in item['genre'].split(',')]
            updated_data.append(item)  # Güncellenmiş öğeyi listeye ekle

    # Güncellenmiş veriyi yeni dosyaya yaz
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(updated_data, file, indent=4, ensure_ascii=False)

    print(f"'genre' anahtarı listeye dönüştürüldü ve sonuç '{output_file}' dosyasına kaydedildi.")


def clean_stars_values(input_file, output_file):
    # JSON dosyasını yükle
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Hatalı değerleri içeren öğelerden stars anahtarını sil
    for item in data:
        if 'stars' in item:
            # stars anahtarındaki değeri kontrol et
            stars_value = item['stars']
            if isinstance(stars_value, str):  # Eğer stars bir string ise
                if stars_value.strip() == "|" or "Stars:" in stars_value:
                    print(f"'{item['title']}' için hatalı stars değeri bulundu. Siliniyor.")
                    del item['stars']  # stars anahtarını sil
            elif isinstance(stars_value, list):  # Eğer stars bir liste ise
                # Liste içindeki hatalı değerleri kontrol et
                item['stars'] = [star for star in stars_value if star.strip() != "|" and "Stars:" not in star]
                if not item['stars']:  # Eğer tüm elemanlar silindiyse anahtarı tamamen kaldır
                    print(f"'{item['title']}' için tüm stars değerleri hatalıydı. Siliniyor.")
                    del item['stars']

    # Güncellenmiş veriyi yeni dosyaya yaz
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Hatalı stars değerleri temizlendi ve sonuç '{output_file}' dosyasına kaydedildi.")


def add_keys_to_json(input_file, output_file, user_rating_default=0, note_default=""):
    # JSON dosyasını yükle
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Her öğeye yeni anahtarları ekle
    for item in data:
        item['userRating'] = user_rating_default  # Varsayılan değerle userRating ekle
        item['note'] = note_default  # Varsayılan değerle note ekle

    # Güncellenmiş veriyi yeni dosyaya yaz
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"'userRating' ve 'note' anahtarları eklendi ve sonuç '{output_file}' dosyasına kaydedildi.")


import shutil
import os


def backup_file(file_path):
    backup_path = file_path + ".backup"
    if os.path.exists(file_path):
        shutil.copy(file_path, backup_path)
        print(f"Yedekleme oluşturuldu: {backup_path}")


"""
# JSON dosyasını yedekle
file_path = 'kucuk.json'
backup_file(file_path)
"""
"""
# Kullanım
csv_file_path = 'IMBD.csv'  # Çevrilecek CSV dosyası
json_file_path = 'detail_movies.json'  # Kaydedilecek JSON dosyası

csv_to_json(csv_file_path, json_file_path)
print(f"'{csv_file_path}' dosyası başarıyla '{json_file_path}' dosyasına dönüştürüldü.")
"""
"""
# JSON'dan 'crew' bilgilerini silme
json_file_path = 'guncel.json'  # Girdi JSON dosyası
output_file_path = 'guncel2.json'  # Çıktı JSON dosyası

with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 'crew' anahtarını her öğeden sil
if isinstance(data, list):  # Eğer veri bir liste ise
    for item in data:
        if 'duration' in item:  # 'votes' anahtarı varsa
            del item['duration']
elif isinstance(data, dict):  # Eğer veri bir sözlük ise
    if 'votes' in data:
        del data['votes']

# Güncellenmiş veriyi yeni JSON dosyasına yaz
with open(output_file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"'crew' anahtarı '{json_file_path}' dosyasından silindi ve '{output_file_path}' dosyasına kaydedildi.")
"""

"""
# JSON dosyasındaki bir anahtar adını değiştiren fonksiyon
# Kullanım

json_file_path = 'movies.json'  # Girdi JSON dosyası
output_file_path = 'yeni_movies.json'  # Güncellenmiş JSON dosyası
old_key = 'rating'  # Değiştirilecek eski anahtar adı
new_key = 'IMBDrating'  # Yeni anahtar adı

rename_key_in_json(json_file_path, output_file_path, old_key, new_key)
"""


"""
# JSON dosyasına yeni bir boolean anahtar ekleme fonksiyonu
# Kullanım

json_file_path = 'yeni_movies.json'  # Girdi JSON dosyası
output_file_path = 'guncel.json'  # Güncellenmiş JSON dosyası
new_key = 'durum'  # Eklenecek yeni anahtar adı
new_value = True  # Yeni anahtarın değeri (True ya da False)

add_boolean_key_to_json(json_file_path, output_file_path, new_key, new_value)
"""

"""
# Belirli bir anahtarın değer sayısını sınırlayan fonksiyon
# Kullanım

json_file_path = 'movies_cleaned.json'  # Girdi JSON dosyası
output_file_path = 'movies.json'  # Güncellenmiş JSON dosyası
target_key = 'stars'  # Değeri sınırlandırılacak anahtar
max_values = 3  # Maksimum değer sayısı

limit_values_in_key(json_file_path, output_file_path, target_key, max_values)
"""


"""

# Kullanım
input_file = 'movies.json'  # Orijinal dosya
output_file = 'movies_cleaned.json'  # Düzeltilecek dosya

fix_stars_or_remove(input_file, output_file)
print(f"Düzeltmeler {output_file} dosyasına kaydedildi!")
"""


"""

# Kullanım
input_file = 'movies.json'  # Orijinal dosya
output_file = 'movies_genre_converted.json'  # Dönüştürülen dosya

convert_genre_to_list(input_file, output_file)
"""

"""

# Kullanım
input_file = 'movies_genre_converted.json'  # Orijinal dosya
output_file = 'movies.json'  # Temizlenmiş dosya

clean_stars_values(input_file, output_file)
"""

"""
# Kullanım
input_file = 'movies.json'  # Orijinal dosya
output_file = 'son_movie.json'  # Güncellenmiş dosya
add_keys_to_json(input_file, output_file, user_rating_default=0, note_default="")
"""
yol = 'son_movie.json'
backup_file(yol)