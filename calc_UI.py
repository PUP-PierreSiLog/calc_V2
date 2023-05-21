import tkinter as tk
import pyfiglet
from tkinter import ttk
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
        operation_window.minsize(500,300)
        operation_window.title("Calculator")
        label=tk.Label(operation_window, text="Please choose your operation from the dropdown box.")
        label.pack()

        operations=['Addition', 'Subtraction', 'Multiplication', 'Division']
        # Create a Combobox widget for operations
        dropdown = ttk.Combobox(operation_window, values=operations)
        dropdown.set("Select an operation")
        dropdown.pack()

        def handle_selection(event):
            global selected_operation
            selected_operation = dropdown.get()
            print("Selected operation:", selected_operation)

        dropdown.bind("<<ComboboxSelected>>", handle_selection)

        operation_window.mainloop()

    def run(self):
        self.window.mainloop()
        

ui=UI()
ui.initial_screen()
ui.run()