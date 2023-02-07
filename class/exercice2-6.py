import tkinter as tk

book_types = ["Science-Fiction", "Thriller", "Roman d'amour", "Historique", "Autre"]

#possibilité d'ajouter un nouveau type de roman
def add_new_book_type():
    new_type = new_type_entry.get()
    book_types.append(new_type)
    book_types.sort(key=lambda x: x if x != "Autre" else "ZZZ")
    book_type_var.set(new_type)
    book_type_dropdown["menu"].add_command(label=new_type, command=lambda: book_type_var.set(new_type))

#sauvegarde du contenu dans un fichier txt
def save_book_details():
    with open("book_details.txt", "a") as file:
        book_name = name_entry.get()
        author = author_entry.get()
        publisher = publisher_entry.get()
        barcode = barcode_entry.get()
        book_type = book_type_var.get()
        description = description_entry.get("1.0", tk.END)
        file.write(f"{book_name},{author},{publisher},{barcode},{book_type},{description}\n")

#création fenêtre de 500*500
root = tk.Tk()
root.geometry("500x500")


#création de chaque label les uns après les autres
name_label = tk.Label(root, text="Nom du livre :")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

author_label = tk.Label(root, text="Auteur :")
author_label.pack()

author_entry = tk.Entry(root)
author_entry.pack()

publisher_label = tk.Label(root, text="Maison d'édition :")
publisher_label.pack()

publisher_entry = tk.Entry(root)
publisher_entry.pack()

barcode_label = tk.Label(root, text="Code barre :")
barcode_label.pack()

barcode_entry = tk.Entry(root)
barcode_entry.pack()

book_type_label = tk.Label(root, text="Type de roman :")
book_type_label.pack()

book_type_var = tk.StringVar()
book_type_var.set("Choisir le type")

book_type_dropdown = tk.OptionMenu(root, book_type_var, *book_types)
book_type_dropdown.pack()

new_type_label = tk.Label(root, text="Ajouter un nouveau type :")
new_type_label.pack()

new_type_entry = tk.Entry(root)
new_type_entry.pack()

new_type_button = tk.Button(root, text="Ajouter", command=add_new_book_type)
new_type_button.pack()

description_label = tk.Label(root, text="Description :")
description_label.pack()

description_entry = tk.Text(root, height=5, width=30)
description_entry.pack()

save_button = tk.Button(root, text="Enregistrer", command=save_book_details)
save_button.pack()

root.mainloop()
