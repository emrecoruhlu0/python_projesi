import json
import time
import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk
import random
import os

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

    def switch_category(self, category):
        self.active_category = category
        if category == 'movies':
            self.info_label.config(text=f"Toplam Filmler: {len(self.movies)}")
        else:
            self.info_label.config(text=f"Toplam Diziler: {len(self.series)}")
        self.load_genres()

    def style_setup(self):
        self.root.configure(bg="#2C3E50")
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", padding=10, relief="flat", background="#3498DB", foreground="white",
                        font=("Helvetica", 12))
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
                save_json_data()
                review_window.destroy()
                messagebox.showinfo("Başarılı", "Veriler kaydedildi!")

            ttk.Button(review_window, text="Kaydet", command=save_review).pack(pady=20)

    def create_main_page(self):
        self.clear_window()

        # Grid yapılandırması
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(1, weight=1)

        # Üst çerçeve
        top_frame = tk.Frame(self.root, bg="#34495E")
        top_frame.grid(row=0, column=0, columnspan=3, sticky="ew")

        ttk.Button(top_frame, text="Filmler", command=lambda: self.switch_category('movies')).grid(row=0, column=0,
                                                                                                   padx=20, pady=10)
        ttk.Button(top_frame, text="Diziler", command=lambda: self.switch_category('series')).grid(row=0, column=1,
                                                                                                   padx=20, pady=10)

        self.info_label = ttk.Label(top_frame, text=f"Toplam Filmler: {len(self.movies)}")
        self.info_label.grid(row=0, column=2, padx=20, pady=10)

        # Sol çerçeve
        self.left_frame = tk.Frame(self.root, bg="#34495E")
        self.left_frame.grid(row=1, column=0, sticky="ns")

        # Sağ çerçeve
        self.right_frame = tk.Frame(self.root, width=200, bg="#1F3A52")
        self.right_frame.grid(row=1, column=2, sticky="ns")

        ttk.Button(self.right_frame, text="Detaylara Bak", command=self.show_details).grid(row=0, column=0, padx=10,
                                                                                           pady=20)
        ttk.Button(self.right_frame, text="Yorum veya Puan Ekle", command=self.add_review).grid(row=1, column=0,
                                                                                                padx=10, pady=20)
        ttk.Button(self.right_frame, text="Rastgele Öner", command=self.random_recommendation).grid(row=2, column=0,
                                                                                                    padx=10, pady=20)
        ttk.Button(self.right_frame, text="Listeye Film Ekle", command=self.open_add_to_list_window).grid(row=3,
                                                                                                          column=0,
                                                                                                          padx=10,
                                                                                                          pady=20)

        # Orta çerçeve
        self.center_frame = tk.Frame(self.root, bg="#2C3E50")
        self.center_frame.grid(row=1, column=1, sticky="nsew")

        self.load_genres()

    def switch_category(self, category):
        self.active_category = category
        if category == 'movies':
            self.info_label.config(text=f"Toplam Filmler: {len(self.movies)}")
        else:
            self.info_label.config(text=f"Toplam Diziler: {len(self.series)}")
        self.load_genres()

    def random_recommendation(self):
        # Bekleme ekranı
        loading_window = tk.Toplevel(self.root)
        loading_window.title("Öneri Bekleniyor")
        loading_window.geometry("300x100")
        tk.Label(loading_window, text="Öneri hazırlanıyor...", font=("Helvetica", 12)).pack(expand=True)
        self.root.update_idletasks()

        # 2 saniye bekle
        time.sleep(2)
        loading_window.destroy()

        # Rastgele öneri - Seçilen türe göre filtreleme
        data = self.movies if self.active_category == 'movies' else self.series
        filtered_data = [item for item in data if self.current_genre in item.get('genre', [])]
        if filtered_data:
            recommendation = random.choice(filtered_data)
            messagebox.showinfo("Öneri",
                                f"Başlık: {recommendation['title']}, Yıl: {recommendation['year']}, Puan: {recommendation.get('IMBDrating', 'N/A')}")
        else:
            messagebox.showinfo("Bilgi", "Seçilen türde öneri bulunamadı.")

    def open_add_to_list_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Listeye Film Ekle")
        add_window.geometry("400x400")

        # Dosya konumunu belirt
        folder_path = "kullanici_listeleri"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Liste adlarını al
        existing_lists = [f.split('.')[0] for f in os.listdir(folder_path) if f.endswith('.json')]

        tk.Label(add_window, text="Liste Seçin:").pack(pady=5)
        list_name_var = tk.StringVar()
        list_name_combobox = ttk.Combobox(add_window, textvariable=list_name_var, values=existing_lists)
        list_name_combobox.pack(pady=5)

        tk.Label(add_window, text="Yeni Liste Adı Girin:").pack(pady=5)
        new_list_entry = ttk.Entry(add_window)
        new_list_entry.pack(pady=5)

        tk.Label(add_window, text="Film Ara:").pack(pady=5)
        search_entry = ttk.Entry(add_window)
        search_entry.pack(pady=5)

        result_list = tk.Listbox(add_window, height=15)
        result_list.pack(pady=10)

        def update_results():
            query = search_entry.get().lower()
            result_list.delete(0, tk.END)
            data = self.movies + self.series
            for item in data:
                if query in item['title'].lower():
                    result_list.insert(tk.END, item['title'])

        search_entry.bind("<KeyRelease>", lambda event: update_results())

        def add_to_list():
            list_name = list_name_var.get().strip() or new_list_entry.get().strip()
            if not list_name:
                messagebox.showwarning("Uyarı", "Liste adı boş bırakılamaz!")
                return

            file_path = os.path.join(folder_path, f"{list_name}.json")
            selected = result_list.get(tk.ACTIVE)
            if selected:
                data = self.load_json_data(file_path) if os.path.exists(file_path) else []
                for item in self.movies + self.series:
                    if item['title'] == selected and item not in data:
                        data.append(item)
                        break
                self.save_json_data(file_path, data)
                messagebox.showinfo("Başarılı", f"{selected} listeye eklendi!")

        ttk.Button(add_window, text="Listeye Ekle", command=add_to_list).pack(pady=10)

    def save_json_data(self, file_path, data):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            messagebox.showinfo("Başarılı", f"Liste başarıyla {file_path} dosyasına kaydedildi!")
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya kaydedilirken bir hata oluştu: {str(e)}")

    def load_genres(self):
        for widget in self.left_frame.winfo_children():
            widget.destroy()

        # Butonlar için grid kullanımı
        row, col = 0, 0
        data = self.filter_data(self.movies if self.active_category == 'movies' else self.series)
        genres = sorted(set(genre for item in data for genre in item['genre']))

        for genre in genres:
            btn = ttk.Button(self.left_frame, text=genre, command=lambda g=genre: self.show_genre(g))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            col += 1
            if col > 2:  # 2 sütun olacak şekilde ayarla
                col = 0
                row += 1

        ttk.Button(self.left_frame, text="Tümünü Göster", command=self.show_all).grid(row=row + 1, columnspan=2,
                                                                                      pady=10, sticky="ew")

    def show_genre(self, genre):
        self.current_genre = genre
        data = self.filter_data(self.movies if self.active_category == 'movies' else self.series)
        filtered_data = [item for item in data if genre in item['genre']]
        self.display_table(filtered_data)

    def show_all(self):
        data = self.filter_data(self.movies if self.active_category == 'movies' else self.series)
        self.display_table(data)

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
            tk.Label(detail_window, text=item['title'], font=("Helvetica", 16, "bold"), bg="#2C3E50", fg="white").pack(
                pady=10)

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
                tk.Label(frame, text=f"{label}: ", font=("Helvetica", 12, "bold"), bg="#34495E", fg="white").pack(
                    side="left")
                tk.Label(frame, text=value, font=("Helvetica", 12), bg="#34495E", fg="white").pack(side="left")

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
