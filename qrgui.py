import tkinter as tk
from tkinter import messagebox
from qrgen import generate_qr_code
from PIL import Image, ImageTk
import os

def on_generate_qr_code():
    qrlink = entry.get()
    
    if not qrlink:
        messagebox.showwarning("Input Error", "Please enter a link.")
        return
    
    try:
        filename = generate_qr_code(qrlink)  # Generate QR code
        display_qr_code(filename)  # Display the generated QR code
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def display_qr_code(filename):
    # Load the generated QR code image
    img = Image.open(filename)
    img = img.resize((250, 250), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)

    # Update the label with the QR code image
    qr_code_label.config(image=img_tk)
    qr_code_label.image = img_tk  # Keep a reference
    qr_code_label.pack()

# Create the main application window
app = tk.Tk()
app.title("QR Code Generator")

# Create a label and an entry widget
label = tk.Label(app, text="Enter your Link:")
label.pack(pady=10)

entry = tk.Entry(app, width=40)
entry.pack(pady=10)

# Create a button to generate the QR code
generate_button = tk.Button(app, text="Generate QR Code", command=on_generate_qr_code)
generate_button.pack(pady=10)

# Label to display the generated QR code
qr_code_label = tk.Label(app)
qr_code_label.pack(pady=10)

# Start the GUI event loop
app.mainloop()
