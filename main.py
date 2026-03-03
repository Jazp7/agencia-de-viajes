import sys
import os
from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow

# NUEVO: Importamos nuestra clase manejadora de la base de datos
from database.connections import DatabaseManager

def start_app():
    app = QApplication(sys.argv)
    
    # Configuración global
    app.setStyle("Fusion")
    
    # Cargar los estilos desde el archivo
    style_path = os.path.join(os.path.dirname(__file__), "views", "styles", "main.css")
    with open(style_path, "r", encoding="utf-8") as file:
        app.setStyleSheet(file.read())

    # Creamos la conexión a la base de datos
    db = DatabaseManager()

    # Le pasamos esa conexión a la ventana principal
    window = MainWindow(db)
    window.showMaximized()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    start_app()