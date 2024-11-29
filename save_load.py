class PasswordManager:
    def init(self, filename='passwords.json'):
        self.filename = filename
        self.passwords = self.load_passwords()
