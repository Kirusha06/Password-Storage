class PasswordStorageApp(QWidget):
    def init(self, master_password):
        super().init()
        self.master_password = master_password
        self.password_manager = PasswordManager()  # Менеджер для хранения паролей
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Password Storage by HSE")
        self.setGeometry(100, 100, 500, 400)
        self.setWindowIcon(QIcon("path_to_icon.png"))  # Можно добавить свой значок для приложения
# Устанавливаем стили для окна с цветом #5d8bb8
        self.setStyleSheet("""
            QWidget {
                background-color: #e6f7ff;
            }
            QLabel {
                color: #333;
                font-size: 15px;
                font-weight: bold;
            }
            QLineEdit {
                padding: 10px;
                border: 2px solid #5d8bb8;
                border-radius: 5px;
                font-size: 14px;
                background-color: #ffffff;
                transition: all 0.3s ease-in-out;
            }
            QLineEdit:focus {
                border-color: #5d8bb8;
            }
            QPushButton {
                background-color: #5d8bb8;
                color: white;
                font-size: 16px;
                padding: 12px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
            }
            QPushButton:hover {
                background-color: #4a7498;
            }
            QTableWidget {
                background-color: #ffffff;
                color: #333;
                font-size: 14px;
                border: 2px solid #5d8bb8;
                border-radius: 5px;
            }
            QHeaderView::section {
                background-color: #5d8bb8;
                color: white;
                padding: 4px;
                font-size: 14px;
            }
        """)
