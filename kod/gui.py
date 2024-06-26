import tkinter as tk
import oracledb
import commands

root = tk.Tk()

def open_start():
    root.geometry("800x600")
    root.title("Menetrend")
    root.configure(bg='#99f')
    try:
        # A user-t meg a jelszo-t sajátra köll átállítani hogy működjön
        dsn = oracledb.makedsn("localhost", 1521, service_name="xe")
        db = oracledb.connect(user="MATT", password="matt", dsn=dsn)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM felhasznalok")
        result = cursor.fetchall()
        print("Result:", result)
        if(result):
            connectionLabel = tk.Label(root, text="Connection established", bg="#99f")
            connectionLabel.place(x=50, y=50)

            mainButton = tk.Button(root, text="Main window", command=main_window, bg="#99f", fg="white")
            mainButton.place(x=50, y=150)
        else:
            errorLabel = tk.Label(root, text="Oops! Something ain't right", fg="red")
            errorLabel.pack()
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

    root.geometry("800x600")
    root.title("Menetrend")
    root.configure(bg='#99f')

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


def open_registration():
    global reg_window
    reg_window = tk.Toplevel(root)
    reg_window.geometry("800x600")
    reg_window.title("Regisztráció")
    reg_window.configure(bg='#99f')

    welcome_label = tk.Label(reg_window, text='Regisztráció', font=('bold', 20), bg='black', fg='white')
    welcome_label.place(x=100, y=100)

    name_label = tk.Label(reg_window, text='Név', font=('bold', 12), bg='black', fg='white')
    name_label.place(x=200, y=200)
    global name_entry
    name_entry = tk.Entry(reg_window)
    name_entry.place(x=300, y=200)

    password_label = tk.Label(reg_window, text='Jelszó', font=('bold', 12), bg='black', fg='white')
    password_label.place(x=200, y=250)
    global password_entry
    password_entry = tk.Entry(reg_window, show='*')
    password_entry.place(x=300, y=250)

    password_confirm_label = tk.Label(reg_window, text='Jelszó megerősítése', font=('bold', 12), bg='black', fg='white')
    password_confirm_label.place(x=150, y=300)
    global password_confirm_entry
    password_confirm_entry = tk.Entry(reg_window, show='*')
    password_confirm_entry.place(x=300, y=300)

    email_label = tk.Label(reg_window, text='E-mail', font=('bold', 12), bg='black', fg='white')
    email_label.place(x=200, y=350)
    global email_entry
    email_entry = tk.Entry(reg_window)
    email_entry.place(x=300, y=350)

    tipus_label = tk.Label(reg_window, text='Utastípus', font=('bold', 12), bg='black', fg='white')
    tipus_label.place(x=200, y=400)
    global tipus_entry
    tipus_entry = tk.Entry(reg_window)
    tipus_entry.place(x=300, y=400)

    login_button = tk.Button(reg_window, text='Belépés', width=20, height=2, command=reg_window.destroy)
    login_button.place(x=200, y=450)

    registrate_button = tk.Button(reg_window, text='Regisztráció', width=20, height=2, command=commands.register)
    registrate_button.place(x=350, y=450)


def open_dolgozo():
    return None