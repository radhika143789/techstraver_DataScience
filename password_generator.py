import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, min_lower, min_upper, min_digits, min_symbols, include_symbols=True):
    if length < (min_lower + min_upper + min_digits + min_symbols):
        raise ValueError("Password length is too short for the given minimum requirements.")
    
    lower = [random.choice(string.ascii_lowercase) for _ in range(min_lower)]
    upper = [random.choice(string.ascii_uppercase) for _ in range(min_upper)]
    digits = [random.choice(string.digits) for _ in range(min_digits)]
    symbols = [random.choice(string.punctuation) for _ in range(min_symbols)] if include_symbols else []

    remaining_length = length - (min_lower + min_upper + min_digits + min_symbols)
    if include_symbols:
        all_chars = string.ascii_letters + string.digits + string.punctuation
    else:
        all_chars = string.ascii_letters + string.digits

    remaining = [random.choice(all_chars) for _ in range(remaining_length)]

    password_list = lower + upper + digits + symbols + remaining
    random.shuffle(password_list)

    return ''.join(password_list)

def generate_password_gui():
    try:
        length = int(length_entry.get())
        min_lower = int(min_lower_entry.get())
        min_upper = int(min_upper_entry.get())
        min_digits = int(min_digits_entry.get())
        min_symbols = int(min_symbols_entry.get())
        include_symbols = include_symbols_var.get()
        
        password = generate_password(length, min_lower, min_upper, min_digits, min_symbols, include_symbols)
        result_label.config(text=f"Generated password: {password}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers for all fields.")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

tk.Label(root, text="Min lowercase:").grid(row=1, column=0)
min_lower_entry = tk.Entry(root)
min_lower_entry.grid(row=1, column=1)

tk.Label(root, text="Min uppercase:").grid(row=2, column=0)
min_upper_entry = tk.Entry(root)
min_upper_entry.grid(row=2, column=1)

tk.Label(root, text="Min digits:").grid(row=3, column=0)
min_digits_entry = tk.Entry(root)
min_digits_entry.grid(row=3, column=1)

tk.Label(root, text="Min symbols:").grid(row=4, column=0)
min_symbols_entry = tk.Entry(root)
min_symbols_entry.grid(row=4, column=1)

include_symbols_var = tk.BooleanVar()
include_symbols_check = tk.Checkbutton(root, text="Include symbols", variable=include_symbols_var)
include_symbols_check.grid(row=5, columnspan=2)

generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.grid(row=6, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=7, columnspan=2)

root.mainloop()
