from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QStatusBar
from database_connection import DatabaseConnection


class AuthForm(QWidget):
    def __init__(self, mainwindow):
        super().__init__()
        self.statusbar = None
        self.auth_confirm_button = None
        self.password_line_edit = None
        self.login_line_edit = None
        self.auth_back_button = None
        self.setupUi(mainwindow)

    def setupUi(self, mainwindow):
        self.setObjectName("AuthFormWidget")
        self.resize(1380, 867)

        self.auth_back_button = QPushButton(self)
        self.auth_back_button.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.auth_back_button.setObjectName("auth_back_button")
        self.auth_back_button.setText("Назад")
        self.auth_back_button.clicked.connect(lambda: self.back_to_mainwindow(mainwindow))

        self.login_line_edit = QLineEdit(self)
        self.login_line_edit.setMaxLength(45)
        self.login_line_edit.setGeometry(QtCore.QRect(530, 320, 311, 41))
        self.login_line_edit.setObjectName("login_line_edit")
        self.login_line_edit.setPlaceholderText('Введите логин')

        self.password_line_edit = QLineEdit(self)
        self.password_line_edit.setMaxLength(45)
        self.password_line_edit.setGeometry(QtCore.QRect(530, 370, 311, 41))
        self.password_line_edit.setObjectName("password_line_edit")
        self.password_line_edit.setPlaceholderText('Введите пароль')
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        self.auth_confirm_button = QPushButton(self)
        self.auth_confirm_button.setGeometry(QtCore.QRect(610, 450, 151, 81))
        self.auth_confirm_button.setObjectName("auth_confirm_button")
        self.auth_confirm_button.setText('Войти')
        self.auth_confirm_button.clicked.connect(lambda: self.auth_user(mainwindow))

    def back_to_mainwindow(self, mainwindow):
        try:
            mainwindow.forms_switch('auth_back')
            self.clear_elements()
        except Exception as e:
            print(e)

    def clear_elements(self):
        self.login_line_edit.setStyleSheet("")
        self.login_line_edit.clear()
        self.login_line_edit.setPlaceholderText('Введите логин')

        self.password_line_edit.setStyleSheet("")
        self.password_line_edit.clear()
        self.password_line_edit.setPlaceholderText('Введите пароль')

    def auth_user(self, mainwindow):
        try:
            db = DatabaseConnection()
            login = self.login_line_edit.text()
            password = self.password_line_edit.text()
            checker, mainwindow.current_user_id = db.find_user_in_database(login, password)
            if checker:
                mainwindow.forms_switch('food_diary')
            else:
                self.clear_elements()
                self.login_line_edit.setStyleSheet("border: 2px solid red;")
                self.login_line_edit.setPlaceholderText('Неверный логин!')
                self.password_line_edit.setStyleSheet("border: 2px solid red;")
                self.password_line_edit.setPlaceholderText('Неверный пароль!')
        except Exception as e:
            print(e)
