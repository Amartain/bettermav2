import oracledb
import gui
import hashlib
import tkinter as tk
from tkinter import messagebox as MessageBox
import pandas as pd

# Connection to database
def connect():
    matt = {"user": "MATT", "pw": "oracle" "matt"}
    kamilla = {"user": "system", "pw": "oracle"}
    currentU = kamilla
    # A user-t meg a jelszo-t sajátra köll átállítani hogy működjön
    dsn = oracledb.makedsn("localhost", 1521, service_name="xe")
    db = oracledb.connect(user=currentU["user"], password=currentU["pw"], dsn=dsn)

    return db





def login():
    email = gui.login_id_entry.get()
    print(email)
    jelszo = gui.login_password_entry.get()

    jelszo_hash = hashlib.sha3_256(jelszo.encode()).hexdigest()
    jelszo = jelszo_hash
    print(jelszo)

    #A user-t meg a jelszo-t sajátra köll átállítani hogy működjön
    #dsn = oracledb.makedsn("localhost", 1521, service_name="xe")
    #db = oracledb.connect(user=kamilla["user"], password=kamilla["pw"], dsn=dsn)

    # use connect function instead having like a gazzilion of db open lines copied
    db = connect()

    cursor = db.cursor()
    print("cursor pipa")

    try:
        cursor.execute("SELECT * FROM felhasznalok WHERE email = :s", (email,))
        print("execute is done")
        result = cursor.fetchone()
        print("fetch is done")
        print(result)

        if result is None:
            MessageBox.showinfo("Hiba", "Nincs ilyen ceges_ID!")
        elif result[2] != jelszo:
            MessageBox.showinfo("Hiba", "Hibás jelszó!")
        else:
            global Email
            Email = result[0]
            print(result[0])
            print(result[1])
            if result[1] == 'Ada Min':
                MessageBox.showinfo("Info", "Üdvözöljük {} adminunk!".format(result[1]))
                global felhasznalo_email
                gui.open_admin_options()
            else:
                MessageBox.showinfo("Info", "Üdvözöljük {}!".format(result[1]))
                gui.open_dolgozo()
    except oracledb.Error as err:
        MessageBox.showinfo("Hiba", "Hiba történt a belépés során: {}".format(err))

    db.close()


def register():
    nev = gui.name_entry.get()
    jelszo = gui.password_entry.get()
    jelszo_megerosites = gui.password_confirm_entry.get()
    email = gui.email_entry.get()
    tipus = gui.tipus.get()

    if not (nev and jelszo and email):
        MessageBox.showinfo("Hiba", "Minden mező kitöltése kötelező!")
        return

    if jelszo != jelszo_megerosites:
        MessageBox.showinfo("Hiba", "A jelszavak nem egyeznek!")
        return

    jelszo_hash = hashlib.sha3_256(jelszo.encode()).hexdigest()
    jelszo = jelszo_hash
    gui.password_entry.delete(0, 'end')
    gui.password_confirm_entry.delete(0, 'end')
    jelszo_megerosites = ""

    ##dsn = oracledb.makedsn("localhost", 1521, service_name="xe")
    #db = oracledb.connect(user="MATT", password="matt", dsn=dsn)
    db = connect()

    cursor = db.cursor()

    try:
        cursor.execute(
            "INSERT INTO Felhasznalok (email, nev, jelszo, utastipus) VALUES (:s, :s, :s, :s)",
            (email, nev, jelszo, tipus))
        db.commit()
        MessageBox.showinfo("Siker", "Sikeres regisztráció!")
        gui.reg_window.destroy()
        MessageBox.showinfo("Siker", "A ceges_ID: {}".format(email))
    except oracledb.Error as err:
        MessageBox.showinfo("Hiba", "Hiba történt a regisztráció során: {}".format(err))
        db.rollback()

    db.close()


# K tries things sectiion

