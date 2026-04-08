import sqlite3

def conectar():
    return sqlite3.connect("productos.db")

def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL,
            cantidad INTEGER
        )
    """)
    conexion.commit()
    conexion.close()