from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class LeftMenu(QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.setupUi(mainwindow)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(693, 503)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 251, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.food_diary_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.food_diary_button.setObjectName("food_diary_button")
        self.verticalLayout.addWidget(self.food_diary_button)
        self.my_weight_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.my_weight_button.setObjectName("my_weight_button")
        self.verticalLayout.addWidget(self.my_weight_button)
        self.add_product_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_product_button.setObjectName("add_product_button")
        self.verticalLayout.addWidget(self.add_product_button)
        self.add_recipe_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_recipe_button.setObjectName("add_recipe_button")
        self.verticalLayout.addWidget(self.add_recipe_button)
        self.user_settings_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.user_settings_button.setObjectName("user_settings_button")
        self.verticalLayout.addWidget(self.user_settings_button)
        self.close_menu_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.close_menu_button.setObjectName("close_menu_button")
        self.verticalLayout.addWidget(self.close_menu_button)

