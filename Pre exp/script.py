import pandas as pd
import tkinter as tk
from excel_analyser_rewa import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

def create_display_file():
    root = tk.Tk()
    root.title("Pre-exp result")
    root.geometry("800x600")  # Set the fixed width and height of the window


    # Create a label and an entry widget for name input
    label = tk.Label(root, text="Enter ID:")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()

    def load_dataframe():
        name = entry.get()
        if name:
            df = analyze_excel_data(name)
            if df is not None:
                # Destroy the input widgets
                label.destroy()
                entry.destroy()

                # Create a scrolled text widget
                text_widget = ScrolledText(root, width=80, height=30, font=("Courier New", 11))
                text_widget.pack()

                # Insert dataframe content into the scrolled text widget
                text_widget.insert(tk.END, df)
                file_name = f"results/{name}_pre_exp_result.txt"
                with open(file_name, "w") as file:
                    file.write(text_widget.get(1.0, tk.END))
                def on_escape_key(event):

                    root.destroy()

                # Bind the Escape key to the window
                root.bind("<Escape>", on_escape_key)
            else:
                messagebox.showerror("Error", "No matching CSV files found.")
        else:
            messagebox.showwarning("Warning", "Please enter a name.")

    # Create a button to load the dataframe
    button = ttk.Button(root, text="Load DataFrame", command=load_dataframe)
    button.pack()

    root.mainloop()


# Example usage
# Assuming you already have a dataframe called 'df'
create_display_file()
