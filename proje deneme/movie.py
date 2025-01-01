import json


class MovieTVShow:
    def __init__(self, title, genre, state, year, IMBD, note=""):
        """
        Initialize a Movie/TVShow instance.

        :param title: Name of the movie or TV show (string).
        :param genre: Type - either "film" or "dizi" (string).
        :param state: Watch status - "izlendi", "izlenecek", "bekleniyor" (string).
        :param IMBD: Rating out of 5 (integer).
        :param note: Optional notes (string).
        """
        self.title = title
        self.genre = genre
        self.state = state
        self.year = year
        self.IMBD = IMBD
        self.note = note

    def update_status(self, new_status):
        """
        Update the watch status.
        :param new_status: The new watch status (string).
        """
        self.state = new_status

    def add_notes(self, new_note):
        """
        Add notes or update existing notes.
        :param new_note: The note to be added or updated (string).
        """
        self.note = new_note

    def to_dict(self):
        """
        Sınıfı bir sözlüğe dönüştürür (JSON yazılabilir format).

        :return: Sözlük formatında film/dizi bilgileri
        """
        return {
            "title": self.title,
            "genre": self.genre,
            "state": self.state,
            "year": self.year,
            "IMBD": self.IMBD,
            "note": self.note
        }


class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Hata: {self.file_path} bulunamadı. Yeni bir dosya oluşturulacak.")
            return []
        except json.JSONDecodeError:
            print(f"Hata: {self.file_path} geçerli bir JSON formatında değil. Dosya sıfırlanacak.")
            return []

    def write_file(self, data):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Veriler başarıyla {self.file_path} dosyasına kaydedildi.")
        except Exception as e:
            print(f"Dosyaya yazma hatası: {str(e)}")

    def add_movie(self, movie):
        data = self.read_file()
        data.append(movie.to_dict())
        self.write_file(data)

    def remove_movie(self, title):
        data = self.read_file()
        data = [item for item in data if item['title'] != title]
        self.write_file(data)

    def update_movie(self, title, updated_movie):
        data = self.read_file()
        for i, item in enumerate(data):
            if item['title'] == title:
                data[i] = updated_movie.to_dict()
                break
        self.write_file(data)

    def get_movies(self):
        """
        JSON dosyasındaki tüm filmleri getirir.
        """
        return self.read_file()

    def find_movie(self, title):
        """
        Başlığa göre bir film arar.
        :param title: Filmin başlığı
        :return: Film verileri veya None
        """
        data = self.read_file()
        for item in data:
            if item['title'].lower() == title.lower():
                return item
        return None
