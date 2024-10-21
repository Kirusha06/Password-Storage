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


if name == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())