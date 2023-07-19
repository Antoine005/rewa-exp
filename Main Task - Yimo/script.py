import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import pandas as pd
from excel_analyser_rewa import *


def create_display_file():
    root = tk.Tk()
    root.title("Pre-exp result")
    root.geometry("800x600")  # Set the fixed width and height of the window

    # Create a label and an entry widget for ID input
    label = tk.Label(root, text="Enter ID:")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()

    def load_dataframe():
        id = entry.get()
        if id:
            df = analyze_excel_data(id)
            if df is not None:
                # Destroy the input widgets
                label.destroy()
                entry.destroy()

                # Create a scrolled text widget
                text_widget = ScrolledText(root, width=80, height=30, font=("Courier New", 11))
                text_widget.pack()

                # Insert DataFrame content into the scrolled text widget
                text_widget.insert(tk.END, df.to_string())

                def on_escape_key(event):
                    root.destroy()

                # Bind the Escape key to the window
                root.bind("<Escape>", on_escape_key)
            else:
                messagebox.showerror("Error", "No matching CSV files found.")
        else:
            messagebox.showwarning("Warning", "Please enter an ID.")

    # Create a button to load the DataFrame
    button = ttk.Button(root, text="Load DataFrame", command=load_dataframe)
    button.pack()

    root.mainloop()


# Example usage
create_display_file()
