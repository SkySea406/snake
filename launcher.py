import tkinter as tk
from tkinter import messagebox
import os
def baslat():
    dif = dife.get()
    if dif.type() != int:
        messagebox.showerror("Error", "Please enter a valid difficulty level.")
    else:
        os.startfile("snake.py")
        parent.destroy()
        exit()
parent = tk.Tk()

parent.title("Launcher")
parent.geometry("100x100")
parent.resizable(False, False)
parent.configure(bg="white")


diff = tk.Label(parent, text="Enter Difficulty", bg="white")
diff.pack()
dife = tk.Entry(parent, bg="white")
dife.pack()
ok = tk.Button(parent, text="OK", command=baslat, bg="white")
ok.pack()




parent.mainloop()