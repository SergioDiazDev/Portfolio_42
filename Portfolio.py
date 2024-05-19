import tkinter as tk
from tkinter import messagebox
import subprocess

def crear_interfaz_con_dos_botones():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Proyectos 42")
    root.geometry("600x400")


    # Funciones de los botones
    def minishell():
        try:
            subprocess.run(['gnome-terminal', '--', 'make', '-C', 'minishell/'])
            subprocess.run(['gnome-terminal', '--', './minishell/minishell'])

        except Exception as e:
            tk.messagebox.showerror("Error", str(e))

    def salir():
        root.quit()

    # Crear los botones y colocarlos en la ventana
    btn_mensaje = tk.Button(root, text="Minishell", command=minishell)
    btn_salir = tk.Button(root, text="Salir", command=salir)

    # Colocar los botones en la ventana
    btn_mensaje.pack(pady=10)
    btn_salir.pack(pady=10)

    # Iniciar el bucle principal
    root.mainloop()

if __name__ == "__main__":
    crear_interfaz_con_dos_botones()
