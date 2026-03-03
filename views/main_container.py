from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                               QPushButton, QLabel, QStackedWidget,
                               QFrame)
from PySide6.QtCore import Qt
from views.dashboard import Dashboard

class MainContainer(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db = db_manager
        self.setup_ui()
        
    def setup_ui(self):
        # Layout principal horizontal
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        # --- Barra Lateral (Sidebar) ---
        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(250)
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(20, 30, 20, 30)
        self.sidebar_layout.setSpacing(15)
        
        # Logo
        self.logo_label = QLabel("✈ TravelPro")
        self.logo_label.setObjectName("logo_label")
        self.sidebar_layout.addWidget(self.logo_label)
        self.sidebar_layout.addSpacing(30)
        
        # Botones de la barra lateral
        self.btn_dashboard = QPushButton("Dashboard")
        self.btn_flights = QPushButton("Available Flights")
        self.btn_bookings = QPushButton("My Bookings")
        self.btn_profile = QPushButton("Profile")
        
        # Agregamos botones a la layout usando los mismos estilos definidos en el QSS
        for btn in [self.btn_dashboard, self.btn_flights, self.btn_bookings, self.btn_profile]:
            btn.setObjectName("sidebar_btn")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            self.sidebar_layout.addWidget(btn)
        
        # Marcamos por defecto al Dashboard como la pestaña activa
        self.btn_dashboard.setProperty("active", True)
        
        self.sidebar_layout.addStretch()
        
        # Info usuario de prueba
        self.user_label = QLabel("Alex Rivera\nID: AG-9872")
        self.user_label.setObjectName("user_label")
        self.sidebar_layout.addWidget(self.user_label)
        
        self.btn_new_booking = QPushButton("+ New Booking")
        self.btn_new_booking.setObjectName("btn_primary")
        self.btn_new_booking.setCursor(Qt.CursorShape.PointingHandCursor)
        self.sidebar_layout.addWidget(self.btn_new_booking)
        
        # --- Contenido Derecho (Header + Páginas) ---
        self.right_widget = QWidget()
        self.right_layout = QVBoxLayout(self.right_widget)
        self.right_layout.setContentsMargins(0, 0, 0, 0)
        self.right_layout.setSpacing(0)
        
        # Header superior
        self.header = QFrame()
        self.header.setObjectName("header")
        self.header.setFixedHeight(70)
        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setContentsMargins(30, 0, 30, 0)
        
        # El título de la pestaña actual que irá cambiando
        self.page_title = QLabel("Dashboard")
        self.page_title.setObjectName("page_title")
        self.header_layout.addWidget(self.page_title)
        
        self.header_layout.addStretch()
        
        self.btn_notifications = QPushButton("🔔")
        self.btn_settings = QPushButton("⚙")
        self.btn_support = QPushButton("❓ Support")
        
        for btn in [self.btn_notifications, self.btn_settings, self.btn_support]:
            btn.setObjectName("header_btn")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            self.header_layout.addWidget(btn)
            
        # El QStackedWidget que contendrá las pantallas que irán cambiando
        self.content_stack = QStackedWidget()
        self.content_stack.setObjectName("content_stack")
        
        # --- Agregando las Páginas ---
        # 1. El Dashboard real que creamos
        self.dashboard_page = Dashboard(self.db)
        self.content_stack.addWidget(self.dashboard_page) # Índice 0
        
        # 2. Página temporal Vuelos
        self.flights_page = QLabel("Página de Vuelos en construcción...")
        self.flights_page.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flights_page.setObjectName("placeholder_page")
        self.content_stack.addWidget(self.flights_page) # Índice 1
        
        # 3. Página temporal Reservas
        self.bookings_page = QLabel("Página de Reservas en construcción...")
        self.bookings_page.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bookings_page.setObjectName("placeholder_page")
        self.content_stack.addWidget(self.bookings_page) # Índice 2
        
        # 4. Página temporal Perfil
        self.profile_page = QLabel("Perfil en construcción...")
        self.profile_page.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.profile_page.setObjectName("placeholder_page")
        self.content_stack.addWidget(self.profile_page) # Índice 3
        
        # Unimos Header y Stack en el lado derecho
        self.right_layout.addWidget(self.header)
        self.right_layout.addWidget(self.content_stack)
        
        # Unimos Sidebar y lado derecho
        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.right_widget)
        
        # Conectamos botones de manera que cambien el índice y el título de arriba
        self.btn_dashboard.clicked.connect(lambda: self.change_page(0, "Dashboard"))
        self.btn_flights.clicked.connect(lambda: self.change_page(1, "Available Flights"))
        self.btn_bookings.clicked.connect(lambda: self.change_page(2, "My Bookings"))
        self.btn_profile.clicked.connect(lambda: self.change_page(3, "User Profile"))
        
    def change_page(self, index, title):
        # Cambiamos página visible y titulo del Header
        self.content_stack.setCurrentIndex(index)
        self.page_title.setText(title)
        
        # Actualizamos la propiedad "active" de los botones y los recargamos
        buttons = [self.btn_dashboard, self.btn_flights, self.btn_bookings, self.btn_profile]
        for i, btn in enumerate(buttons):
            # True si es el boton que acaba de ser presionado, si no False
            btn.setProperty("active", i == index)
            
            # Repolish actualiza los estilos
            btn.style().unpolish(btn)
            btn.style().polish(btn)
