import tkinter as tk
from tkinter import messagebox
import os


def baslat():
    dif = dife.get()
    
    if not dif.isdigit() and dif != "2player":
        messagebox.showerror("Error", "Please enter a valid difficulty level.")
        
    else:
        dir = os.path.dirname(os.path.realpath(__file__))
        snakedir = os.path.join(dir, "snake.py")

        os.system("python "+snakedir+" "+dif)
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
run = tk.Button(parent, text="Run", command=baslat, bg="white")
run.pack()




parent.mainloop()
