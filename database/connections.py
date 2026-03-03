# Lógica para conectar y cerrar la DB
# database/connections.py
import sqlite3
import os

from database.queries import (
    CREATE_USUARIOS_TABLE,
    COUNT_USUARIOS,
    INSERT_USUARIO,
    VERIFY_CREDENTIALS
)

class DatabaseManager:
    def __init__(self):
        # EXPLICACIÓN: Aseguramos que la carpeta database exista y nos conectamos al archivo .db
        # Si el archivo agencia.db no existe, sqlite3 lo crea automáticamente.
        db_path = os.path.join(os.path.dirname(__file__), "agencia.db")
        self.conexion = sqlite3.connect(db_path)
        self.cursor = self.conexion.cursor()
        
        # NUEVO: Crear una tabla de usuarios por defecto si no existe
        self._crear_tabla_inicial()

    def _crear_tabla_inicial(self):
        # EXPLICACIÓN: Crea la tabla y mete un usuario "admin" con clave "123" para que puedas probar
        self.cursor.execute(CREATE_USUARIOS_TABLE)
        
        # Insertar usuario de prueba solo si la tabla está vacía
        self.cursor.execute(COUNT_USUARIOS)
        if self.cursor.fetchone()[0] == 0:
            self.cursor.execute(INSERT_USUARIO, ("admin", "123"))
            self.conexion.commit()

    def verificar_credenciales(self, usuario, password):
        # EXPLICACIÓN: Busca en la base de datos si existe la combinación exacta
        self.cursor.execute(VERIFY_CREDENTIALS, (usuario, password))
        
        resultado = self.cursor.fetchone()
        
        # Si resultado tiene datos, retorna True (existe). Si es None, retorna False.
        return resultado is not None