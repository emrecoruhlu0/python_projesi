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