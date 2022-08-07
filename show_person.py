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
    text="Enter ID.",
    bg="white", 
    fg="black"
)
label.pack()

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)

frm_form.pack()

lbl_id = tk.Label(master=frm_form, text="Id:")
ent_id = tk.Entry(master=frm_form, width=50)

lbl_id.grid(row=1, column=0)
ent_id.grid(row=1, column=1)

#Button
def send_id():
    get_id = int(ent_id.get())
    cursor.execute("SELECT name, surname, phone FROM vacancy where id = {}".format(get_id))
    data=cursor.fetchall()
    label2.config(text="{}".format(data))
     
label2 = tk.Label(
    text="",
    bg="white", 
    fg="black"
)
label2.pack()


frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Show", command=send_id)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

w.mainloop()
cursor.close()