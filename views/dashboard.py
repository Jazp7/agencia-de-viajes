from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                               QLabel, QFrame, QPushButton)
from PySide6.QtCore import Qt

class Dashboard(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db = db_manager
        self.setup_ui()
        
    def setup_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(30, 30, 30, 30)
        self.main_layout.setSpacing(20)
        
        # Fila de estadísticas (Tarjetas superiores)
        self.stats_layout = QHBoxLayout()
        self.stats_layout.setSpacing(20)
        
        # Añadiento mini cuadros
        self.stats_layout.addWidget(self.create_stat_card("Total Spent", "$12,480.00", "+12% from last month", "#00b894", "💵"))
        self.stats_layout.addWidget(self.create_stat_card("Upcoming Trips", "3 Bookings", "Next: Oct 25 to London", "#0984e3", "📅"))
        self.stats_layout.addWidget(self.create_stat_card("Loyalty Points", "45,200 pts", "Gold Tier Member", "#e17055", "⭐"))
        
        self.main_layout.addLayout(self.stats_layout)
        
        # Quick Actions
        self.quick_actions_label = QLabel("QUICK ACTIONS")
        self.quick_actions_label.setObjectName("section_title")
        self.main_layout.addWidget(self.quick_actions_label)
        
        self.qa_layout = QHBoxLayout()
        btn_book = QPushButton("✈ Book a Flight")
        btn_book.setObjectName("btn_qa_primary")
        btn_book.setCursor(Qt.CursorShape.PointingHandCursor)
        
        btn_status = QPushButton("🔍 Check Status")
        btn_status.setObjectName("btn_qa_secondary")
        btn_status.setCursor(Qt.CursorShape.PointingHandCursor)
        
        btn_hotels = QPushButton("🏨 Find Hotels")
        btn_hotels.setObjectName("btn_qa_secondary")
        btn_hotels.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.qa_layout.addWidget(btn_book)
        self.qa_layout.addWidget(btn_status)
        self.qa_layout.addWidget(btn_hotels)
        self.qa_layout.addStretch()
        self.qa_layout.setSpacing(15)
        
        self.main_layout.addLayout(self.qa_layout)
        
        # Fila inferior (Tablas grandes, calendarios, etc.)
        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setSpacing(20)
        
        calendar_widget = self.create_mock_card("Travel Calendar", "Oct 25: Business Trip London\nNov 10: Vacations Paris\nDec 24: Miami Family")
        activity_widget = self.create_mock_card("Recent Activity", "• Searched for flights to Tokyo\n   Departing Jan 15 - 2 hours ago\n\n• Booking Confirmed: SFO to LHR\n   Order #TR-5521 - Yesterday, 4:30 PM\n\n• Earned 1,200 Loyalty Points\n   Bonus from London Trip - 2 days ago")
        
        # Darle el doble de ancho visual a Activity en comparación a Calendar (stretch factors)
        self.bottom_layout.addWidget(calendar_widget, 1)
        self.bottom_layout.addWidget(activity_widget, 2)
        
        self.main_layout.addLayout(self.bottom_layout)
        self.main_layout.addStretch() # Empuja el resto hacia arriba
        
    def create_stat_card(self, title, value, subtitle, color, icon):
        card = QFrame()
        card.setObjectName("stat_card")
        layout = QVBoxLayout(card)
        
        top_layout = QHBoxLayout()
        title_label = QLabel(title)
        title_label.setObjectName("stat_title")
        icon_label = QLabel(icon)
        icon_label.setStyleSheet(f"color: {color}; font-size: 20px;")
        
        top_layout.addWidget(title_label)
        top_layout.addStretch()
        top_layout.addWidget(icon_label)
        layout.addLayout(top_layout)
        
        val_label = QLabel(value)
        val_label.setObjectName("stat_value")
        layout.addWidget(val_label)
        
        sub_label = QLabel(subtitle)
        sub_label.setObjectName("stat_subtitle")
        sub_label.setStyleSheet(f"color: {color};")
        layout.addWidget(sub_label)
        
        return card
        
    def create_mock_card(self, title, content):
        card = QFrame()
        card.setObjectName("mock_card")
        layout = QVBoxLayout(card)
        
        title_label = QLabel(title)
        title_label.setObjectName("mock_title")
        layout.addWidget(title_label)
        
        content_label = QLabel(content)
        content_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        content_label.setStyleSheet("color: #636e72; font-size: 14px; line-height: 1.5; margin-top: 10px;")
        layout.addWidget(content_label)
        
        return card