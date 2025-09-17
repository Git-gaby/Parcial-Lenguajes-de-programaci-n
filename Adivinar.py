import tkinter as tk
from tkinter import messagebox
import random

def adivinar():
    try:
        numero_usuario = int(entry.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")
        return

    if numero_usuario < 1 or numero_usuario > 100:
        messagebox.showwarning("Advertencia", "El número debe estar entre 1 y 100.")
    elif numero_usuario == numero_secreto:
        messagebox.showinfo("¡Correcto!", "¡Adivinaste el número!")
    elif numero_usuario < numero_secreto:
        messagebox.showinfo("Sigue intentando", "El número es mayor.")
    else:
        messagebox.showinfo("Sigue intentando", "El número es menor.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Reto 2: Adivina el Número")
ventana.geometry("300x150")

# Cambiar ícono de la ventana (asegúrate que el archivo IN.ico esté en la misma carpeta)
ventana.iconbitmap(r"C:\Users\ci5\OneDrive\Desktop\Taller de seguimiento 1\taller\IN.ico")

# Generar número aleatorio
numero_secreto = random.randint(1, 100)

# Etiqueta
label = tk.Label(ventana, text="Adivina un número entre 1 y 100:")
label.pack(pady=5)

# Caja de texto
entry = tk.Entry(ventana)
entry.pack(pady=5)

# Botón
btn = tk.Button(ventana, text="Adivinar", command=adivinar)
btn.pack(pady=5)

ventana.mainloop()


"""
Este programa crea un juego sencillo para adivinar un número usando **Tkinter** como interfaz gráfica. Primero, importa `tkinter`,
`messagebox` y `random` para construir la ventana, mostrar mensajes y generar un número aleatorio entre 1 y 100. Luego define la función
`adivinar()`, que obtiene el número ingresado en la caja de texto, verifica si es válido y muestra mensajes informativos dependiendo de si el
número es mayor, menor o igual al número secreto. Después, se crea la ventana principal con título y tamaño fijo, se genera el número 
secreto y se añaden los widgets: una etiqueta con el mensaje, una caja de texto para que el usuario escriba su intento y un botón que 
al hacer clic ejecuta la función `adivinar()`. Finalmente, `ventana.mainloop()` mantiene la aplicación en ejecución hasta que el usuario
la cierre.
"""
