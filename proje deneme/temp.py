import json
import tkinter as tk
from tkinter import messagebox, ttk
from movie import MovieTVShow, FileManager

class FilmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Film ve Dizi Yönetim Uygulaması")
        self.root.geometry("1000x700")

        # File managers for movies and series
        self.movies_manager = FileManager("filtered_films.json")
        self.series_manager = FileManager("filtered_series.json")

        self.current_genre = None
        self.selected_item = None
        self.active_category = 'movies'

        self.style_setup()
        self.create_main_page()

    def style_setup(self):
        self.root.configure(bg="#2C3E50")
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", padding=10, relief="flat", background="#3498DB", foreground="white", font=("Helvetica", 12))
        style.configure("TLabel", background="#2C3E50", foreground="white", font=("Helvetica", 12))

    def create_main_page(self):
        self.clear_window()

        # Grid yapılandırması
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(1, weight=1)

        # Üst çerçeve
        top_frame = tk.Frame(self.root, bg="#34495E")
        top_frame.grid(row=0, column=0, columnspan=3, sticky="ew")

        ttk.Button(top_frame, text="Filmler", command=lambda: self.switch_category('movies')).grid(row=0, column=0, padx=20, pady=10)
        ttk.Button(top_frame, text="Diziler", command=lambda: self.switch_category('series')).grid(row=0, column=1, padx=20, pady=10)

        self.info_label = ttk.Label(top_frame, text=f"Toplam Filmler: {len(self.movies_manager.get_movies())}")
        self.info_label.grid(row=0, column=2, padx=20, pady=10)

        # Sol çerçeve
        self.left_frame = tk.Frame(self.root, bg="#34495E")
        self.left_frame.grid(row=1, column=0, sticky="ns")

        # Sağ çerçeve
        self.right_frame = tk.Frame(self.root, width=200, bg="#1F3A52")
        self.right_frame.grid(row=1, column=2, sticky="ns")

        ttk.Button(self.right_frame, text="Detaylara Bak", command=self.show_details).grid(row=0, column=0, padx=10, pady=20)
        ttk.Button(self.right_frame, text="Yeni Film/Dizi Ekle", command=self.add_new_item).grid(row=1, column=0, padx=10, pady=20)

        # Orta çerçeve
        self.center_frame = tk.Frame(self.root, bg="#2C3E50")
        self.center_frame.grid(row=1, column=1, sticky="nsew")

        self.load_genres()

    def switch_category(self, category):
        self.active_category = category
        if category == 'movies':
            self.info_label.config(text=f"Toplam Filmler: {len(self.movies_manager.get_movies())}")
        else:
            self.info_label.config(text=f"Toplam Diziler: {len(self.series_manager.get_movies())}")
        self.load_genres()

    def load_genres(self):
        for widget in self.left_frame.winfo_children():
            widget.destroy()

        data = self.movies_manager.get_movies() if self.active_category == 'movies' else self.series_manager.get_movies()
        genres = sorted(set(genre for item in data for genre in item['genre']))

        row, col = 0, 0
        for genre in genres:
            btn = ttk.Button(self.left_frame, text=genre, command=lambda g=genre: self.show_genre(g))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            col += 1
            if col > 2:
                col = 0
                row += 1

    def show_genre(self, genre):
        self.current_genre = genre
        data = self.movies_manager.get_movies() if self.active_category == 'movies' else self.series_manager.get_movies()
        filtered_data = [item for item in data if genre in item['genre']]
        self.display_table(filtered_data)

    def display_table(self, data):
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        tree = ttk.Treeview(self.center_frame, columns=("title", "year", "IMBD", "state"), show='headings')
        tree.heading("title", text="Başlık")
        tree.heading("year", text="Yıl")
        tree.heading("IMBD", text="Puan")
        tree.heading("state", text="Durum")
        tree.pack(expand=True, fill='both')

        for item in data:
            tree.insert("", "end", values=(item['title'], item['year'], item['IMBD'], item['state']))

    def add_new_item(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Yeni Film/Dizi Ekle")
        add_window.geometry("400x300")

        tk.Label(add_window, text="Başlık:").pack(pady=5)
        title_entry = ttk.Entry(add_window)
        title_entry.pack(pady=5)

        tk.Label(add_window, text="Tür:").pack(pady=5)
        genre_entry = ttk.Entry(add_window)
        genre_entry.pack(pady=5)

        tk.Label(add_window, text="Durum:").pack(pady=5)
        state_entry = ttk.Entry(add_window)
        state_entry.pack(pady=5)

        tk.Label(add_window, text="Yıl:").pack(pady=5)
        year_entry = ttk.Entry(add_window)
        year_entry.pack(pady=5)

        tk.Label(add_window, text="IMDB Puanı:").pack(pady=5)
        rating_entry = ttk.Entry(add_window)
        rating_entry.pack(pady=5)

        def save_new_item():
            new_item = MovieTVShow(
                title=title_entry.get(),
                genre=genre_entry.get(),
                state=state_entry.get(),
                year=int(year_entry.get()),
                IMBD=int(rating_entry.get())
            )
            manager = self.movies_manager if self.active_category == 'movies' else self.series_manager
            manager.add_movie(new_item)
            add_window.destroy()
            self.load_genres()

        ttk.Button(add_window, text="Kaydet", command=save_new_item).pack(pady=20)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FilmApp(root)
    root.mainloop()
