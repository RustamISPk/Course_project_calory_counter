from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QStatusBar, QWidget


class AuthForm(QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.statusbar = None
        self.auth_confirm_button = None
        self.password_line_edit = None
        self.login_line_edit = None
        self.auth_back_button = None
        self.centralwidget = None
        self.setupUi(mainwindow)

    def setupUi(self, mainwindow):
        mainwindow.setObjectName("MainWindow")
        mainwindow.resize(1380, 867)
        self.centralwidget = QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.auth_back_button = QPushButton(self.centralwidget)
        self.auth_back_button.setGeometry(QtCore.QRect(0, 0, 131, 51))
        self.auth_back_button.setObjectName("auth_back_button")
        self.auth_back_button.setText("Назад")
        self.auth_back_button.clicked.connect(lambda: mainwindow.forms_switch('auth_back'))
        self.login_line_edit = QLineEdit(self.centralwidget)
        self.login_line_edit.setMaxLength(45)
        self.login_line_edit.setGeometry(QtCore.QRect(530, 320, 311, 41))
        self.login_line_edit.setObjectName("login_line_edit")
        self.login_line_edit.setPlaceholderText('Введите логин')
        self.password_line_edit = QLineEdit(self.centralwidget)
        self.password_line_edit.setMaxLength(45)
        self.password_line_edit.setGeometry(QtCore.QRect(530, 370, 311, 41))
        self.password_line_edit.setObjectName("password_line_edit")
        self.password_line_edit.setPlaceholderText('Введите пароль')
        self.password_line_edit.setEchoMode(QLineEdit.Password)
        self.auth_confirm_button = QPushButton(self.centralwidget)
        self.auth_confirm_button.setGeometry(QtCore.QRect(610, 450, 151, 81))
        self.auth_confirm_button.setObjectName("auth_confirm_button")
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)
        self.setCentralWidget(self.centralwidget)
