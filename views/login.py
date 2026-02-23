from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFrame
# from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from pathlib import Path

class Login(QWidget):
    def __init__(self):
        super().__init__()

        # Qt ignora los estilos de fondo en subclases directas de QWidget a menos que se active esta propiedad
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # 1. Configurar la ruta de la imagen
        base_dir = Path(__file__).parent.parent 
        image_path = base_dir / "assets" / "Inicio.jpg"
        # Convertimos la ruta a un formato que el estilo entienda (usando slashes /)
        style_path = str(image_path).replace("\\", "/")

        # 2. Cargar el archivo CSS
        css_path = Path(__file__).parent / "styles" / "login.css"
        try:
            with open(css_path, "r", encoding="utf-8") as f:
                stylesheet = f.read()
            # Reemplazamos la variable en el CSS con la ruta real de la imagen
            stylesheet = stylesheet.replace("{{background_image_path}}", style_path)
            self.setStyleSheet(stylesheet)
        except Exception as e:
            print(f"Error cargando CSS: {e}")

        # 3. Crear el Layout Principal (servirá para centrar la tarjeta)
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 4. Crear "La Tarjeta" (El marco blanco que pediste)
        # Usamos un QFrame para que actúe como el contenedor flotante
        self.card = QFrame()
        self.card.setObjectName("loginCard") # Importante para que aplique el selector #loginCard del CSS
        self.card.setFixedSize(400, 500) # Tamaño fijo para que parezca una tarjeta
        
        # 5. Layout interno de la tarjeta (aquí van tus botones e inputs)
        card_layout = QVBoxLayout(self.card)
        card_layout.setContentsMargins(30, 30, 30, 30)

        # Ejemplo: Agregando un título dentro de la tarjeta
        titulo = QLabel("Agency Portal Login")
        titulo.setStyleSheet("font-size: 20px; font-weight: bold;")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Elementos
        self.label_desc = QLabel("Ingresa tus credenciales para iniciar sesión")
        self.label_email = QLabel("Correo electrónico o usuario")
        self.input_email = QLineEdit()
        self.label_pass = QLabel("Contraseña")
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn_login = QPushButton("Iniciar sesión")

        card_layout.addWidget(titulo)
        card_layout.addWidget(self.label_desc)
        card_layout.addWidget(self.label_email)
        card_layout.addWidget(self.input_email)
        card_layout.addWidget(self.label_pass)
        card_layout.addWidget(self.input_pass)
        card_layout.addWidget(self.btn_login)

        # 6. Agregar la tarjeta al layout principal
        main_layout.addWidget(self.card)