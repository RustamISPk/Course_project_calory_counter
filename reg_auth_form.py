from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget


class RegAuthForm(QWidget):
    def __init__(self, mainwindow):
        super().__init__()
        self.centralwidget = None
        self.login_button = None
        self.registration_button = None
        self.statusbar = None
        self.setupUi(mainwindow)

    def setupUi(self, mainwindow):
        self.centralwidget = QWidget(self)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.centralwidget.setObjectName("centralwidget")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(860, 340, 200, 100))
        self.login_button.setObjectName("login_button")
        self.login_button.setText('Войти')
        self.login_button.clicked.connect(lambda: mainwindow.forms_switch('auth'))
        self.registration_button = QtWidgets.QPushButton(self.centralwidget)
        self.registration_button.setGeometry(QtCore.QRect(860, 460, 200, 100))
        self.registration_button.setObjectName("registration_button")
        self.registration_button.setText('Регистрация')
        self.registration_button.clicked.connect(lambda: mainwindow.forms_switch('reg'))



