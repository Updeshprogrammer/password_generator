import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip


def generate_password(length, include_letters, include_numbers, include_symbols):
    character_set = ''
    if include_letters:
        character_set += string.ascii_letters
    if include_numbers:
        character_set += string.digits
    if include_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("No characters available to generate password.")

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password
def generate_password_gui():
    try:
        length = int(length_entry.get())
        include_letters = letters_var.get()
        include_numbers = numbers_var.get()
        include_symbols = symbols_var.get()

        password = generate_password(length, include_letters, include_numbers, include_symbols)
        result_label.config(text=password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard():
    password = result_label.cget("text")
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")

# Length
tk.Label(root, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

# Include letters
letters_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Letters", variable=letters_var).grid(row=1, column=0, columnspan=2)

# Include numbers
numbers_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, column=0, columnspan=2)

# Include symbols
symbols_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, columnspan=2)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password_gui).grid(row=4, column=0, columnspan=2)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=6, column=0, columnspan=2)

root.mainloop()
