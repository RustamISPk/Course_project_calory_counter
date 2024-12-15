from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton


class LeftMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.close_menu_button = None
        self.user_settings_button = None
        self.add_recipe_button = None
        self.add_product_button = None
        self.my_weight_button = None
        self.food_diary_button = None
        self.verticalLayout = None
        self.setupUi(parent)

    def setupUi(self, parent):
        self.setGeometry(QtCore.QRect(0, 0, 251, 241))

        self.verticalLayout = QVBoxLayout(self)

        self.food_diary_button = QPushButton("Дневник питания", self)
        self.food_diary_button.clicked.connect(lambda: parent.switch_form('food_diary'))
        self.verticalLayout.addWidget(self.food_diary_button)

        self.my_weight_button = QPushButton("Мой вес", self)
        self.my_weight_button.clicked.connect(lambda: parent.switch_form('user_weight'))
        self.verticalLayout.addWidget(self.my_weight_button)

        self.add_product_button = QPushButton("Добавить продукт", self)
        self.add_product_button.clicked.connect(lambda: parent.switch_form('add_product'))
        self.verticalLayout.addWidget(self.add_product_button)

        self.add_recipe_button = QPushButton("Добавить рецепт", self)
        self.add_recipe_button.clicked.connect(lambda: parent.switch_form('add_recipe'))
        self.verticalLayout.addWidget(self.add_recipe_button)

        self.user_settings_button = QPushButton("Настройки пользователя", self)
        self.user_settings_button.clicked.connect(lambda: parent.switch_form('user_settings'))
        self.verticalLayout.addWidget(self.user_settings_button)

        self.close_menu_button = QPushButton("Закрыть меню", self)
        self.close_menu_button.clicked.connect(lambda: parent.hide_left_menu())
        self.verticalLayout.addWidget(self.close_menu_button)

