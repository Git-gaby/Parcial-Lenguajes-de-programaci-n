import tkinter as tk
from tkinter import messagebox

# =========================
# Clases
# =========================
class Receta:
    """Clase que representa una receta con nombre e ingredientes."""
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes


class GestorRecetas:
    """Clase que gestiona la lista de recetas."""
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, nombre, ingredientes):
        self.recetas.append(Receta(nombre, ingredientes))

    def eliminar_receta(self, indice):
        try:
            return self.recetas.pop(indice).nombre
        except IndexError:
            return None


# =========================
# Funciones
# =========================
def agregar_receta():
    nombre = entry_nombre.get().strip()
    ingredientes = [ing.strip() for ing in entry_ingredientes.get().split(",") if ing.strip()]

    if nombre and ingredientes:
        gestor.agregar_receta(nombre, ingredientes)
        listbox_recetas.insert(tk.END, nombre)
        entry_nombre.delete(0, tk.END)
        entry_ingredientes.delete(0, tk.END)
        messagebox.showinfo("Receta agregada", f"La receta '{nombre}' ha sido agregada.")
    else:
        messagebox.showwarning("Error", "Por favor, ingrese un nombre y al menos un ingrediente.")


def ver_ingredientes():
    seleccion = listbox_recetas.curselection()
    if seleccion:
        indice = seleccion[0]
        receta = gestor.recetas[indice]
        ingredientes = ", ".join(receta.ingredientes)
        messagebox.showinfo(f"Ingredientes de {receta.nombre}", ingredientes)
    else:
        messagebox.showwarning("Error", "Seleccione una receta para ver sus ingredientes.")


def eliminar_receta():
    seleccion = listbox_recetas.curselection()
    if seleccion:
        indice = seleccion[0]
        nombre = gestor.eliminar_receta(indice)
        if nombre:
            listbox_recetas.delete(indice)
            messagebox.showinfo("Receta eliminada", f"La receta '{nombre}' ha sido eliminada.")
        else:
            messagebox.showerror("Error", "No se pudo eliminar la receta.")
    else:
        messagebox.showwarning("Error", "Seleccione una receta para eliminar.")


def mostrar_ayuda():
    instrucciones = (
        "Instrucciones de uso:\n\n"
        "1. Escriba el nombre de la receta en el campo 'Nombre de la receta'.\n"
        "2. Escriba los ingredientes separados por coma en el campo correspondiente.\n"
        "3. Presione 'Agregar receta' para guardarla en la lista.\n"
        "4. Seleccione una receta de la lista y presione 'Ver ingredientes' para verlos.\n"
        "5. Seleccione una receta y presione 'Eliminar receta' para borrarla."
    )
    messagebox.showinfo("Ayuda", instrucciones)


def mostrar_informacion():
    messagebox.showinfo("Información", "Gestor de Recetas\nHecho el 16/09/2025 por Gabriel Gómez.")


# =========================
# Ventana principal
# =========================
ventana = tk.Tk()
ventana.title("Gestor de Recetas")
ventana.geometry("500x600")

# Ícono de la ventana (usa .ico si es posible)
ruta_icono = "git.ico"
try:
    ventana.iconbitmap(r"C:\Users\ci5\OneDrive\Desktop\Taller de seguimiento 1\taller\git.ico")
except Exception as e:
    print(f"No se pudo cargar el ícono: {e}")

gestor = GestorRecetas()

# =========================
# Widgets
# =========================

# Frame superior con botones de ayuda e información
frame_superior = tk.Frame(ventana)
frame_superior.pack(pady=5, anchor="w")

btn_ayuda = tk.Button(frame_superior, text="Ayuda", command=mostrar_ayuda)
btn_ayuda.pack(side="left", padx=5)

btn_info = tk.Button(frame_superior, text="Información", command=mostrar_informacion)
btn_info.pack(side="left", padx=5)

# Título del programa
label_titulo = tk.Label(ventana, text="Gestor de Recetas", font=("Arial", 16, "bold"))
label_titulo.pack(pady=5)

# Entradas
label_nombre = tk.Label(ventana, text="Nombre de la receta:")
label_nombre.pack(pady=2)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=2)

label_ingredientes = tk.Label(ventana, text="Ingredientes (separados por coma):")
label_ingredientes.pack(pady=2)
entry_ingredientes = tk.Entry(ventana)
entry_ingredientes.pack(pady=2)

# Botones
btn_agregar = tk.Button(ventana, text="Agregar receta", command=agregar_receta)
btn_agregar.pack(pady=5)

listbox_recetas = tk.Listbox(ventana, height=10)
listbox_recetas.pack(pady=5, fill=tk.BOTH, expand=True)

btn_ver = tk.Button(ventana, text="Ver ingredientes", command=ver_ingredientes)
btn_ver.pack(pady=2)

btn_eliminar = tk.Button(ventana, text="Eliminar receta", command=eliminar_receta)
btn_eliminar.pack(pady=2)

# Ejecutar la ventana
ventana.mainloop()



# =========================
# Lógica principal
# =========================
gestor = GestorRecetas()
ventana.mainloop()
