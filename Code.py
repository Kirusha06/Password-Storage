import sys
import random
import string
import json
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox,
                             QTableWidget, QTableWidgetItem, QHeaderView, QInputDialog)
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon
from PyQt5.QtCore import Qt

# Функция для генерации паролей
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Менеджер паролей для сохранения и загрузки
class PasswordManager:
    def __init__(self, filename='passwords.json'):
        self.filename = filename
        self.passwords = self.load_passwords()

    def load_passwords(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                if isinstance(data, dict):  # Проверяем, что данные — это словарь
                    return data
                else:
                    return {}  # Если это не словарь, возвращаем пустой словарь
        except FileNotFoundError:
            return {}

    def save_passwords(self):
        with open(self.filename, 'w') as f:
            json.dump(self.passwords, f)

    def add_password(self, service, username, password):
        self.passwords[service] = {"username": username, "password": password}
        self.save_passwords()

class PasswordStorageApp(QWidget):
    def __init__(self, master_password):
        super().__init__()
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

        # Таблица для отображения паролей
        self.password_table = QTableWidget(self)
        self.password_table.setColumnCount(3)
        self.password_table.setHorizontalHeaderLabels(["Сервис", "Логин", "Пароль"])
        self.password_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Поле поиска
        self.search_label = QLabel("Поиск по сервису:")
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Введите название сервиса для поиска")
        self.search_input.textChanged.connect(self.search_service)

        # Кнопка для добавления нового сервиса
        self.add_button = QPushButton("Добавить сервис")
        self.add_button.clicked.connect(self.add_service)

        # Основная компоновка
        layout = QVBoxLayout()
        layout.addWidget(self.search_label)
        layout.addWidget(self.search_input)
        layout.addWidget(self.password_table)
        layout.addWidget(self.add_button)

        self.setLayout(layout)
        self.load_passwords()

    def load_passwords(self):
        # Загрузка паролей в таблицу
        self.password_table.setRowCount(0)
        for service, data in self.password_manager.passwords.items():
            self.add_to_table(service, data['username'], data['password'])

    def add_service(self):
        service, ok = QInputDialog.getText(self, 'Новый сервис', 'Введите название сервиса:')
        if ok and service:
            username, ok2 = QInputDialog.getText(self, 'Логин', 'Введите логин:')
            if ok2 and username:
                password, ok3 = QInputDialog.getText(self, 'Пароль', 'Введите пароль (или оставьте пустым для генерации):')
                if ok3:
                    if not password:
                        password = generate_password()
                    self.password_manager.add_password(service, username, password)
                    self.add_to_table(service, username, password)

    def add_to_table(self, service, username, password):
        row = self.password_table.rowCount()
        self.password_table.insertRow(row)
        self.password_table.setItem(row, 0, QTableWidgetItem(service))
        self.password_table.setItem(row, 1, QTableWidgetItem(username))
        self.password_table.setItem(row, 2, QTableWidgetItem(password))

    def search_service(self):
        search_term = self.search_input.text().lower()
        filtered_data = {s: u for s, u in self.password_manager.passwords.items() if search_term in s.lower()}
        self.update_table(filtered_data)

    def update_table(self, data):
        self.password_table.setRowCount(0)
        for service, info in data.items():
            self.add_to_table(service, info["username"], info["password"])


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Вход в систему")
        self.setGeometry(100, 100, 300, 200)

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
        """)

        self.password_label = QLabel("Введите мастер-пароль:")
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Введите мастер-пароль")

        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.check_password)

        layout = QVBoxLayout()
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_password(self):
        entered_password = self.password_input.text()
        if entered_password == "master123":  # Мастер-пароль можно заменить на более сложный
            self.open_main_app(entered_password)
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный мастер-пароль!")

    def open_main_app(self, master_password):
        self.main_app = PasswordStorageApp(master_password)
        self.main_app.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
