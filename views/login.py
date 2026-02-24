# views/login.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFrame
from PySide6.QtCore import Qt, Signal # NUEVO: Importamos Signal
from pathlib import Path

class Login(QWidget):
    # NUEVO: Creamos el "grito" o evento personalizado. Debe declararse a nivel de clase.
    login_exitoso = Signal()

    # NUEVO: Recibimos el db_manager en el constructor
    def __init__(self, db_manager):
        super().__init__()
        
        self.db = db_manager # Guardamos la herramienta para consultar datos

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
        card_layout.setSpacing(15)  # Agregar espaciado entre elementos

        # Agregar emoji de avión antes del título
        self.emoji_label = QLabel("✈️")
        self.emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emoji_label.setObjectName("emojiLabel")
        card_layout.addWidget(self.emoji_label)

        # Ejemplo: Agregando un título dentro de la tarjeta
        titulo = QLabel("Agency Portal Login")
        titulo.setObjectName("titulo")  # Para aplicar estilos específicos en CSS
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Elementos
        self.label_desc = QLabel("Ingresa tus credenciales para iniciar sesión")
        self.label_desc.setObjectName("descripcion")
        self.label_desc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_email = QLabel("Correo electrónico o usuario")
        self.label_email.setObjectName("labelEmail")

        self.input_email = QLineEdit()
        self.input_email.setObjectName("inputEmail")
        self.input_email.setMinimumHeight(50)

        self.label_pass = QLabel("Contraseña")
        self.label_pass.setObjectName("labelPass")

        self.input_pass = QLineEdit()
        self.input_pass.setObjectName("inputPass")
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_pass.setMinimumHeight(50)
        
        self.btn_login = QPushButton("Iniciar sesión")
        self.btn_login.setObjectName("btnLogin")
        self.btn_login.setMinimumHeight(70)  # Hacer el botón más alto para que el texto se vea bien

        card_layout.addWidget(titulo)
        card_layout.addWidget(self.label_desc)
        card_layout.addWidget(self.label_email)
        card_layout.addWidget(self.input_email)
        card_layout.addWidget(self.label_pass)
        card_layout.addWidget(self.input_pass)
        card_layout.addWidget(self.btn_login)

        # 6. Agregar la tarjeta al layout principal
        main_layout.addWidget(self.card)

        # NUEVO: 7. Conectamos el clic del botón a nuestra nueva función de validación
        self.btn_login.clicked.connect(self.intentar_login)

    # NUEVO: Método que se ejecuta al presionar el botón
    def intentar_login(self):
        # Obtenemos el texto que escribió el usuario
        usuario_ingresado = self.input_email.text()
        password_ingresado = self.input_pass.text()

        # Le preguntamos al Archivista (la base de datos) si los datos son correctos
        if self.db.verificar_credenciales(usuario_ingresado, password_ingresado):
            # ¡Éxito! Emitimos la señal para que main_window cambie la pantalla
            self.login_exitoso.emit()
        else:
            # Error visual: Cambiamos el texto de la descripción y lo ponemos en rojo
            self.label_desc.setText("Usuario o contraseña incorrectos")
            self.label_desc.setStyleSheet("color: red; font-weight: bold;")
            
            # Limpiamos el campo de contraseña para que vuelva a intentar
            self.input_pass.clear()