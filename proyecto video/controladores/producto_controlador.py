from modelos.producto_modelo import ProductoModelo

class ProductoControlador:

    def __init__(self):
        self.modelo = ProductoModelo()

    def obtener_productos(self):
        return self.modelo.obtener_todos()

    def agregar_producto(self, nombre, precio, cantidad):
        self.modelo.insertar(nombre, precio, cantidad)

    def actualizar_producto(self, id, nombre, precio, cantidad):
        self.modelo.actualizar(id, nombre, precio, cantidad)

    def eliminar_producto(self, id):
        self.modelo.eliminar(id)