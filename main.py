import sys
from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow

# NUEVO: Importamos nuestra clase manejadora de la base de datos
from database.connections import DatabaseManager

STYLESHEET = """
QMainWindow {
    background-color: #f5f6fa;
}

#sidebar {
    background-color: #ffffff;
    border-right: 1px solid #dcdde1;
}

#logo_label {
    font-size: 24px;
    font-weight: bold;
    color: #2f3640;
}

#sidebar_btn {
    text-align: left;
    padding: 12px 15px;
    border: none;
    border-radius: 6px;
    font-size: 15px;
    color: #718093;
    background-color: transparent;
}

#sidebar_btn:hover {
    background-color: #f5f6fa;
    color: #0097e6;
}

#sidebar_btn[active="true"] {
    background-color: #e3f2fd;
    color: #0097e6;
    font-weight: bold;
}

#user_label {
    font-size: 13px;
    color: #2f3640;
    margin-bottom: 15px;
}

#btn_primary, #btn_qa_primary {
    background-color: #00a8ff;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 12px;
    font-size: 14px;
    font-weight: bold;
}

#btn_primary:hover, #btn_qa_primary:hover {
    background-color: #0097e6;
}

#header {
    background-color: #ffffff;
    border-bottom: 1px solid #dcdde1;
}

#page_title {
    font-size: 20px;
    font-weight: bold;
    color: #2f3640;
}

#header_btn {
    border: none;
    background-color: transparent;
    font-size: 16px;
    color: #718093;
    padding: 8px;
}

#header_btn:hover {
    color: #2f3640;
}

#content_stack {
    background-color: #f5f6fa;
}

#placeholder_page {
    font-size: 24px;
    color: #7f8fa6;
}

/* Dashboard specific elements */
#stat_card, #mock_card {
    background-color: #ffffff;
    border-radius: 10px;
    border: 1px solid #dcdde1;
    padding: 20px;
}

#stat_title, #mock_title {
    color: #7f8fa6;
    font-size: 14px;
    font-weight: bold;
}

#stat_value {
    color: #2f3640;
    font-size: 26px;
    font-weight: bold;
    margin: 10px 0;
}

#stat_subtitle {
    font-size: 12px;
}

#section_title {
    color: #7f8fa6;
    font-size: 13px;
    font-weight: bold;
    margin-top: 10px;
}

#btn_qa_secondary {
    background-color: #ffffff;
    color: #2f3640;
    border: 1px solid #dcdde1;
    border-radius: 6px;
    padding: 12px 20px;
    font-size: 14px;
    font-weight: bold;
}

#btn_qa_secondary:hover {
    background-color: #f5f6fa;
}
"""

def start_app():
    app = QApplication(sys.argv)
    
    # Configuración global
    app.setStyle("Fusion")
    app.setStyleSheet(STYLESHEET)

    # Creamos la conexión a la base de datos
    db = DatabaseManager()

    # Le pasamos esa conexión a la ventana principal
    window = MainWindow(db)
    window.showMaximized()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    start_app()