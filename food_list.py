from PyQt5 import QtCore
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel, QFormLayout, \
    QListWidget, QListWidgetItem
from database_connection import DatabaseConnection


class FoodList(QWidget):
    def __init__(self, mainwindow, type):
        super().__init__()
        self.db = DatabaseConnection()
        self.list_item = None
        self.food_to_write_button = None
        self.food_to_write_count_line_edit = None
        self.food_to_write_name_label = None
        self.formLayout_2 = None
        self.formLayoutWidget = None
        self.food_to_write_widget = None
        self.choice_food_button = None
        self.food_carbohydrates_label = None
        self.food_fats_label = None
        self.food_protein_label = None
        self.food_calory_label = None
        self.food_name_label = None
        self.food_list_widget = None
        self.recipes_button = None
        self.products_button = None
        self.change_food_mode_widget = None
        self.find_products_line_edit = None
        self.find_products_button = None
        self.products_list_back_button = None
        self.using_type = type
        self.setupUi(mainwindow)
        foods = self.db.find_all_food()
        self.load_food(mainwindow, foods)

    def setupUi(self, mainwindow):
        self.setObjectName("FoodListWidget")
        self.resize(1920, 1080)

        self.products_list_back_button = QPushButton(self)
        self.products_list_back_button.setGeometry(QtCore.QRect(0, 10, 181, 41))
        self.products_list_back_button.setObjectName("products_list_back_button")
        if self.using_type == 'use_for_food_diary':
            self.products_list_back_button.clicked.connect(lambda: mainwindow.forms_switch('food_diary'))
        else:
            self.products_list_back_button.clicked.connect(lambda: mainwindow.forms_switch('add_recipe'))
        self.products_list_back_button.setText('Назад')

        self.find_products_button = QPushButton(self)
        self.find_products_button.setGeometry(QtCore.QRect(1718, 10, 181, 41))
        self.find_products_button.setObjectName("find_products_button")
        self.find_products_button.setText('Найти')
        self.find_products_button.clicked.connect(lambda: self.find_product_by_name(mainwindow))

        self.find_products_line_edit = QLineEdit(self)
        self.find_products_line_edit.setGeometry(QtCore.QRect(180, 10, 1538, 41))
        self.find_products_line_edit.setObjectName("find_products_line_edit")
        self.find_products_line_edit.setPlaceholderText('Введите продукт')

        self.change_food_mode_widget = QWidget(self)
        self.change_food_mode_widget.setGeometry(QtCore.QRect(0, 50, 1920, 101))
        self.change_food_mode_widget.setObjectName("change_food_mode_widget")

        self.products_button = QPushButton(self.change_food_mode_widget)
        self.products_button.setGeometry(QtCore.QRect(0, 0, 945, 101))
        self.products_button.setObjectName("products_button")
        self.products_button.setText('Продукты')
        self.products_button.clicked.connect(lambda: self.find_products(mainwindow))

        self.recipes_button = QPushButton(self.change_food_mode_widget)
        self.recipes_button.setGeometry(QtCore.QRect(950, 0, 948, 101))
        self.recipes_button.setObjectName("recipes_button")
        self.recipes_button.setText('Рецепты')
        self.recipes_button.clicked.connect(lambda: self.find_recipes(mainwindow))

        self.food_list_widget = QListWidget(self)
        self.food_list_widget.setGeometry(QtCore.QRect(170, 150, 1600, 691))
        self.food_list_widget.setObjectName("food_list_widget")

        self.food_to_write_widget = QWidget(self.food_list_widget)
        self.food_to_write_widget.setGeometry(QtCore.QRect(565, 250, 450, 110))
        self.food_to_write_widget.setObjectName("food_to_write_widget")
        self.formLayoutWidget = QWidget(self.food_to_write_widget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 400, 500))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.food_to_write_name_label = QLabel(self.formLayoutWidget)
        self.food_to_write_name_label.setObjectName("food_to_write_name_label")
        self.food_to_write_count_line_edit = QLineEdit(self.formLayoutWidget)
        self.food_to_write_count_line_edit.setObjectName("food_to_write_count_line_edit")
        self.food_to_write_count_line_edit.setFixedHeight(30)
        self.food_to_write_count_line_edit.setPlaceholderText('Количество продукта')
        self.food_to_write_count_line_edit.setVisible(True)
        self.food_to_write_count_line_edit.setValidator(QIntValidator(1, 5000, self))

        self.food_to_write_button = QPushButton(self.formLayoutWidget)
        self.food_to_write_button.setObjectName("food_to_write_button")
        self.food_to_write_button.setText('Добавить')

        self.formLayout_2.addRow(self.food_to_write_name_label)
        self.formLayout_2.addRow(self.food_to_write_count_line_edit)
        self.formLayout_2.addRow(self.food_to_write_button)

        self.food_to_write_widget.hide()

    def load_food(self, mainwindow, foods):
        # foods = self.db.find_all_food()
        if self.food_list_widget is not None and self.list_item is not None:
            self.food_list_widget.clear()
        for food in foods:
            food_card_widget = QWidget()
            food_card_widget.setGeometry(QtCore.QRect(0, 0, 1011, 111))

            vertical_layout = QVBoxLayout(food_card_widget)
            vertical_layout.setContentsMargins(0, 0, 0, 0)

            food_name_label = QLabel(food["product_name"])
            vertical_layout.addWidget(food_name_label)

            food_calory_label = QLabel(f"Калории: {food['calory']}")
            vertical_layout.addWidget(food_calory_label)

            food_protein_label = QLabel(f"Белки: {food['protein']}")
            vertical_layout.addWidget(food_protein_label)

            food_fats_label = QLabel(f"Жиры: {food['fats']}")
            vertical_layout.addWidget(food_fats_label)

            food_carbohydrates_label = QLabel(f"Углеводы: {food['carbohydrates']}")
            vertical_layout.addWidget(food_carbohydrates_label)

            choice_food_button = QPushButton('Выбрать')
            choice_food_button.clicked.connect(lambda checked, food=food: self.choose_food(food, mainwindow))
            vertical_layout.addWidget(choice_food_button)

            self.list_item = QListWidgetItem()
            self.list_item.setSizeHint(food_card_widget.sizeHint())
            self.food_list_widget.addItem(self.list_item)
            self.food_list_widget.setItemWidget(self.list_item, food_card_widget)

    def choose_food(self, food, mainwindow):
        self.food_to_write_name_label.setText(f"{food['product_name']}")
        self.food_to_write_widget.hide()
        self.food_to_write_widget.show()
        if self.using_type == 'use_for_food_diary':
            self.food_to_write_button.clicked.connect(lambda: self.write_eating(mainwindow, food))
        elif self.using_type == 'use_for_add_recipe':
            self.food_to_write_button.clicked.connect(lambda: self.for_add_recipe(mainwindow, food))
            self.products_list_back_button.clicked.connect(lambda: mainwindow.forms_switch('add_product'))

    def write_eating(self, mainwindow, food):
        try:
            if self.food_to_write_count_line_edit.text() != '':
                product_id = food['product_id']
                count = self.food_to_write_count_line_edit.text()
                eating_type = ''
                match mainwindow.eating_type:
                    case 'breakfast':
                        eating_type = 'breakfast'
                    case 'lunch':
                        eating_type = 'lunch'
                    case 'dinner':
                        eating_type = 'dinner'
                self.db.write_eating_db(user_id=mainwindow.current_user_id, product_id=product_id,
                                        product_count=count, eating_type=eating_type)
                mainwindow.forms_switch('food_diary')
        except Exception as e:
            print(e)

    def for_add_recipe(self, mainwindow, food):
        try:
            if self.food_to_write_count_line_edit.text() != '':
                product_id = food['product_id']
                count = self.food_to_write_count_line_edit.text()
                food_list_for_recipe = self.db.get_product_by_id_for_recipe(product_id)
                food_list_for_recipe[0]['count'] = count
                mainwindow.food_list_for_recipe.append(food_list_for_recipe[0])
                mainwindow.forms_switch('add_recipe')
        except Exception as e:
            print(e)

    def find_product_by_name(self, mainwindow):
        try:
            name = self.find_products_line_edit.text()
            need_food = []
            food_list = self.db.find_all_food()
            if name != '':
                for food in food_list:
                    if name.lower() in food['product_name'].lower():
                        need_food.append(food)
                self.load_food(mainwindow, need_food)
            elif name == '':
                self.load_food(mainwindow, food_list)
        except Exception as e:
            print(e)

    def find_products(self, mainwindow):
        try:
            food_list = self.db.find_products()
            self.load_food(mainwindow, food_list)
        except Exception as e:
            print(e)

    def find_recipes(self, mainwindow):
        try:
            food_list = self.db.find_recipes()
            self.load_food(mainwindow, food_list)
        except Exception as e:
            print(e)