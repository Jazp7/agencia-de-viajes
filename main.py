import sys
from PySide6.QtWidgets import QApplication
# Importamos las vistas desde el paquete 'views'
from views.main_window import MainWindow

def start_app():
    # 1. Crear la instancia de la aplicación (el motor)
    app = QApplication(sys.argv)
    
    # 2. Configuración global (opcional)
    app.setStyle("Fusion") 

    # 3. Instanciar la ventana principal
    # Aquí es donde en el futuro crearás la conexión a la DB 
    # y se la pasarás a MainWindow(db_connection)
    window = MainWindow()
    
    # 4. Mostrar la interfaz
    window.showMaximized()

    # 5. Cerrar el script correctamente al salir
    sys.exit(app.exec())

if __name__ == "__main__":
    start_app()