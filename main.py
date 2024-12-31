import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

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

    collection_frame = tk.Frame(root, bg="#34495e", bd=5)
    collection_frame.pack(pady=20, padx=20, fill="both", expand=True)

    top_frame = tk.Frame(collection_frame, bg="#34495e")
    top_frame.pack(fill="x", pady=(0,10))
    top_frame.columnconfigure(0, weight=0)
    top_frame.columnconfigure(1, weight=1)

    back_button = ttk.Button(top_frame, text="Ana Menüye Dön", command=lambda: go_to_main_menu(collection_frame), style="TBack.TButton")
    back_button.grid(row=0, column=0, sticky="w", padx=5)

    title_label_collection = tk.Label(top_frame, text="Eserlerim", font=("Arial", 18, "bold"), fg="#ecf0f1", bg="#34495e")
    title_label_collection.grid(row=0, column=1, pady=5)

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

    def update_tree(filter_type):
        for item in collection_tree.get_children():
            collection_tree.delete(item)
        for item in collection_data[username]:
            if filter_type == "Hepsi" or item['türü'] == filter_type:
                collection_tree.insert("", tk.END, values=(item['adı'], item['türü'], item['durum'], item['puan'], item['not']))

    update_tree("Hepsi")

    def add_item():
        collection_frame.pack_forget()
        add_item_frame = tk.Frame(root, bg="#34495e", bd=5)
        add_item_frame.pack(pady=20, padx=20, fill="both", expand=True)
        tk.Label(add_item_frame, text="Adı:", font=("Arial", 12), bg="#34495e", fg="#ecf0f1").grid(row=0, column=0, pady=5, padx=10, sticky="e")
        name_entry = ttk.Entry(add_item_frame, font=("Arial", 12))
        name_entry.grid(row=0, column=1, pady=5, padx=10, sticky="w")
        tk.Label(add_item_frame, text="Türü:", font=("Arial", 12), bg="#34495e", fg="#ecf0f1").grid(row=1, column=0, pady=5, padx=10, sticky="e")
        type_combobox_add = ttk.Combobox(add_item_frame, values=["Film", "Dizi", "Diğer"], font=("Arial", 12), state="readonly")
        type_combobox_add.grid(row=1, column=1, pady=5, padx=10, sticky="w")
        tk.Label(add_item_frame, text="Durum:", font=("Arial", 12), bg="#34495e", fg="#ecf0f1").grid(row=2, column=0, pady=5, padx=10, sticky="e")
        status_combobox = ttk.Combobox(add_item_frame, values=["İzlendi", "İzleniyor", "İzlenecek"], font=("Arial", 12), state="readonly")
        status_combobox.grid(row=2, column=1, pady=5, padx=10, sticky="w")
        tk.Label(add_item_frame, text="Puan (1-5):", font=("Arial", 12), bg="#34495e", fg="#ecf0f1").grid(row=3, column=0, pady=5, padx=10, sticky="e")
        rating_combobox = ttk.Combobox(add_item_frame, values=["1", "2", "3", "4", "5"], font=("Arial", 12), state="readonly")
        rating_combobox.grid(row=3, column=1, pady=5, padx=10, sticky="w")
        tk.Label(add_item_frame, text="Not:", font=("Arial", 12), bg="#34495e", fg="#ecf0f1").grid(row=4, column=0, pady=5, padx=10, sticky="ne")
        note_entry = tk.Text(add_item_frame, font=("Arial", 12), height=5, width=30)
        note_entry.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        def save_item():
            name = name_entry.get()
            type_ = type_combobox_add.get()
            status = status_combobox.get()
            rating = rating_combobox.get()
            note = note_entry.get("1.0", "end").strip()
            if not name or not type_ or not status or not rating:
                messagebox.showerror("Hata", "Adı, Türü, Durum ve Puan alanları doldurulmalıdır!")
                return
            new_item = {
                "adı": name,
                "türü": type_,
                "durum": status,
                "puan": rating,
                "not": note
            }
            collection_data[username].append(new_item)
            with open("collection.json", "w") as file:
                json.dump(collection_data, file, indent=4)
            current_filter = filter_combobox.get()
            update_tree(current_filter)
            add_item_frame.pack_forget()
            collection_frame.pack(pady=20, padx=20, fill="both", expand=True)

        def cancel():
            add_item_frame.pack_forget()
            collection_frame.pack(pady=20, padx=20, fill="both", expand=True)

        ttk.Button(add_item_frame, text="Ekle", command=save_item).grid(row=5, column=0, pady=20, padx=10, sticky="e")
        ttk.Button(add_item_frame, text="İptal", command=cancel).grid(row=5, column=1, pady=20, padx=10, sticky="w")

    def delete_item():
        selected_item = collection_tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Emin misiniz?", "Bu eseri silmek istediğinize emin misiniz?")
            if confirm:
                index = collection_tree.index(selected_item)
                collection_tree.delete(selected_item)
                del collection_data[username][index]
                with open("collection.json", "w") as file:
                    json.dump(collection_data, file, indent=4)

    def edit_item():
        selected_item = collection_tree.selection()
        if not selected_item:
            messagebox.showerror("Hata", "Düzenlemek için bir eser seçmelisiniz!")
            return
        index = collection_tree.index(selected_item)
        item_data = collection_data[username][index]
        collection_frame.pack_forget()
        edit_item_frame = tk.Frame(root, bg="#34495e", bd=5)
        edit_item_frame.pack(pady=20, padx=20, fill="both", expand=True)
        tk.Label(edit_item_frame, text="Adı:", font=("Arial", 12), bg="#34495e", fg="#ecf0f1").grid(row=0, column=0, pady=5, padx=10, sticky="e")
        name_entry = ttk.Entry(edit_item_frame, font=("Arial", 12))
        name_entry.grid(row=0, column=1, pady=5, padx=10, sticky="w")
        name_entry.insert(0, item_data["adı"])
        tk.Label(edit_item_frame, text="Türü:", font=("Arial", 12), bg="#34495e", fg="#ecf0f1").grid(row=1, column=0, pady=5, padx=10, sticky="e")
        type_combobox_edit = ttk.Combobox(edit_item_frame, values=["Film", "Dizi", "Diğer"], font=("Arial", 12), state="readonly")
        type_combobox_edit.grid(row=1, column=1, pady=5, padx=10, sticky="w")
        type_combobox_edit.set(item_data["türü"])
        tk.Label(edit_item_frame, text="Durum:", font=("Arial", 12), bg="#34495e", fg="#ecf0f1").grid(row=2, column=0, pady=5, padx=10, sticky="e")
        status_combobox = ttk.Combobox(edit_item_frame, values=["İzlendi", "İzleniyor", "İzlenecek"], font=("Arial", 12), state="readonly")
        status_combobox.grid(row=2, column=1, pady=5, padx=10, sticky="w")
        status_combobox.set(item_data["durum"])
        tk.Label(edit_item_frame, text="Puan (1-5):", font=("Arial", 12), bg="#34495e", fg="#ecf0f1").grid(row=3, column=0, pady=5, padx=10, sticky="e")
        rating_combobox = ttk.Combobox(edit_item_frame, values=["1", "2", "3", "4", "5"], font=("Arial", 12), state="readonly")
        rating_combobox.grid(row=3, column=1, pady=5, padx=10, sticky="w")
        rating_combobox.set(item_data["puan"])
        tk.Label(edit_item_frame, text="Not:", font=("Arial", 12), bg="#34495e", fg="#ecf0f1").grid(row=4, column=0, pady=5, padx=10, sticky="ne")
        note_entry = tk.Text(edit_item_frame, font=("Arial", 12), height=5, width=30)
        note_entry.grid(row=4, column=1, pady=5, padx=10, sticky="w")
        note_entry.insert("1.0", item_data["not"])

        def save_edited_item():
            name = name_entry.get()
            type_ = type_combobox_edit.get()
            status = status_combobox.get()
            rating = rating_combobox.get()
            note = note_entry.get("1.0", "end").strip()
            if not name or not type_ or not status or not rating:
                messagebox.showerror("Hata", "Adı, Türü, Durum ve Puan alanları doldurulmalıdır!")
                return
            updated_item = {
                "adı": name,
                "türü": type_,
                "durum": status,
                "puan": rating,
                "not": note
            }
            collection_data[username][index] = updated_item
            with open("collection.json", "w") as file:
                json.dump(collection_data, file, indent=4)
            current_filter = filter_combobox.get()
            update_tree(current_filter)
            edit_item_frame.pack_forget()
            collection_frame.pack(pady=20, padx=20, fill="both", expand=True)

        def cancel_edit():
            edit_item_frame.pack_forget()
            collection_frame.pack(pady=20, padx=20, fill="both", expand=True)

        ttk.Button(edit_item_frame, text="Kaydet", command=save_edited_item).grid(row=5, column=0, pady=20, padx=10, sticky="e")
        ttk.Button(edit_item_frame, text="İptal", command=cancel_edit).grid(row=5, column=1, pady=20, padx=10, sticky="w")

    def go_to_main_menu(frame_to_hide):
        frame_to_hide.pack_forget()
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        register_label.place(relx=0.95, rely=0.95, anchor="se")
        forgot_password_label.place(relx=0.05, rely=0.95, anchor="sw")

    button_frame = tk.Frame(collection_frame, bg="#34495e")
    button_frame.pack(side="left", fill="y", padx=10, pady=10)
    ttk.Button(button_frame, text="Eser Ekle", command=add_item).pack(anchor="w", pady=5)
    ttk.Button(button_frame, text="Eser Sil", command=delete_item).pack(anchor="w", pady=5)
    ttk.Button(button_frame, text="Eser Düzenle", command=edit_item).pack(anchor="w", pady=5)

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

def create_account():
    frame.pack_forget()
    register_label.place_forget()
    forgot_password_label.place_forget()
    create_account_frame = tk.Frame(root, bg="#34495e", bd=5)
    create_account_frame.pack(pady=20, padx=20, fill="both", expand=True)
    tk.Label(create_account_frame, text="Kullanıcı Adı:", font=("Arial", 12), fg="#ecf0f1", bg="#34495e").grid(row=0, column=0, pady=10, padx=10, sticky="e")
    new_username_entry = ttk.Entry(create_account_frame, font=("Arial", 12))
    new_username_entry.grid(row=0, column=1, pady=10, padx=10, sticky="ew")
    tk.Label(create_account_frame, text="Şifre:", font=("Arial", 12), fg="#ecf0f1", bg="#34495e").grid(row=1, column=0, pady=10, padx=10, sticky="e")
    new_password_entry = ttk.Entry(create_account_frame, font=("Arial", 12), show="*")
    new_password_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")
    tk.Label(create_account_frame, text="En Sevdiğiniz Hayvan:", font=("Arial", 12), fg="#ecf0f1", bg="#34495e").grid(row=2, column=0, pady=10, padx=10, sticky="e")
    favorite_animal_entry = ttk.Entry(create_account_frame, font=("Arial", 12))
    favorite_animal_entry.grid(row=2, column=1, pady=10, padx=10, sticky="ew")

    def save_account():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()
        favorite_animal = favorite_animal_entry.get()
        if not new_username or not new_password or not favorite_animal:
            messagebox.showerror("Hata", "Tüm alanlar doldurulmalıdır!")
            return
        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}
        if new_username in users:
            messagebox.showerror("Hata", "Bu kullanıcı adı zaten kullanılıyor!")
        else:
            users[new_username] = {"password": new_password, "favorite_animal": favorite_animal}
            with open("users.json", "w") as file:
                json.dump(users, file, indent=4)
            messagebox.showinfo("Başarılı", "Hesap başarıyla oluşturuldu!")
            create_account_frame.pack_forget()
            frame.pack(pady=20, padx=20, fill="both", expand=True)
            register_label.place(relx=0.95, rely=0.95, anchor="se")
            forgot_password_label.place(relx=0.05, rely=0.95, anchor="sw")

    ttk.Button(create_account_frame, text="Hesap Oluştur", command=save_account).grid(row=3, column=0, columnspan=2, pady=20)
    ttk.Button(create_account_frame, text="Geri", command=lambda: [create_account_frame.pack_forget(), frame.pack(pady=20, padx=20, fill="both", expand=True), register_label.place(relx=0.95, rely=0.95, anchor="se"), forgot_password_label.place(relx=0.05, rely=0.95, anchor="sw")]).grid(row=4, column=0, columnspan=2, pady=10)

def forgot_password():
    frame.pack_forget()
    register_label.place_forget()
    forgot_password_label.place_forget()
    forgot_password_frame = tk.Frame(root, bg="#34495e", bd=5)
    forgot_password_frame.pack(pady=20, padx=20, fill="both", expand=True)
    tk.Label(forgot_password_frame, text="Kullanıcı Adı:", font=("Arial", 12), fg="#ecf0f1", bg="#34495e").grid(row=0, column=0, pady=10, padx=10, sticky="e")
    username_entry_fp = ttk.Entry(forgot_password_frame, font=("Arial", 12))
    username_entry_fp.grid(row=0, column=1, pady=10, padx=10, sticky="ew")
    tk.Label(forgot_password_frame, text="En Sevdiğiniz Hayvan:", font=("Arial", 12), fg="#ecf0f1", bg="#34495e").grid(row=1, column=0, pady=10, padx=10, sticky="e")
    animal_entry = ttk.Entry(forgot_password_frame, font=("Arial", 12))
    animal_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

    def verify_details():
        username = username_entry_fp.get()
        animal = animal_entry.get()
        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}
        if username in users and users[username]["favorite_animal"] == animal:
            forgot_password_frame.pack_forget()
            reset_password_frame = tk.Frame(root, bg="#34495e", bd=5)
            reset_password_frame.pack(pady=20, padx=20, fill="both", expand=True)
            tk.Label(reset_password_frame, text="Yeni Şifre:", font=("Arial", 12), fg="#ecf0f1", bg="#34495e").grid(row=0, column=0, pady=10, padx=10, sticky="e")
            new_password_entry = ttk.Entry(reset_password_frame, font=("Arial", 12), show="*")
            new_password_entry.grid(row=0, column=1, pady=10, padx=10, sticky="ew")
            tk.Label(reset_password_frame, text="Yeni Şifre (Tekrar):", font=("Arial", 12), fg="#ecf0f1", bg="#34495e").grid(row=1, column=0, pady=10, padx=10, sticky="e")
            confirm_password_entry = ttk.Entry(reset_password_frame, font=("Arial", 12), show="*")
            confirm_password_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

            def reset_password():
                new_password = new_password_entry.get()
                confirm_password = confirm_password_entry.get()
                if new_password != confirm_password:
                    messagebox.showerror("Hata", "Şifreler eşleşmiyor!")
                    return
                users[username]["password"] = new_password
                with open("users.json", "w") as file:
                    json.dump(users, file, indent=4)
                messagebox.showinfo("Başarılı", "Şifre başarıyla değiştirildi!")
                reset_password_frame.pack_forget()
                frame.pack(pady=20, padx=20, fill="both", expand=True)
                register_label.place(relx=0.95, rely=0.95, anchor="se")
                forgot_password_label.place(relx=0.05, rely=0.95, anchor="sw")
            ttk.Button(reset_password_frame, text="Şifreyi Değiştir", command=reset_password).grid(row=2, column=0, columnspan=2, pady=20)
        else:
            messagebox.showerror("Hata", "Bilgiler doğru değil!")

    ttk.Button(forgot_password_frame, text="Doğrula", command=verify_details).grid(row=2, column=0, columnspan=2, pady=20)
    ttk.Button(forgot_password_frame, text="Geri", command=lambda: [forgot_password_frame.pack_forget(), frame.pack(pady=20, padx=20, fill="both", expand=True), register_label.place(relx=0.95, rely=0.95, anchor="se"), forgot_password_label.place(relx=0.05, rely=0.95, anchor="sw")]).grid(row=3, column=0, columnspan=2, pady=10)

def resize_fonts(event):
    new_width = root.winfo_width()
    new_font_size = max(12, new_width // 50)
    title_label.config(font=("Arial", new_font_size, "bold"))
    username_label.config(font=("Arial", new_font_size))
    password_label.config(font=("Arial", new_font_size))
    login_button.config(style="TButton")

root = tk.Tk()
root.title("Film Listeleme Uygulaması")
root.geometry("800x600")
root.configure(bg="#2c3e50")

title_label = tk.Label(root, text="Film Listeleme Uygulaması", font=("Arial", 18, "bold"), fg="#ecf0f1", bg="#2c3e50")
title_label.pack(pady=20)

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

register_label = tk.Label(root, text="Hesabınız yok mu? Hesap oluşturun.", fg="#3498db", bg="#2c3e50", font=("Arial", 10, "italic"), cursor="hand2")
register_label.place(relx=0.95, rely=0.95, anchor="se")
register_label.bind("<Button-1>", lambda e: create_account())

forgot_password_label = tk.Label(root, text="Şifremi Unuttum", fg="#3498db", bg="#2c3e50", font=("Arial", 10, "italic"), cursor="hand2")
forgot_password_label.place(relx=0.05, rely=0.95, anchor="sw")
forgot_password_label.bind("<Button-1>", lambda e: forgot_password())

style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TEntry", padding=5)
style.configure("TBack.TButton", font=("Arial", 10), foreground="#7f8c8d", padding=5)

title_label.bind("<Configure>", resize_fonts)
root.bind("<Configure>", resize_fonts)

root.mainloop()