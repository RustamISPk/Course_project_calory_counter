from PyQt5 import QtCore
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit
from database_connection import DatabaseConnection
from left_menu import LeftMenu


class AddProductWidget(QWidget):
    def __init__(self, mainwindow):
        super().__init__()
        self.left_menu = None
        self.add_food_carbohydrates_line_edit = None
        self.add_food_fats_line_edit = None
        self.add_food_protein_line_edit = None
        self.add_food_calory_line_edit = None
        self.add_food_name_line_edit = None
        self.verticalLayout = None
        self.verticalLayoutWidget = None
        self.menu_button = None
        self.add_food_save_button = None
        self.mainwindow = mainwindow
        self.db = DatabaseConnection()
        self.setupUi(mainwindow)

    def setupUi(self, mainwindow):
        self.setGeometry(100, 100, 1380, 867)

        self.left_menu = LeftMenu(self)
        self.left_menu.hide()

        self.menu_button = QPushButton(self)
        self.menu_button.setGeometry(QtCore.QRect(0, 0, 121, 51))
        self.menu_button.setObjectName("menu_button")
        self.menu_button.setText('Меню')
        self.menu_button.clicked.connect(lambda: self.show_left_menu())

        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(550, 270, 231, 191)

        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.add_food_name_line_edit = QLineEdit(self)
        self.add_food_name_line_edit.setObjectName("add_food_name_line_edit")
        self.add_food_name_line_edit.setPlaceholderText('Введите название продукта')
        self.verticalLayout.addWidget(self.add_food_name_line_edit)

        self.add_food_calory_line_edit = QLineEdit(self)
        self.add_food_calory_line_edit.setObjectName("add_food_calory_line_edit")
        self.add_food_calory_line_edit.setPlaceholderText('Введите калорийность продукта')
        self.add_food_calory_line_edit.setValidator(QIntValidator(1, 999, self))
        self.verticalLayout.addWidget(self.add_food_calory_line_edit)

        self.add_food_protein_line_edit = QLineEdit(self)
        self.add_food_protein_line_edit.setObjectName("add_food_protein_line_edit")
        self.add_food_protein_line_edit.setPlaceholderText('Введите количество белка в продукте')
        self.add_food_protein_line_edit.setValidator(QDoubleValidator(0.0, 100.0, 2, self))
        self.add_food_protein_line_edit.setMaxLength(4)
        self.verticalLayout.addWidget(self.add_food_protein_line_edit)

        self.add_food_fats_line_edit = QLineEdit(self)
        self.add_food_fats_line_edit.setObjectName("add_food_fats_line_edit")
        self.add_food_fats_line_edit.setPlaceholderText('Введите количество жиров в продукте')
        self.add_food_fats_line_edit.setValidator(QDoubleValidator(0.0, 100.0, 2, self))
        self.add_food_fats_line_edit.setMaxLength(4)
        self.verticalLayout.addWidget(self.add_food_fats_line_edit)

        self.add_food_carbohydrates_line_edit = QLineEdit(self)
        self.add_food_carbohydrates_line_edit.setObjectName("add_food_carbohydrates_line_edit")
        self.add_food_carbohydrates_line_edit.setPlaceholderText('Введите количество углеводов в продукте')
        self.add_food_carbohydrates_line_edit.setValidator(QDoubleValidator(0.0, 100.0, 2, self))
        self.add_food_carbohydrates_line_edit.setMaxLength(4)
        self.verticalLayout.addWidget(self.add_food_carbohydrates_line_edit)

        self.add_food_save_button = QPushButton(self)
        self.add_food_save_button.setObjectName("add_food_save_button")
        self.add_food_save_button.setText('Сохранить')
        self.add_food_save_button.clicked.connect(lambda: self.write_food())
        self.verticalLayout.addWidget(self.add_food_save_button)

    def write_food(self):
        try:
            product = {
                'name': '',
                'calory': '',
                'protein': '',
                'fats': '',
                'carbohydrate': ''
            }
            elements = [self.add_food_name_line_edit, self.add_food_calory_line_edit, self.add_food_protein_line_edit,
                        self.add_food_fats_line_edit, self.add_food_carbohydrates_line_edit]
            product_name = self.add_food_name_line_edit.text()
            product_calory = self.add_food_calory_line_edit.text()
            product_protein = self.add_food_protein_line_edit.text()
            product_fats = self.add_food_fats_line_edit.text()
            product_carbohydrate = self.add_food_carbohydrates_line_edit.text()
            if product_name != '' and product_calory != '' and product_protein != '' and product_fats != '' and product_carbohydrate != '':
                product['name'] = product_name
                product['calory'] = product_calory
                product['protein'] = product_protein.replace(',', '.')
                product['fats'] = product_fats.replace(',', '.')
                product['carbohydrate'] = product_carbohydrate.replace(',', '.')
                self.db.save_product_in_database(product)
                for element in elements:
                    element.clear()
                    element.setStyleSheet("")
                self.add_food_name_line_edit.setPlaceholderText('Введите название продукта')
                self.add_food_calory_line_edit.setPlaceholderText('Введите калорийность продукта')
                self.add_food_protein_line_edit.setPlaceholderText('Введите количество белка в продукте')
                self.add_food_fats_line_edit.setPlaceholderText('Введите количество жиров в продукте')
                self.add_food_carbohydrates_line_edit.setPlaceholderText('Введите количество углеводов в продукте')
            else:
                for element in elements:
                    if element.text() == '':
                        element.setStyleSheet("border: 2px solid red;")
                        element.setPlaceholderText('Заполните поле!')
        except Exception as e:
            print(e)

    def show_left_menu(self):
        self.left_menu.show()
        self.left_menu.raise_()
        self.menu_button.hide()

    def hide_left_menu(self):
        self.left_menu.hide()
        self.menu_button.show()

    def switch_form(self, case):
        self.mainwindow.forms_switch(case)
