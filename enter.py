import tkinter as tk
import mysql.connector

connection = mysql.connector.connect(host="127.0.0.1",
                                    database="project",
                                    user="root",
                                    password="")

cursor=connection.cursor()

w = tk.Tk()

w.geometry("500x200")

label = tk.Label(
    text="Enter information about yourself.",
    bg="white", 
    fg="black"
)
label.pack()

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)

frm_form.pack()

lbl_name = tk.Label(master=frm_form, text="Name:")
ent_name = tk.Entry(master=frm_form, width=50)

lbl_name.grid(row=0, column=0)
ent_name.grid(row=0, column=1)
 
lbl_surname = tk.Label(master=frm_form, text="Surname:")
ent_surname = tk.Entry(master=frm_form, width=50)

lbl_surname.grid(row=1, column=0)
ent_surname.grid(row=1, column=1)
 
lbl_phone = tk.Label(master=frm_form, text="Phone number: +")
ent_phone = tk.Entry(master=frm_form, width=50)

lbl_phone.grid(row=2, column=0)
ent_phone.grid(row=2, column=1)

#Buttons
def send_inf():
    get_name = ent_name.get()
    get_surname = ent_surname.get()
    get_phone = int(ent_phone.get())
    cursor.execute("select name, surname, phone from vacancy where name = %s and surname = %s and phone = %s",
    (get_name, get_surname, get_phone))

    if cursor.fetchone() is None:
        cursor.execute("insert into vacancy(name, surname, phone) values(%s, %s, %s)",
        (get_name, get_surname, get_phone))
        connection.commit()

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Save", command=send_inf)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

w.mainloop()
cursor.close()