import tkinter as tk
from tkinter import messagebox
import subprocess
import time
import os

def esperar_archivo(ruta_archivo, tiempo_espera=1, max_intentos=10):
    intentos = 0
    while not os.path.exists(ruta_archivo):
        intentos += 1
        if intentos >= max_intentos:
            raise TimeoutError(f"El archivo {ruta_archivo} no se encontró después de {max_intentos} intentos.")
        time.sleep(tiempo_espera)

def crear_interfaz_con_dos_botones():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Proyectos 42")
    root.geometry("600x400")

    # Funciones de los botones
    def minishell():
        try:
            subprocess.Popen(['gnome-terminal', '--', 'make', '-C', '/root/Desktop/minishell/'])
            esperar_archivo('/root/Desktop/minishell/minishell')

            subprocess.Popen(['gnome-terminal', '--', '/root/Desktop/minishell/minishell'])
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
