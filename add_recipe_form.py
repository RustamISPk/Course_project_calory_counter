from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QScrollArea
from database_connection import DatabaseConnection
from left_menu import LeftMenu


class AddRecipeWidget(QWidget):
    def __init__(self, mainwindow):
        super().__init__()
        self.db = DatabaseConnection()
        self.products_layout = None
        self.products_widget = None
        self.scroll_area = None
        self.foods = mainwindow.food_list_for_recipe
        self.mainwindow = mainwindow
        self.left_menu = None
        self.add_recipe_save_button = None
        self.add_recipe_line_edit = None
        self.add_recipe_product_label = None
        self.add_product_button = None
        self.add_recipe_widget = None
        self.menu_button = None
        self.setupUi(mainwindow)
        self.load_food(mainwindow)

    def setupUi(self, mainwindow):
        try:
            self.setObjectName("AddRecipeWidget")
            self.resize(1920, 1080)

            self.menu_button = QPushButton(self)
            self.menu_button.setGeometry(QtCore.QRect(0, 0, 141, 61))
            self.menu_button.setObjectName("menu_button")
            self.menu_button.setText("Меню")
            self.menu_button.clicked.connect(lambda: self.show_left_menu())

            self.left_menu = LeftMenu(self)
            self.left_menu.hide()

            self.scroll_area = QScrollArea(self)
            self.scroll_area.setGeometry(QtCore.QRect(0, 170, 1800, 700))
            self.scroll_area.setWidgetResizable(True)

            self.products_widget = QWidget(self)
            self.products_layout = QVBoxLayout(self.products_widget)
            self.products_layout.setContentsMargins(0, 0, 0, 0)

            self.scroll_area.setWidget(self.products_widget)

            self.add_recipe_line_edit = QLineEdit(self)
            self.add_recipe_line_edit.setGeometry(QtCore.QRect(70, 0, 200, 41))
            self.add_recipe_line_edit.setObjectName("add_recipe_line_edit")
            self.add_recipe_line_edit.setPlaceholderText('Введите название рецепта')
            self.products_layout.addWidget(self.add_recipe_line_edit)

            self.add_product_button = QPushButton(self)
            self.add_product_button.setGeometry(QtCore.QRect(70, 60, 200, 41))
            self.add_product_button.setObjectName("pushButton")
            self.add_product_button.setText("Добавить продукт")
            self.add_product_button.clicked.connect(lambda: self.switch_form('food_list_for_recipe'))
            self.products_layout.addWidget(self.add_product_button)

            self.add_recipe_save_button = QPushButton(self)
            self.add_recipe_save_button.setGeometry(QtCore.QRect(70, 150, 200, 41))
            self.add_recipe_save_button.setObjectName("add_recipe_save_button")
            self.add_recipe_save_button.setText("Сохранить рецепт")
            self.add_recipe_save_button.clicked.connect(lambda: self.save_recipe(mainwindow))
            self.products_layout.addWidget(self.add_recipe_save_button)

            self.add_recipe_product_label = QLineEdit(self)
            self.add_recipe_product_label.setGeometry(QtCore.QRect(80, 110, 200, 31))
            self.add_recipe_product_label.setObjectName("add_recipe_product_label")
            self.add_recipe_product_label.setText("Продукты для рецепта:")
            self.add_recipe_product_label.setReadOnly(True)
            self.products_layout.addWidget(self.add_recipe_product_label)

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

    def load_food(self, mainwindow):
        trash = []
        id = 0
        if len(self.foods) > 0:
            for food in mainwindow.food_list_for_recipe:
                id += 1
                food['id'] = id
                if food not in trash:
                    food_card_widget = QWidget()
                    food_card_widget.setFixedSize(250, 150)
                    vertical_layout = QVBoxLayout(food_card_widget)
                    vertical_layout.setContentsMargins(5, 5, 5, 5)
                    food_name_label = QLabel(food["product_name"])
                    vertical_layout.addWidget(food_name_label)

                    calory = float(food['calory']) / 100 * float(food['count'])
                    calory = round(calory)
                    food_calory_label = QLabel(f"Калории: {calory}")
                    vertical_layout.addWidget(food_calory_label)

                    protein = float(food['protein']) / 100 * float(food['count'])
                    protein = round(protein, 1)
                    food_protein_label = QLabel(f"Белки: {protein}")
                    vertical_layout.addWidget(food_protein_label)

                    fats = float(food['fats']) / 100 * float(food['count'])
                    fats = round(fats, 1)
                    food_fats_label = QLabel(f"Жиры: {fats}")
                    vertical_layout.addWidget(food_fats_label)

                    carbohydrates = float(food['carbohydrates']) / 100 * float(food['count'])
                    carbohydrates = round(carbohydrates, 1)
                    food_carbohydrates_label = QLabel(f"Углеводы: {carbohydrates}")
                    vertical_layout.addWidget(food_carbohydrates_label)

                    remove_food_button = QPushButton('Удалить')
                    remove_food_button.clicked.connect(lambda checked, widget=food_card_widget, food=food:
                                                       self.remove_food_cart(widget, food, mainwindow))
                    vertical_layout.addWidget(remove_food_button)

                    self.products_layout.addWidget(food_card_widget)
                    trash.append(food)

    def remove_food_cart(self, widget, food, mainwindow):
        try:
            mainwindow.food_list_for_recipe.remove(food)
            widget.deleteLater()
            print(mainwindow.food_list_for_recipe)
        except Exception as e:
            print(e)

    def save_recipe(self, mainwindow):
        if self.add_recipe_line_edit.text() != '':
            product = {
                'name': '',
                'calory': 0,
                'protein': 0,
                'fats': 0,
                'carbohydrate': 0,
                'type': 'recipe'
            }
            for food in mainwindow.food_list_for_recipe:
                product['name'] = self.add_recipe_line_edit.text()
                calory = float(food['calory']) / 100 * float(food['count'])
                calory = round(calory)
                product['calory'] += calory

                protein = float(food['protein']) / 100 * float(food['count'])
                protein = round(protein, 1)
                product['protein'] += protein

                fats = float(food['fats']) / 100 * float(food['count'])
                fats = round(fats, 1)
                product['fats'] += fats

                carbohydrates = float(food['carbohydrates']) / 100 * float(food['count'])
                carbohydrates = round(carbohydrates, 1)
                product['carbohydrate'] += carbohydrates

            self.db.save_product_in_database(product)
            mainwindow.food_list_for_recipe = []
            mainwindow.forms_switch('add_recipe')
        else:
            self.add_recipe_line_edit.setStyleSheet("border: 2px solid red;")
            self.add_recipe_line_edit.setPlaceholderText('Заполните поле!')
