import tkinter as tk
from doctest import master

import oracledb
import commands
import pandas as pd
from tkinter import messagebox as MessageBox
import displayData as dd
from tkinter import *
import display_infos


root = tk.Tk()

def open_start():
    root.geometry("800x600")
    root.title("Menetrend")
    root.configure(bg='black')
    try:
        # A user-t meg a jelszo-t sajátra köll átállítani hogy működjön
        #dsn = oracledb.makedsn("localhost", 1521, service_name="xe")
        #db = oracledb.connect(user="MATT", password="matt", dsn=dsn)

        matt = {"user": "MATT", "pw": "oracle" "matt"}
        kamilla = {"user": "system", "pw": "oracle"}
        currentU = kamilla
        # A user-t meg a jelszo-t sajátra köll átállítani hogy működjön
        dsn = oracledb.makedsn("localhost", 1521, service_name="xe")
        db = oracledb.connect(user=currentU["user"], password=currentU["pw"], dsn=dsn)
        #db = commands.connect()

        # with pandas try, columns displayed but no rows
        """chunk_size = 10  # Adjust as needed
        query = "SELECT * FROM felhasznalok"
        result_chunks = pd.read_sql(query, db, chunksize=chunk_size)
        for chunk in result_chunks:
            # Process each chunk of data
            print(chunk)"""



        cursor = db.cursor()
        cursor.execute("SELECT * FROM varosok")
        result = cursor.fetchone()
        print("Result:", result)
        print(type(result))
        data = list(result)
        rowCount = cursor.rowcount
        colCount = 4

        if(result):
            MessageBox.showinfo("Siker", "Sikeres csatlakozás az adatbázishoz!")
            tk.Button(text="Kezdőlap", command=open_login).pack(expand=True)
        else:
            MessageBox.showinfo("Hiba", "Sajnos nem sikerült csatlakozni az adatbázishoz, kérlek próbáld újra!")
        cursor.close()
        db.close()
        root.mainloop()
    except oracledb.Error as error:
        print("Error:", error)

def main_window():
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("800x600")
    root.title("Menetrend")
    root.configure(bg='#99f')

    login_button = tk.Button(root, text='Belépés', width=20, height=2, command=open_login, bg='white', fg='black')
    login_button.place(x=100, y=100)

    register_button = tk.Button(root, text='Regisztráció', width=20, height=2, command=open_registration, bg='white', fg='black')
    register_button.place(x=250, y=100)

def open_login():
    for widget in root.winfo_children():
        widget.destroy()



    login_lable = tk.Label(root, text='Belépés', font=('bold', 20), bg='black', fg='white')
    login_lable.place(x=200, y=100)

    id_label = tk.Label(root, text='Email cím', font=('bold', 12), bg='black', fg='white')
    id_label.place(x=200, y=200)

    global login_id_entry
    login_id_entry = tk.Entry(root)
    login_id_entry.place(x=300, y=200)

    password_label = tk.Label(root, text='Jelszó', font=('bold', 12), bg='black', fg='white')
    password_label.place(x=200, y=250)

    global login_password_entry
    login_password_entry = tk.Entry(root, show='*')
    login_password_entry.place(x=300, y=250)

    login_button = tk.Button(root, text='Belépés', width=20, height=2, command=commands.login)
    login_button.place(x=200, y=300)

    register_button = tk.Button(root, text='Regisztráció', width=20, height=2, command=open_registration)
    register_button.place(x=350, y=300)

    search_button = tk.Button(root, text="Menetrend keresés", width=20, height=2, command=open_Menetrendek)
    search_button.place(x=250, y=400)


def open_registration():



    global reg_window
    reg_window = tk.Toplevel(root)
    reg_window.geometry("800x600")
    reg_window.title("Regisztráció")
    reg_window.configure(bg='black')

    tk.Label(reg_window, text='Regisztráció', font=('bold', 20), bg='black', fg='white').pack()
    #welcome_label.place(x=100, y=100)

    tk.Label(reg_window, text='Név', font=('bold', 12), bg='black', fg='white').pack()
    #name_label.place(x=200, y=200)
    global name_entry
    name_entry = tk.Entry(reg_window)
    #name_entry.place(x=300, y=200)
    name_entry.pack(expand=True)

    tk.Label(reg_window, text='Jelszó', font=('bold', 12), bg='black', fg='white').pack()
    #password_label.place(x=200, y=250)
    global password_entry
    password_entry = tk.Entry(reg_window, show='*')
    #password_entry.place(x=300, y=250)
    password_entry.pack(expand=True)

    tk.Label(reg_window, text='Jelszó megerősítése', font=('bold', 12), bg='black', fg='white').pack()
    #password_confirm_label.place(x=150, y=300)
    global password_confirm_entry
    password_confirm_entry = tk.Entry(reg_window, show='*')
    #password_confirm_entry.place(x=300, y=300)
    password_confirm_entry.pack()

    tk.Label(reg_window, text='E-mail', font=('bold', 12), bg='black', fg='white').pack()
    #email_label.place(x=200, y=350)
    global email_entry
    email_entry = tk.Entry(reg_window)
    #email_entry.place(x=300, y=350)
    email_entry.pack(expand=True)

    """tipus_label = tk.Label(reg_window, text='Utastípus', font=('bold', 12), bg='black', fg='white')
    tipus_label.place(x=200, y=400)
    global tipus_entry
    tipus_entry = tk.Entry(reg_window)
    tipus_entry.place(x=300, y=400)"""

    global tipus
    tipus = StringVar(reg_window)
    tipus.set("Felnőtt")

    tk.Label(reg_window, text='Utastípus', font=('bold', 12), bg='black', fg='white').pack()
    OptionMenu(reg_window, tipus, 'Felnőtt', 'Tanuló', 'Gyermek', 'Nyugdíjas', 'Kedvezményes', 'Admin').pack(expand=True)






    tk.Button(reg_window, text='Regisztráció', width=20, height=2, command=commands.register).pack(expand=True)
    #registrate_button.place(x=350, y=450)

    tk.Button(reg_window, text='Belépés', width=20, height=2, command=reg_window.destroy).pack()
    # login_button.place(x=200, y=450)


def open_dolgozo():
    for widget in root.winfo_children():
        widget.destroy()
    #TODO: build this method actually this is just a test
    tk.Button(root, text="További lekérdezések", width=20, height=2, command=display_infos.display).pack(expand=True)


    pass


def open_admin_options():
    for widget in root.winfo_children():
        widget.destroy()
    #TODO: build this method actually this is just a test
    tk.Button(root, text="Lekérdezések", width=20, height=2, command=display_infos.admin_display()).pack(expand=True)
    tk.Button(root, text="Város hozzáadása", width=20, height=2, command=addCity).pack(expand=True)


def addCity    ():
    for widget in root.winfo_children():
        widget.destroy()


    tk.Label(root,text='Állomás neve').pack()
    nevE = tk.Entry(root)
    nevE.pack()
    tk.Label(root,text='Irányítószám').pack()
    irszE = tk.Entry(root)
    irszE.pack()
    tk.Label(root,text='Régió').pack()
    regioE = tk.Entry(root)
    regioE.pack()
    tk.Label(root, text='Orszag').pack()
    orszagE = tk.Entry(root)
    orszagE.pack()


    def insertCity():

        nev = nevE.get()
        irsz = irszE.get()
        regio = regioE.get()
        orszag = orszagE.get()
        db = commands.connect()

        print(nev)

        if not (irszE and nevE and regioE and orszagE):
            MessageBox.showinfo("Hiba", "Minden mező kitöltése kötelező!")
            return

        cursor = db.cursor()

        try:
            cursor.execute(
                "INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (:s, :s, :s, :s)",
                (irsz, nev, regio, orszag))
            db.commit()
            MessageBox.showinfo("Siker", "Sikeresen hozzáadva!")
            nevE.delete(0, 'end')
            irszE.delete(0, 'end')
            regioE.delete(0, 'end')
            orszagE.delete(0, 'end')
        except oracledb.Error as err:
            MessageBox.showinfo("Hiba", "Hiba történt a regisztráció során: {}".format(err))
            db.rollback()

        db.close()


    okAE = tk.Button(root,text='INSERT', command=insertCity)
    okAE.pack()



def open_Menetrendek():
    #TODO: get from Mate this
    MessageBox.showinfo("Working on it...", "Loading....")




