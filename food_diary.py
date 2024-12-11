from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QScrollArea
from left_menu import LeftMenu
from database_connection import DatabaseConnection


class FoodDiary(QWidget):
    def __init__(self, mainwindow):
        super().__init__()
        self.main_layout = None
        self.main_widget = None
        self.scroll_area = None
        self.left_menu = None
        self.menu_button = None
        self.calory_eated = 0
        self.proein_eated = 0
        self.fats_eated = 0
        self.carbohydrates_eated = 0
        self.db = DatabaseConnection()
        self.setupUi(mainwindow)

    def setupUi(self, mainwindow):
        self.setObjectName("FoodDiaryWidget")
        self.resize(1920, 1080)

        self.left_menu = LeftMenu(self)
        self.left_menu.hide()

        self.menu_button = QPushButton(self)
        self.menu_button.setGeometry(QtCore.QRect(0, 0, 151, 81))
        self.menu_button.setObjectName("menu_button")
        self.menu_button.setText("Меню")
        self.menu_button.clicked.connect(self.show_left_menu)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setGeometry(QtCore.QRect(0, 170, 1331, 700))  # Установите нужную высоту
        self.scroll_area.setWidgetResizable(True)

        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.add_meal_section('Завтрак', 'breakfast', mainwindow)
        self.add_meal_section('Обед', 'lunch', mainwindow)
        self.add_meal_section('Ужин', 'dinner', mainwindow)

        self.scroll_area.setWidget(self.main_widget)

    def add_meal_section(self, meal_name, meal_type, mainwindow):
        meal_label = QLabel(meal_name, self)
        self.main_layout.addWidget(meal_label)

        meal_layout = QVBoxLayout()

        foods_ate = self.db.get_ate_food_by_type(mainwindow.current_user_id, meal_type)
        # print(foods_ate)
        trash = []

        for food_ate in foods_ate:
            food_data = self.db.get_product_by_id(food_ate['product_id'], food_ate['eating_id'])
            # print(food_data)
            for food in food_data:
                food['eat_id'] = food_ate['eating_id']
                food['product_count'] = food_ate['product_count']
                if food not in trash:
                    food_card_widget = QWidget()
                    vertical_layout = QVBoxLayout(food_card_widget)
                    vertical_layout.setContentsMargins(0, 0, 0, 0)

                    food_name_label = QLabel(food["product_name"])
                    vertical_layout.addWidget(food_name_label)

                    food_calory_label = QLabel(f"Калории: {int(food['calory']) * int(food['product_count'])}")
                    vertical_layout.addWidget(food_calory_label)

                    food_protein_label = QLabel(f"Белки: {food['protein']}")
                    vertical_layout.addWidget(food_protein_label)

                    food_fats_label = QLabel(f"Жиры: {food['fats']}")
                    vertical_layout.addWidget(food_fats_label)

                    food_carbohydrates_label = QLabel(f"Углеводы: {food['carbohydrates']}")
                    vertical_layout.addWidget(food_carbohydrates_label)

                    choice_food_button = QPushButton('Удалить')
                    vertical_layout.addWidget(choice_food_button)

                    meal_layout.addWidget(food_card_widget)
                    trash.append(food)
                else:
                    print('в мусорке')

        write_food_button = QPushButton('Добавить')
        write_food_button.clicked.connect(lambda: mainwindow.forms_switch(f'food_list_{meal_type}'))
        meal_layout.addWidget(write_food_button)

        self.main_layout.addLayout(meal_layout)

    def show_left_menu(self):
        self.left_menu.show()
        self.left_menu.raise_()
        self.menu_button.hide()

    def hide_left_menu(self):
        self.left_menu.hide()
        self.menu_button.show()
