import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import sys
import os

# Kullanıcı girişi fonksiyonu
register_label = tk.Label(root, text="Hesap Oluştur", fg="#3498db", bg="#2c3e50", font=("Arial", 10, "italic"), cursor="hand2")
register_label.place(relx=0.95, rely=0.95, anchor="se")

def login():
    username = username_entry.get()
    password = password_entry.get()
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}
    if username in users and users[username]["password"] == password:
        messagebox.showinfo("Giriş Başarılı", f"Hoş geldiniz, {username}!")
        frame.pack_forget()
        register_label.place_forget()
        forgot_password_label.place_forget()
        display_collection(username)
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı!")

# Koleksiyon ekranını gösteren fonksiyon
def display_collection(username):
    try:
        with open("collection.json", "r") as file:
            collection_data = json.load(file)
    except FileNotFoundError:
        collection_data = {}
    if username not in collection_data:
        collection_data[username] = []
        with open("collection.json", "w") as file:
            json.dump(collection_data, file, indent=4)

    # Ana koleksiyon penceresi
    collection_frame = tk.Frame(root, bg="#34495e", bd=5)
    collection_frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Üst başlık çubuğu
    top_frame = tk.Frame(collection_frame, bg="#34495e")
    top_frame.pack(fill="x", pady=(0,10))
    top_frame.columnconfigure(0, weight=0)
    top_frame.columnconfigure(1, weight=1)

    back_button = ttk.Button(top_frame, text="Ana Menüye Dön", command=lambda: go_to_main_menu(collection_frame), style="TBack.TButton")
    back_button.grid(row=0, column=0, sticky="w", padx=5)

    title_label_collection = tk.Label(top_frame, text="Eserlerim", font=("Arial", 18, "bold"), fg="#ecf0f1", bg="#34495e")
    title_label_collection.grid(row=0, column=1, pady=5)

    # Tablo yapısı
    columns = ("Ad", "Tür", "Durum", "Puan", "Not")
    collection_tree = ttk.Treeview(collection_frame, columns=columns, show="headings")
    collection_tree.pack(pady=10, padx=10, fill="both", expand=True)
    collection_tree.heading("Ad", text="Ad")
    collection_tree.heading("Tür", text="Tür")
    collection_tree.heading("Durum", text="Durum")
    collection_tree.heading("Puan", text="Puan")
    collection_tree.heading("Not", text="Not")
    collection_tree.column("Ad", width=150)
    collection_tree.column("Tür", width=100)
    collection_tree.column("Durum", width=100)
    collection_tree.column("Puan", width=50)
    collection_tree.column("Not", width=200)

    # Tabloyu güncelleyen fonksiyon
    def update_tree(filter_type):
        for item in collection_tree.get_children():
            collection_tree.delete(item)
        for item in collection_data[username]:
            if filter_type == "Hepsi" or item['türü'] == filter_type:
                collection_tree.insert("", tk.END, values=(item['adı'], item['türü'], item['durum'], item['puan'], item['not']))

    update_tree("Hepsi")

    # Tür filtresi
    filter_frame = tk.Frame(collection_frame, bg="#34495e")
    filter_frame.pack(side="bottom", anchor="e", pady=5, padx=5)
    tk.Label(filter_frame, text="Tür Filtrele:", font=("Arial", 12), bg="#34495e", fg="#ecf0f1").pack(side="left", padx=5)
    filter_combobox = ttk.Combobox(filter_frame, values=["Hepsi", "Film", "Dizi", "Diğer"], font=("Arial", 12), state="readonly")
    filter_combobox.set("Hepsi")
    filter_combobox.pack(side="left", padx=5)

    def apply_filter():
        selected_filter = filter_combobox.get()
        update_tree(selected_filter)

    ttk.Button(filter_frame, text="Filtrele", command=apply_filter).pack(side="left", padx=5)

# Ana menüye geri dön fonksiyonu
def go_to_main_menu(frame_to_hide):
    frame_to_hide.pack_forget()
    frame.pack(pady=20, padx=20, fill="both", expand=True)

# Ana pencere ayarları
root = tk.Tk()
root.title("Film Listeleme Uygulaması")
root.geometry("800x600")
root.configure(bg="#2c3e50")

# Ana başlık etiketi
title_label = tk.Label(root, text="Film Listeleme Uygulaması", font=("Arial", 18, "bold"), fg="#ecf0f1", bg="#2c3e50")
title_label.pack(pady=20)

# Ana giriş ekranı
frame = tk.Frame(root, bg="#34495e", bd=5)
frame.pack(pady=20, padx=20, fill="both", expand=True)

username_label = tk.Label(frame, text="Kullanıcı Adı:", font=("Arial", 12), fg="#ecf0f1", bg="#34495e")
username_label.grid(row=0, column=0, pady=10, padx=10, sticky="e")
username_entry = ttk.Entry(frame, font=("Arial", 12))
username_entry.grid(row=0, column=1, pady=10, padx=10, sticky="ew")

password_label = tk.Label(frame, text="Şifre:", font=("Arial", 12), fg="#ecf0f1", bg="#34495e")
password_label.grid(row=1, column=0, pady=10, padx=10, sticky="e")
password_entry = ttk.Entry(frame, font=("Arial", 12), show="*")
password_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

login_button = ttk.Button(frame, text="Giriş Yap", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
