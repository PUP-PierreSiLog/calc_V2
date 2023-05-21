import tkinter as tk
import pyfiglet

class UI:
    def Operation_selection(self):
        window=tk.Tk()
        window.minsize(500,500)
        window.title("Calculator")
        label=tk.Label(window, text=pyfiglet.figlet_format("Calculator", justify="center", font="slant"))
        label.pack()
        window.mainloop()

ui=UI()
ui.Operation_selection()