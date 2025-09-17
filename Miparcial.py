import tkinter as tk
from tkinter import messagebox

# Lista para guardar el historial de solicitudes
historial_solicitudes = []

def abrir_ventana_secundaria():
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Ventana de Adivinanza")
    nueva_ventana.geometry("500x500")
    nueva_ventana.config(bg="#555CEC")
    nueva_ventana.iconbitmap("saul.ico")

    label_nueva = tk.Label(nueva_ventana, text="¿En qué puedo ayudarte?", bg="#555CEC", fg="white", font=("Arial", 14))
    label_nueva.pack(pady=10)

    frame_botones = tk.Frame(nueva_ventana, bg="#555CEC")
    frame_botones.pack(pady=10)

    frame_entry = tk.Frame(nueva_ventana, bg="#555CEC")
    frame_entry.pack(pady=10)

    # Variable para almacenar el entry actual
    entry_actual = tk.StringVar()

    def mostrar_entry(tipo):
        for widget in frame_entry.winfo_children():
            widget.destroy()

        tk.Label(frame_entry, text=f"Escribe tu solicitud para: {tipo}", bg="#555CEC", fg="white").pack()
        entry_box = tk.Entry(frame_entry, textvariable=entry_actual, width=40)
        entry_box.pack(pady=5)
        entry_actual.set("")  # Limpia el texto anterior

    def enviar_solicitud():
        texto = entry_actual.get().strip()
        if texto:
            historial_solicitudes.append(texto)
            messagebox.showinfo("Solicitud enviada", f"Se guardó la solicitud:\n\n{texto}")
            entry_actual.set("")  # Limpia el campo después de enviar
        else:
            messagebox.showwarning("Campo vacío", "Por favor escribe una solicitud antes de enviar.")

    def mostrar_historial():
        historial_ventana = tk.Toplevel(nueva_ventana)
        historial_ventana.title("Historial de Solicitudes")
        historial_ventana.geometry("400x300")
        historial_ventana.config(bg="#F5F5F5")
        historial_ventana.iconbitmap("saul.ico")

        if historial_solicitudes:
            texto_historial = "\n".join(f"{i+1}. {sol}" for i, sol in enumerate(historial_solicitudes))
        else:
            texto_historial = "No hay solicitudes registradas aún."

        tk.Label(historial_ventana, text=texto_historial, bg="#F5F5F5", justify="left", wraplength=380).pack(padx=10, pady=10)
        tk.Button(historial_ventana, text="Cerrar", command=historial_ventana.destroy).pack(pady=10)

    # Botones alineados en fila
    tk.Button(frame_botones, text="Estrategia de estudio",
              command=lambda: mostrar_entry("Estrategia de estudio")).pack(side="left", padx=5)

    tk.Button(frame_botones, text="Acompañamiento psicosocial",
              command=lambda: mostrar_entry("Acompañamiento psicosocial")).pack(side="left", padx=5)

    tk.Button(frame_botones, text="Tutoría",
              command=lambda: mostrar_entry("Tutoría")).pack(side="left", padx=5)

    # Botón para enviar ayuda
    tk.Button(nueva_ventana, text="Enviar solicitud de ayuda", command=enviar_solicitud).pack(pady=10)

    # Nuevo botón para ver historial
    tk.Button(nueva_ventana, text="Ver historial de solicitudes", command=mostrar_historial,
              bg="white", fg="#555CEC").pack(pady=5)


# 🔹 Ventanas de ayuda 🔹
def abrir_ventana_ayuda1():
    ayuda1 = tk.Toplevel(ventana)
    ayuda1.title("Ayuda - Uso del Asistente")
    ayuda1.geometry("420x320")
    ayuda1.config(bg="#F5F5F5")

    texto_ayuda = (
        "📖 **Cómo usar el asistente:**\n\n"
        "1️⃣ Ingresa tu nombre o email en el recuadro.\n"
        "2️⃣ Presiona el botón 'Ingresar'.\n"
        "3️⃣ Selecciona la opción que necesites:\n"
        "   • Estrategia de estudio\n"
        "   • Acompañamiento psicosocial\n"
        "   • Tutoría\n\n"
        "✏️ **Ejemplo de solicitud:**\n"
        "Hola, soy Gabriel y tengo dificultades con cálculo diferencial.\n"
        "¿Podrían ayudarme con estrategias de estudio?"
    )

    tk.Label(ayuda1, text=texto_ayuda, font=("Arial", 11), bg="#F5F5F5",
             wraplength=380, justify="left").pack(padx=15, pady=15)

    tk.Button(ayuda1, text="Cerrar", command=ayuda1.destroy).pack(pady=10)


def abrir_ventana_ayuda2():
    ayuda2 = tk.Toplevel(ventana)
    ayuda2.title("Ayuda - Información Extra")
    ayuda2.geometry("420x300")
    ayuda2.config(bg="#F5F5F5")

    texto_ayuda_extra = (
        "ℹ️ **Información adicional sobre el asistente:**\n\n"
        "✅ Puedes solicitar estrategias de estudio para mejorar tu rendimiento.\n"
        "✅ Acceder a acompañamiento psicosocial para apoyo emocional.\n"
        "✅ Solicitar tutorías personalizadas para resolver dudas específicas.\n\n"
        "💡 Usa estas herramientas para aprovechar al máximo tu aprendizaje."
    )

    tk.Label(ayuda2, text=texto_ayuda_extra, font=("Arial", 11), bg="#F5F5F5",
             wraplength=380, justify="left").pack(padx=15, pady=15)

    tk.Button(ayuda2, text="Cerrar", command=ayuda2.destroy).pack(pady=10)


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Prototipo de interfaz: Asistente de Saul")
ventana.geometry("500x500")
ventana.config(background="#555CEC")
ventana.iconbitmap("saul.ico")

# Frame superior con botones de ayuda
frame_superior = tk.Frame(ventana, bg="#555CEC")
frame_superior.pack(fill="x", pady=5)

btn_ayuda1 = tk.Button(frame_superior, text="?", command=abrir_ventana_ayuda1,
                       width=2, bg="white", fg="#555CEC", font=("Arial", 10, "bold"))
btn_ayuda1.pack(side="right", padx=5)

btn_ayuda2 = tk.Button(frame_superior, text="i", command=abrir_ventana_ayuda2,
                       width=2, bg="white", fg="#555CEC", font=("Arial", 10, "bold"))
btn_ayuda2.pack(side="right", padx=5)

# Etiqueta principal
label = tk.Label(ventana, text="Bienvenido al asistente virtual de Saul, ¿comenzamos?",
                 bg="#555CEC", fg="white", font=("Arial", 12, "bold"))
label.pack(pady=5)

# Entry principal
entry = tk.Entry(ventana)
entry.pack(pady=5)

# Botón principal
btn_ingresar = tk.Button(ventana,
                text="Ingresar",
                command=abrir_ventana_secundaria,
                font=("Arial", 14, "bold"),
                width=15,
                height=2,
                bg="white",
                fg="#555CEC",
                relief="raised")
btn_ingresar.pack(pady=10)

ventana.mainloop()
