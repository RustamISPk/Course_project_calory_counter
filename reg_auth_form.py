from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class RegAuthForm(QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.centralwidget = None
        self.login_button = None
        self.registration_button = None
        self.statusbar = None
        self.setupUi(mainwindow)

    def setupUi(self, mainwindow):
        # mainwindow.setObjectName("MainWindow")
        # mainwindow.resize(1379, 867)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(610, 290, 171, 81))
        self.login_button.setObjectName("login_button")
        self.login_button.setText('Войти')
        self.registration_button = QtWidgets.QPushButton(self.centralwidget)
        self.registration_button.setGeometry(QtCore.QRect(610, 390, 171, 81))
        self.registration_button.setObjectName("registration_button")
        self.registration_button.setText('Регистрация')
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)
        self.setCentralWidget(self.centralwidget)
