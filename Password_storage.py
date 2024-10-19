я тогда беру 126-188 строки 

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
