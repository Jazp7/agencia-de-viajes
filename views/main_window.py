from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from login import Login

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.resize(1080, 720)

        self.central = QWidget()
        self.setCentralWidget(self.central)

        self.layout = QVBoxLayout()
        self.central.setLayout(self.layout)

        login = Login()
        self.layout.addWidget(login)

    def closeEvent(self, event):
        print("Cerrando aplicación...")
        QApplication.quit()
        event.accept()


