import json
import re

# Dosyayı okuma
with open('son_movie.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Filmleri ve dizileri ayırmak için listeler oluşturma
films = []
series = []
errors = []
film_titles = set()
series_titles = set()

# Düzenleme öncesi toplam sayılar
initial_film_count = 0
initial_series_count = 0

for item in data:
    try:
        # Eksik IMDb puanını kontrol et
        if not item['IMBDrating']:
            item['IMBDrating'] = 'N/A'

        # Yıl bilgisindeki parantezleri kaldır
        item['year'] = item['year'].replace('(', '').replace(')', '')

        # Yıl bilgisinde sadece sayılar veya aralık (örneğin '2015–2022') kontrolü yap
        if not re.match(r'^\d{4}(–\d{4})?$', item['year']):
            continue

        # Yıl bilgisini kontrol et (dizi veya film ayrımı)
        if '–' in item['year']:  # Dizi
            initial_series_count += 1
            # Dizi tekrarını kontrol et ve eklemeyi önle
            if item['title'] not in series_titles:
                series.append(item)
                series_titles.add(item['title'])
        else:  # Film
            initial_film_count += 1
            # Film tekrarını kontrol et ve eklemeyi önle
            if item['title'] not in film_titles:
                films.append(item)
                film_titles.add(item['title'])
    except KeyError as e:
        errors.append({'title': item.get('title', 'Unknown'), 'error': str(e)})

# Düzenleme sonrası toplam sayılar
final_film_count = len(films)
final_series_count = len(series)

# Sonuçları dosyalara kaydetme
with open('filtered_films.json', 'w', encoding='utf-8') as f:
    json.dump(films, f, ensure_ascii=False, indent=4)

with open('filtered_series.json', 'w', encoding='utf-8') as s:
    json.dump(series, s, ensure_ascii=False, indent=4)

with open('error_log.json', 'w', encoding='utf-8') as e:
    json.dump(errors, e, ensure_ascii=False, indent=4)

print("Veriler işlendi. Filmler, diziler ve hatalar ayrı dosyalara kaydedildi.")
print(f"Düzenleme öncesi - Filmler: {initial_film_count}, Diziler: {initial_series_count}")
print(f"Düzenleme sonrası - Filmler: {final_film_count}, Diziler: {final_series_count}")
