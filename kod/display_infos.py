from tkinter import *
from tkinter import ttk
import commands
import gui
import tkinter as tk


def display():
    for widget in gui.root.winfo_children():
        widget.destroy()

    tk.Button(text="Városok listája", command=list_cities).pack(expand=True)

    tk.Button(text="Vonalak listája", command=list_Lines).pack(expand=True)

def admin_display():
    for widget in gui.root.winfo_children():
        widget.destroy()

    tk.Button(text="Vonalak listája", command=list_Lines_admin).pack(expand=True)

    tk.Button(text="Városok listája", command=lambda: list_cities(True)).pack(expand=True)

    tk.Button(text="Felhasznalok listaja", command=list_users).pack(expand=True)

def list_cities(isAdmin=False):
    for widget in gui.root.winfo_children():
        widget.destroy()
    db = commands.connect()
    cursor = db.cursor()

    result = cursor.execute("SELECT * FROM varosok")

    tree = ttk.Treeview(gui.root, columns=("Column1", "Column2", "Column3", "Column4"), show="headings")
    tree.heading("#1", text="Irányítószám")
    tree.heading("#2", text="Név")
    tree.heading("#3", text="Régió")
    tree.heading("#4", text="Ország")

    # Adatok hozzáadása a Treeview-hoz
    for row in result:
        tree.insert("", "end", values=row)

    # Treeview hozzáadása a Tkinter ablakhoz
    tree.pack(expand=True, fill="both", pady=10)

    if(isAdmin):
        tk.Button(text="Vissza", command=admin_display).pack(expand=True)
    else:
        tk.Button(text="Vissza", command=display).pack(expand=True)

    db.close()


def list_Lines():
    for widget in gui.root.winfo_children():
        widget.destroy()


    db = commands.connect()
    cursor = db.cursor()

    cursor.execute("SELECT nev FROM vonatvonalak")

    result = cursor.fetchall()

    print(result)

    tree = ttk.Treeview(gui.root, columns=("c1"), show="headings")
    tree.heading("#1", text="Vonalnév")

    for row in result:
        tree.insert("", "end", values=row)

    tree.pack(expand=True)

    tk.Button(text="Vissza", command=display).pack(expand=True)

    db.close()
def list_Lines_admin():
    for widget in gui.root.winfo_children():
        widget.destroy()

    db = commands.connect()
    cursor = db.cursor()

    cursor.execute("SELECT nev FROM vonatvonalak")

    result = cursor.fetchall()

    print(result)

    tree = ttk.Treeview(gui.root, columns=("c1"), show="headings")
    tree.heading("#1", text="Vonalnév")

    for row in result:
        tree.insert("", "end", values=row)

    tree.pack(expand=True)
    tk.Button(text="Vissza", command=admin_display).pack(expand=True)

    db.close()


def list_users():
    for widget in gui.root.winfo_children():
        widget.destroy()

    db = commands.connect()
    cursor = db.cursor()

    cursor.execute("Select email, nev, utastipus, regisztracio_datuma FROM felhasznalok")
    result = cursor.fetchall()

    print(result)

    tree = ttk.Treeview(gui.root, columns=("C1", "C2", "C3", "C4"), show="headings")
    tree.heading("#1",text="E-mail")
    tree.heading("#2", text="Név")
    tree.heading("#3", text="Utastípus")
    tree.heading("#4", text="Regisztráció dátuma")

    for row in result:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill="both", pady=10)

    tk.Button(text="Vissza", command=admin_display).pack(expand=True)

    db.close()
