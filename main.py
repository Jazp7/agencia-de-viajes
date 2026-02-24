# main.py
import sys
from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow

# NUEVO: Importamos nuestra clase manejadora de la base de datos
from database.connections import DatabaseManager

def start_app():
    app = QApplication(sys.argv)
    
    # Configuración global (opcional)
    app.setStyle("Fusion")

    # NUEVO: 1. Creamos la conexión a la base de datos (El Archivista)
    db = DatabaseManager()

    # NUEVO: 2. Le pasamos esa conexión a la ventana principal (El Escenario)
    window = MainWindow(db)
    window.showMaximized()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    start_app()