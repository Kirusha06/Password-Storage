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