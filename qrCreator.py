import qrcode
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def generar_qr():
    url = entrada.get()
    if not url.strip():
        messagebox.showwarning("Error", "Por favor, ingresa un enlace.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_qr = os.path.join(carpeta_actual, "qr_temp.png")

    img.save(ruta_qr)

    max_width, max_height = 300, 300  # tamaño máximo para mostrar en la app
    img = img.resize((max_width, max_height), Image.Resampling.LANCZOS)

    img_tk = ImageTk.PhotoImage(img)
    ventana.geometry("300x470")
    etiqueta_img.config(image=img_tk)
    etiqueta_img.image = img_tk

def guardar_qr():
    url = entrada.get()
    if not url.strip():
        messagebox.showwarning("Error", "Primero ingresa un enlace y genera el QR.")
        return

    archivo = filedialog.asksaveasfilename(defaultextension=".png",
                                           filetypes=[("PNG files", "*.png")])
    if archivo:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(archivo)
        messagebox.showinfo("Éxito", f"Código QR guardado en:\n{archivo}")

ventana = tk.Tk()
ventana.title("Generador de Códigos QR")
ventana.geometry("300x300")
ventana.resizable(False, False)
ventana.config(bg="black")

tk.Label(ventana, text="Ingresa un enlace:", font=("Arial", 12), fg="white", bg="black").pack(pady=10)
entrada = tk.Entry(ventana, width=40, font=("Arial", 10))
entrada.pack(pady=5)

tk.Button(ventana, text="Crear QR", command=generar_qr, bg="lightblue").pack(pady=10)
tk.Button(ventana, text="Guardar QR", command=guardar_qr, bg="lightgreen").pack(pady=5)

etiqueta_img = tk.Label(ventana)
etiqueta_img.pack(pady=20)

ventana.mainloop()
