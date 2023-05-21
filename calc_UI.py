import tkinter as tk
import pyfiglet

class UI:
    def initial_screen(self):
        window=tk.Tk()
        window.minsize(500,300)
        window.title("Calculator")
        label=tk.Label(window, text=pyfiglet.figlet_format("Calculator", justify="center", font="slant"))
        label.pack()
        label2=tk.Label(window, text="Welcome to the calculator made with OOP. Made by Pierre Victor T. Zurbito")
        label2.pack()
        button=tk.Button(window, text="Take me in!", command=window.quit)
        button.pack()
        window.mainloop()

    def operation_selection():
        selected_item = dropdown.get()
        print("Selected item:", selected_item)

        window = tk.Tk()

        # Create a list of options for the dropdown
        options = ["Option 1", "Option 2", "Option 3", "Option 4"]

        # Create a Combobox widget
        dropdown = ttk.Combobox(window, values=options)

        # Set an initial value for the dropdown
        dropdown.set("Select an option")

        # Bind an event handler to the selection event
        dropdown.bind("<<ComboboxSelected>>", operation_selection)

        # Add the dropdown to the window
        dropdown.pack()

        window.mainloop()
ui=UI()
ui.initial_screen()
ui.operation_selection()