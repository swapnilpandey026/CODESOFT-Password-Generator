import tkinter as tk
from tkinter import messagebox
import string
import random

# ---------------- Password Generator Logic ----------------
def generate_password():
    length = length_var.get()
    
    try:
        length = int(length)
        if length < 4:
            messagebox.showwarning("Invalid", "Length must be at least 4.")
            return
    except ValueError:
        messagebox.showwarning("Invalid", "Please enter a valid number.")
        return

    # Character pools based on user selection
    characters = ""
    if use_letters.get():
        characters += string.ascii_letters
    if use_numbers.get():
        characters += string.digits
    if use_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Invalid", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f7f7f7")

# Title Label
tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg="#f7f7f7").pack(pady=10)

# Length input
tk.Label(root, text="Password Length:", font=("Arial", 12), bg="#f7f7f7").pack()
length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var, font=("Arial", 12), width=10, justify='center')
length_entry.pack(pady=5)
length_var.set("12")  # Default length

# Checkboxes for options
use_letters = tk.BooleanVar(value=True)
use_numbers = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=use_letters, bg="#f7f7f7", font=("Arial", 10)).pack()
tk.Checkbutton(root, text="Include Numbers", variable=use_numbers, bg="#f7f7f7", font=("Arial", 10)).pack()
tk.Checkbutton(root, text="Include Symbols", variable=use_symbols, bg="#f7f7f7", font=("Arial", 10)).pack()

# Generate Button
tk.Button(root, text="Generate Password", font=("Arial", 12), bg="#4CAF50", fg="white", command=generate_password).pack(pady=10)

# Password Entry
password_entry = tk.Entry(root, font=("Arial", 14), width=30, justify='center')
password_entry.pack(pady=5)

# Copy Button
tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), bg="#2196F3", fg="white", command=copy_to_clipboard).pack(pady=5)

root.mainloop()
