from base_datos import conectar

class ProductoModelo:

    def obtener_todos(self):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()
        conexion.close()
        return datos

    def insertar(self, nombre, precio, cantidad):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, precio, cantidad) VALUES (?, ?, ?)",
            (nombre, precio, cantidad)
        )
        conexion.commit()
        conexion.close()

    def actualizar(self, id, nombre, precio, cantidad):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE productos SET nombre=?, precio=?, cantidad=? WHERE id=?",
            (nombre, precio, cantidad, id)
        )
        conexion.commit()
        conexion.close()

    def eliminar(self, id):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id=?", (id,))
        conexion.commit()
        conexion.close()