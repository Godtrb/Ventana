import tkinter as tk
from unittest import result

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Escribe digito 1:")
etiqueta.pack(pady=5)

dig1 = tk.Entry(ventana)
dig1.pack(pady=5)

etiqueta = tk.Label(ventana, text="Escribe digito 2:")
etiqueta.pack(pady=5)

dig2 = tk.Entry(ventana)
dig2.pack(pady=5)

def sum():
    num1=dig1.get()
    num1=int(num1)
    num2= dig2.get()
    num2 = int(num2)
    resul=num1+num2
    etiqueta.config(text=f"{resul}")

def min():
    entrada.delete(0, tk.END)
    etiqueta.config(text="Escribe tu nombre:")

boton_saludar = tk.Button(ventana, text="sum", command=sum)
boton_saludar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar",)
boton_limpiar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()