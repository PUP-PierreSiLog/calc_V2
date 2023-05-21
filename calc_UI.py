import tkinter as tk
import pyfiglet
class UI:
    def __init__(self):
        self.window=tk.Tk()

    def quit_window(self):
        self.window.quit()

    def initial_screen(self):
        self.window.minsize(500,300)
        self.window.title("Calculator")
        label=tk.Label(self.window, text=pyfiglet.figlet_format("Calculator", justify="center", font="slant"))
        label.pack()
        label2=tk.Label(self.window, text="Welcome to the calculator made with OOP. Made by Pierre Victor T. Zurbito")
        label2.pack()
        button=tk.Button(self.window, text="Take me in!", command=self.operation_selection)
        button.pack()

    def operation_selection(self):
        self.window.destroy()
        operation_window=tk.Tk()
        self.window.minsize(500,300)
        self.window.title("Calculator")
        label=tk.Label(self.window, text="Please choose your operation from the dropdown box.")
        label.pack()

    def run(self):
        self.window.mainloop()
        

ui=UI()
ui.initial_screen()
ui.run()