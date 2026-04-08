import tkinter as tk
from base_datos import crear_tabla
from controladores.producto_controlador import ProductoControlador
from vistas.producto_vista import ProductoVista

def main():
    crear_tabla()

    root = tk.Tk()
    controlador = ProductoControlador()
    app = ProductoVista(root, controlador)

    root.mainloop()

if __name__ == "__main__":
    main()