import qrcode
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import filedialog
from tkinter import IntVar


def string_to_qr(data, mode):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    if mode:
        img = qr.make_image(fill_color="black", back_color="white")
    else:
        img = qr.make_image(fill_color="#6BAAE4", back_color="#17405C")
    return img


def on_entry_click(event):
    if entry.get() == "Enter Data":
        entry.delete(0, "end")
        entry.config(fg="white")


def on_focusout(event):
    if entry.get() == "":
        entry.insert(0, "Enter Data")
        entry.config(fg="grey")


def save_qr():
    data = entry.get()
    if data != "Enter Data":
        mode = mode_var.get()
        img = string_to_qr(data, mode)
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            img.save(file_path)
            messagebox.showinfo("Info", "QR code saved successfully!")


root = tk.Tk()
root.title("QR Code Generator")

label = tk.Label(root, text="Generate Your QR:")
label.config(fg="Lightblue")
label.pack(pady=10)

entry = tk.Entry(root)
entry.insert(0, "Enter Data")
entry.config(fg="grey")
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focusout)
entry.pack(pady=10)

mode_var = IntVar()
mode_var.set(1)

light_mode = tk.Radiobutton(root, text="Light Mode", variable=mode_var, value=1)
light_mode.pack(pady=5)

dark_mode = tk.Radiobutton(root, text="Dark Mode", variable=mode_var, value=0)
dark_mode.pack(pady=5)

save_button = tk.Button(root, text="Save QR Code", command=save_qr)
save_button.pack(pady=10)

root.mainloop()
