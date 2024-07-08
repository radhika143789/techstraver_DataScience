import tkinter as tk
from tkinter import messagebox
import pyqrcode
import png

# Function to generate QR code
def generate_qr():
    input_data = entry.get()
    if input_data.strip() == "":
        messagebox.showerror("Error", "Input field cannot be empty.")
        return
    qr_code = pyqrcode.create(input_data)
    qr_code.png('qr_code.png', scale=6)
    messagebox.showinfo("Success", "QR Code generated and saved as qr_code.png")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place the input field and labels
tk.Label(root, text="Enter URL or String:").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Create and place the generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=20)

# Run the application
root.mainloop()
