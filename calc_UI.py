import tkinter as tk
import pyfiglet
class UI:
    def quit_window(self):
        window=tk.Tk()
        window.quit()

    def initial_screen(self):
        window=tk.Tk()
        window.minsize(500,300)
        window.title("Calculator")
        label=tk.Label(window, text=pyfiglet.figlet_format("Calculator", justify="center", font="slant"))
        label.pack()
        label2=tk.Label(window, text="Welcome to the calculator made with OOP. Made by Pierre Victor T. Zurbito")
        label2.pack()
        button=tk.Button(window, text="Take me in!", command=self.quit_window)
        button.pack()
        window.mainloop()

    def operation_selection(self):
        window=tk.Tk()
        window.minsize(500,300)
        window.title("Calculator")
        label=tk.Label(window, text="Please choose your operation from the dropdown box.")
        label.pack()
        window.mainloop()
        

ui=UI()
ui.initial_screen()
ui.operation_selection()