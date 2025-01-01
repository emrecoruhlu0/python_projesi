import json
import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk
import random



# JSON dosyasındaki kullanıcı bilgileri
USERS = {
    "a": "11",
    "user": "password"
}

class FilmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Film ve Dizi Yönetim Uygulaması")
        self.root.geometry("1000x700")
        self.movies = self.load_json_data("filtered_films.json")
        self.series = self.load_json_data("filtered_series.json")
        self.current_genre = None
        self.selected_item = None
        self.active_category = 'movies'
        self.style_setup()
        self.create_login_page()

    def style_setup(self):
        self.root.configure(bg="#2C3E50")
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", padding=10, relief="flat", background="#3498DB", foreground="white", font=("Helvetica", 12))
        style.configure("TLabel", background="#2C3E50", foreground="white", font=("Helvetica", 12))

    def create_login_page(self):
        self.clear_window()
        ttk.Label(self.root, text="Kullanıcı Adı:").pack(pady=5)
        self.username_entry = ttk.Entry(self.root)
        self.username_entry.pack(pady=5)

        ttk.Label(self.root, text="Şifre:").pack(pady=5)
        self.password_entry = ttk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        ttk.Button(self.root, text="Giriş", command=self.authenticate).pack(pady=20)

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in USERS and USERS[username] == password:
            messagebox.showinfo("Başarılı", "Giriş başarılı!")
            self.create_main_page()
        else:
            messagebox.showerror("Hata", "Hatalı kullanıcı adı veya şifre!")

    def add_review(self):
        if not self.selected_item:
            messagebox.showwarning("Uyarı", "Lütfen bir öğe seçin!")
            return

        data = self.movies if self.active_category == 'movies' else self.series
        item = next((x for x in data if x['title'] == self.selected_item), None)

        if item:
            review_window = tk.Toplevel(self.root)
            review_window.title("Yorum ve Puan Ekle")
            review_window.geometry("400x300")
            review_window.configure(bg="#2C3E50")

            # Önceki verileri al
            existing_rating = item.get('rating', '')
            existing_comment = item.get('comment', '')
            existing_watched = item.get('watched', False)

            # Puan
            tk.Label(review_window, text="Puan (1-10):", bg="#2C3E50", fg="white").pack(pady=5)
            rating_entry = ttk.Entry(review_window)
            rating_entry.insert(0, str(existing_rating))
            rating_entry.pack(pady=5)

            # Yorum
            tk.Label(review_window, text="Yorum:", bg="#2C3E50", fg="white").pack(pady=5)
            comment_entry = tk.Text(review_window, height=5, width=40)
            comment_entry.insert("1.0", existing_comment)
            comment_entry.pack(pady=5)

            # İzlenme durumu
            watched_var = tk.BooleanVar(value=existing_watched)
            check_button = tk.Checkbutton(review_window, text="İzlendi", variable=watched_var, bg="#2C3E50", fg="white")
            check_button.pack(pady=5)
            if existing_watched:
                check_button.select()

            def save_review():
                try:
                    rating = int(rating_entry.get())
                    if rating < 1 or rating > 10:
                        raise ValueError("Puan 1 ile 10 arasında olmalıdır.")
                except ValueError as e:
                    messagebox.showerror("Hata", str(e))
                    return

                item['rating'] = rating
                item['comment'] = comment_entry.get("1.0", tk.END).strip()
                item['watched'] = watched_var.get()
                self.save_json_data()
                review_window.destroy()
                messagebox.showinfo("Başarılı", "Veriler kaydedildi!")

            ttk.Button(review_window, text="Kaydet", command=save_review).pack(pady=20)

    def create_main_page(self):
        self.clear_window()

        # Üst kısımda kategori seçimi
        top_frame = tk.Frame(self.root, bg="#34495E")
        top_frame.pack(side="top", fill="x")
        ttk.Button(top_frame, text="Filmler", command=lambda: self.switch_category('movies')).pack(side="left", padx=20, pady=10)
        ttk.Button(top_frame, text="Diziler", command=lambda: self.switch_category('series')).pack(side="left", padx=20, pady=10)

        # Bilgi kutusu
        self.info_label = ttk.Label(top_frame, text=f"Toplam Filmler: {len(self.movies)}")
        self.info_label.pack(side="right", padx=20, pady=10)

        # Sol tarafta kategoriler
        self.left_frame = tk.Frame(self.root, width=200, bg="#34495E")
        self.left_frame.pack(side="left", fill="y")

        # Sağ tarafta butonlar
        self.right_frame = tk.Frame(self.root, width=200, bg="#1F3A52")
        self.right_frame.pack(side="right", fill="y")

        ttk.Button(self.right_frame, text="Detaylara Bak", command=self.show_details).pack(pady=20, padx=10)
        ttk.Button(self.right_frame, text="Yorum veya Puan Ekle", command=self.add_review).pack(pady=20, padx=10)
        ttk.Button(self.right_frame, text="Rastgele Öner", command=self.random_recommendation).pack(pady=20, padx=10)

        # Orta alanda tablo
        self.center_frame = tk.Frame(self.root, bg="#2C3E50")
        self.center_frame.pack(expand=True, fill="both")

        self.load_genres()

    def switch_category(self, category):
        self.active_category = category
        if category == 'movies':
            self.info_label.config(text=f"Toplam Filmler: {len(self.movies)}")
        else:
            self.info_label.config(text=f"Toplam Diziler: {len(self.series)}")
        self.load_genres()

    def random_recommendation(self):
        data = self.movies if self.active_category == 'movies' else self.series
        if not data:
            messagebox.showinfo("Bilgi", "Öneri bulunamadı.")
            return
        recommendation = random.choice(data)
        messagebox.showinfo(
            "Rastgele Öneri",
            f"Başlık: {recommendation['title']}\nYıl: {recommendation['year']}\nIMDb Puanı: {recommendation['IMBDrating']}"
        )

    def load_genres(self):
        for widget in self.left_frame.winfo_children():
            widget.destroy()

        data = self.filter_data(self.movies if self.active_category == 'movies' else self.series)
        genres = sorted(set(genre for item in data for genre in item['genre']))
        for genre in genres:
            ttk.Button(self.left_frame, text=genre, command=lambda g=genre: self.show_genre(g)).pack(pady=10, padx=5, fill="x")

        self.show_genre(genres[0])

    def filter_data(self, data):
        temiz_filmler = []
        for film in data:
            if 'TV Special' in film.get('title', ''):
                continue
            if not film.get('title'):
                continue
            if not film.get('genre') or not isinstance(film['genre'], list) or len(film['genre']) == 0 or any(
                    i == "" for i in film.get('genre')):
                continue
            if not film.get('stars') or not isinstance(film['stars'], list) or len(
                    film['stars']) == 0:
                continue
            if not film.get('IMBDrating') or not film['IMBDrating'].replace('.', '', 1).isdigit():
                continue
            temiz_filmler.append(film)
        return temiz_filmler

    def show_genre(self, genre):
        self.current_genre = genre
        data = self.filter_data(self.movies if self.active_category == 'movies' else self.series)
        filtered_data = [item for item in data if genre in item['genre']]
        self.display_table(filtered_data)

    def show_details(self):
        if not self.selected_item:
            messagebox.showwarning("Uyarı", "Lütfen bir öğe seçin!")
            return

        data = self.movies if self.active_category == 'movies' else self.series
        item = next((x for x in data if x['title'] == self.selected_item), None)

        if item:
            detail_window = tk.Toplevel(self.root)
            detail_window.title("Detaylar")
            detail_window.geometry("500x400")
            detail_window.configure(bg="#2C3E50")

            # Başlık
            tk.Label(detail_window, text=item['title'], font=("Helvetica", 16, "bold"), bg="#2C3E50", fg="white").pack(pady=10)

            # İçerik
            details = [
                ("Yıl", item.get('year', 'Bilinmiyor')),
                ("IMDb Puanı", item.get('IMBDrating', 'Bilinmiyor')),
                ("Tür", ', '.join(item.get('genre', []))),
                ("Oyuncular", ', '.join(item.get('stars', []))),
                ("Puan", item.get('rating', 'Henüz eklenmedi')),
                ("Yorum", item.get('comment', 'Henüz eklenmedi')),
                ("İzlenme Durumu", 'Evet' if item.get('watched', False) else 'Hayır')
            ]

            for label, value in details:
                frame = tk.Frame(detail_window, bg="#34495E")
                frame.pack(fill="x", padx=20, pady=5)
                tk.Label(frame, text=f"{label}: ", font=("Helvetica", 12, "bold"), bg="#34495E", fg="white").pack(side="left")
                tk.Label(frame, text=value, font=("Helvetica", 12), bg="#34495E", fg="white").pack(side="left")

    def save_json_data(self):
        with open("filtered_films.json", 'w', encoding='utf-8') as file:
            json.dump(self.movies, file, indent=4)
        with open("filtered_series.json", 'w', encoding='utf-8') as file:
            json.dump(self.series, file, indent=4)

    def display_table(self, data):
        for widget in self.center_frame.winfo_children():
            widget.destroy()

        self.tree = ttk.Treeview(self.center_frame)
        self.tree["columns"] = ["title", "year", "IMBDrating"]
        self.tree["show"] = "headings"

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

        for item in data:
            self.tree.insert("", "end", values=(item['title'], item['year'], item['IMBDrating']))

        self.tree.pack(expand=True, fill='both')
        self.tree.bind("<ButtonRelease-1>", self.select_item)

    def select_item(self, event):
        selected_item = self.tree.selection()[0]
        self.selected_item = self.tree.item(selected_item, 'values')[0]

    def load_json_data(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FilmApp(root)
    root.mainloop()
