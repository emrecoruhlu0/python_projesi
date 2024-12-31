"""import json
from movie import MovieTVShow

import json


def read_file(json_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            readed_json = json.load(f)
        return readed_json
    except FileNotFoundError:
        print(f"Hata: {json_file_path} bulunamadı.")
        return None
    except json.JSONDecodeError:
        print(f"Hata: {json_file_path} geçerli bir JSON formatında değil.")
        return None


def add_movie(json_file_path,new_movie):
    data = read_file(json_file_path)

    # Yeni film ekle
    data.append(new_movie)

    # Güncellenmiş JSON'u dosyaya yaz
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Yeni film başarıyla eklendi ve '{json_file_path}' dosyasına kaydedildi.")


file_path = 'kucuk.json'

new_movie = MovieTVShow(
    title="Inception",
    genre="film",
    state="izlenecek",
    year=2010,
    IMBD=9,
    note="Bilim kurgu harikası bir film."
)

add_movie(file_path, new_movie)


"""

import json
from movie import MovieTVShow


def read_file(json_file_path):
    """
    Bir JSON dosyasını okuyarak Python veri yapısına (dict veya list) dönüştürür.

    :param json_file_path: JSON dosyasının yolu (string)
    :return: Okunmuş JSON verisi (dict veya list) veya boş liste
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            readed_json = json.load(f)
        return readed_json
    except FileNotFoundError:
        print(f"Hata: {json_file_path} bulunamadı. Yeni bir dosya oluşturulacak.")
        return []  # Boş bir liste döndür
    except json.JSONDecodeError:
        print(f"Hata: {json_file_path} geçerli bir JSON formatında değil. Dosya sıfırlanacak.")
        emin = int(input("emin misin"))
        if emin == 1:
            return []  # Boş bir liste döndür
        else:
            print("hata var")


def add_movie(json_file_path, new_movie):
    """
    Mevcut bir JSON dosyasına yeni bir film ekler ve eski verileri korur.

    :param json_file_path: JSON dosyasının yolu (string)
    :param new_movie: Eklenecek film (MovieTVShow sınıfı örneği)
    """
    # Mevcut verileri oku
    data = read_file(json_file_path)

    # Yeni filmi ekle (sözlük formatında)
    data.append(new_movie.to_dict())

    # Güncellenmiş JSON'u aynı dosyaya yaz
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Yeni film başarıyla eklendi ve '{json_file_path}' dosyasına kaydedildi.")


file_path = 'movies.json'

new_movie = MovieTVShow(
    title="Inception",
    genre="film",
    state="izlenecek",
    year=2010,
    IMBD=9,
    note="Bilim kurgu harikası bir film."
)

# Yeni filmi dosyaya ekle
add_movie(file_path, new_movie)
