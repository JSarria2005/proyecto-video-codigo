import tkinter as tk
from tkinter import ttk

class ProductoVista:

    def __init__(self, root, controlador):
        self.controlador = controlador
        self.root = root
        self.root.title("Gestión de Productos")

        # Campos
        tk.Label(root, text="Nombre").grid(row=0, column=0)
        self.nombre = tk.Entry(root)
        self.nombre.grid(row=0, column=1)

        tk.Label(root, text="Precio").grid(row=1, column=0)
        self.precio = tk.Entry(root)
        self.precio.grid(row=1, column=1)

        tk.Label(root, text="Cantidad").grid(row=2, column=0)
        self.cantidad = tk.Entry(root)
        self.cantidad.grid(row=2, column=1)

        # Botones
        tk.Button(root, text="Agregar", command=self.agregar).grid(row=3, column=0)
        tk.Button(root, text="Actualizar", command=self.actualizar).grid(row=3, column=1)
        tk.Button(root, text="Eliminar", command=self.eliminar).grid(row=3, column=2)

        # Tabla
        self.tabla = ttk.Treeview(root, columns=("ID", "Nombre", "Precio", "Cantidad"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Precio", text="Precio")
        self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.grid(row=4, column=0, columnspan=3)

        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        self.cargar_datos()

    def cargar_datos(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for producto in self.controlador.obtener_productos():
            self.tabla.insert("", "end", values=producto)

    def seleccionar(self, event):
        item = self.tabla.selection()[0]
        valores = self.tabla.item(item, "values")

        self.id_seleccionado = valores[0]

        self.nombre.delete(0, tk.END)
        self.nombre.insert(0, valores[1])

        self.precio.delete(0, tk.END)
        self.precio.insert(0, valores[2])

        self.cantidad.delete(0, tk.END)
        self.cantidad.insert(0, valores[3])

    def agregar(self):
        self.controlador.agregar_producto(
            self.nombre.get(),
            float(self.precio.get()),
            int(self.cantidad.get())
        )
        self.cargar_datos()

    def actualizar(self):
        self.controlador.actualizar_producto(
            self.id_seleccionado,
            self.nombre.get(),
            float(self.precio.get()),
            int(self.cantidad.get())
        )
        self.cargar_datos()

    def eliminar(self):
        self.controlador.eliminar_producto(self.id_seleccionado)
        self.cargar_datos()