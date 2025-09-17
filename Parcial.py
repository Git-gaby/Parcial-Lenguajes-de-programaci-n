import tkinter as tk
from tkinter import messagebox

# =========================
# FUNCIONES
# =========================
def mostrar_tutorial():
    messagebox.showinfo("Tutorial", "Esta aplicación tiene dos marcos.\n"
                                   "En el marco izquierdo hay botones que interactúan con el marco derecho.\n"
                                   "Usa el menú superior para ver información o salir.")

def salir():
    ventana.destroy()

def mostrar_funcionalidad1():
    messagebox.showinfo("Funcionalidad 1", "El primer botón cambia el texto en el marco derecho.")

def mostrar_funcionalidad2():
    messagebox.showinfo("Funcionalidad 2", "El segundo botón cambia el color de fondo de la aplicación.")

def mostrar_acerca_de():
    messagebox.showinfo("Acerca de", "Autor: Gabriel\nAplicación creada como práctica de Tkinter.")

# =========================
# FUNCIONES DE LOS BOTONES
# =========================
def cambiar_texto():
    etiqueta_derecha.config(text="¡Hola, mundo!", fg="blue")

def cambiar_color():
    ventana.config(bg="lightgreen")
    marco_izquierdo.config(bg="lightgreen")
    marco_derecho.config(bg="lightgreen")

def mostrar_mensaje():
    messagebox.showinfo("Saludo", "¡Has hecho clic en el tercer botón!")

# =========================
# VENTANA PRINCIPAL
# =========================
ventana = tk.Tk()
ventana.title("Aplicación GUI - Reto")
ventana.geometry("600x400")
ventana.iconbitmap("gitlab.ico")  # Asegúrate de tener el archivo icono.ico en el mismo directorio

# =========================
# MENÚ SUPERIOR
# =========================
barra_menu = tk.Menu(ventana)

# Menú Inicio
menu_inicio = tk.Menu(barra_menu, tearoff=0)
menu_inicio.add_command(label="Tutorial de la aplicación", command=mostrar_tutorial)
menu_inicio.add_separator()
menu_inicio.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Inicio", menu=menu_inicio)

# Menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Funcionalidad 1", command=mostrar_funcionalidad1)
menu_ayuda.add_command(label="Funcionalidad 2", command=mostrar_funcionalidad2)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

# Menú Acerca de
menu_acerca = tk.Menu(barra_menu, tearoff=0)
menu_acerca.add_command(label="Acerca de", command=mostrar_acerca_de)
barra_menu.add_cascade(label="Acerca de", menu=menu_acerca)

ventana.config(menu=barra_menu)

# =========================
# MARCOS
# =========================
marco_izquierdo = tk.Frame(ventana, width=200, bg="lightgray")
marco_izquierdo.pack(side="left", fill="y")

marco_derecho = tk.Frame(ventana, bg="white")
marco_derecho.pack(side="right", expand=True, fill="both")

# =========================
# CONTENIDO MARCO IZQUIERDO
# =========================
tk.Label(marco_izquierdo, text="Opciones de la aplicación:", bg="lightgray", font=("Arial", 12, "bold")).pack(pady=10)

boton_texto = tk.Button(marco_izquierdo, text="Cambiar texto", command=cambiar_texto)
boton_texto.pack(pady=5, fill="x")

boton_color = tk.Button(marco_izquierdo, text="Cambiar color", command=cambiar_color)
boton_color.pack(pady=5, fill="x")

boton_mensaje = tk.Button(marco_izquierdo, text="Mostrar mensaje", command=mostrar_mensaje)
boton_mensaje.pack(pady=5, fill="x")

# =========================
# CONTENIDO MARCO DERECHO
# =========================
etiqueta_derecha = tk.Label(marco_derecho, text="Bienvenido a la aplicación", font=("Arial", 16), bg="white")
etiqueta_derecha.pack(expand=True)

# =========================
# INICIAR BUCLE
# =========================
ventana.mainloop()
