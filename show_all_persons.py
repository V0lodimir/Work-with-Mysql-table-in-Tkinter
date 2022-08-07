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

def show_users():
    cursor.execute("select * from vacancy")
    data = cursor.fetchall()
    text.insert(tk.END, data)

text = tk.Text(width=50, height=9)
text.pack()

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Show", command=show_users)
btn_submit.pack(padx=10, ipadx=10)

w.mainloop()
cursor.close()