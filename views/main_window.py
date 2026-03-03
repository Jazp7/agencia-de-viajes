# views/main_window.py
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QLabel
from PySide6.QtCore import Qt
from views.login import Login
from views.dashboard import Dashboard

class MainWindow(QMainWindow):
    # NUEVO: Ahora el constructor recibe el db_manager que le manda main.py
    def __init__(self, db_manager):
        super().__init__()
        
        self.db = db_manager # Guardamos la referencia de la DB

        self.setWindowTitle("Agencia de Viajes")
        self.resize(1080, 720)

        # NUEVO: En lugar de un QVBoxLayout estático, usamos QStackedWidget (El mazo de cartas)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # NUEVO: Instanciamos el Login y le pasamos la base de datos
        self.pantalla_login = Login(self.db)
        
        # NUEVO: Añadimos el login como la primera "carta" del mazo (índice 0)
        self.stack.addWidget(self.pantalla_login)

        # EXPLICACIÓN: Aquí escuchamos el "grito" (Signal) del login. 
        # Si el login es exitoso, ejecutamos la función mostrar_dashboard
        self.pantalla_login.login_exitoso.connect(self.mostrar_dashboard)

    def mostrar_dashboard(self):
        # EXPLICACIÓN: Esta función se ejecuta solo si las credenciales fueron correctas.
        from views.main_container import MainContainer
        
        # Instanciamos el contenedor principal (que tiene sidebar, header y páginas)
        self.main_app_view = MainContainer(self.db)

        # Añadimos el dashboard principal al mazo (índice 1) y lo ponemos a la vista
        self.stack.addWidget(self.main_app_view)
        self.stack.setCurrentWidget(self.main_app_view)

    def closeEvent(self, event):
        print("Cerrando aplicación...")
        QApplication.quit()
        event.accept()