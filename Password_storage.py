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
