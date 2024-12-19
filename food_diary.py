from datetime import datetime

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QScrollArea
from left_menu import LeftMenu
from database_connection import DatabaseConnection


class FoodDiary(QWidget):
    def __init__(self, mainwindow):
        super().__init__()
        self.calory_counter_label = None
        self.main_layout = None
        self.main_widget = None
        self.scroll_area = None
        self.left_menu = None
        self.menu_button = None
        self.calory_eated = 0
        self.proein_eated = 0
        self.fats_eated = 0
        self.mainwindow = mainwindow
        self.carbohydrates_eated = 0
        self.db = DatabaseConnection()
        self.count_calory(mainwindow)
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
        self.scroll_area.setGeometry(QtCore.QRect(0, 170, 1850, 600))
        self.scroll_area.setWidgetResizable(True)

        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.add_meal_section('Завтрак', 'breakfast', mainwindow)
        self.add_meal_section('Обед', 'lunch', mainwindow)
        self.add_meal_section('Ужин', 'dinner', mainwindow)

        self.calory_counter_label = QLabel(self)
        self.calory_counter_label.setGeometry(QtCore.QRect(1450, 0, 400, 81))
        self.calory_counter_label.setText(f'Калории: {self.calory_eated} из {mainwindow.calory_can_eat}'
                                          f'\nБелки: {self.proein_eated}\nЖиры: {self.fats_eated}\nУглеводы: {self.carbohydrates_eated}')
        self.calory_counter_label.setStyleSheet("font: 15pt Times New Roman")


        self.scroll_area.setWidget(self.main_widget)

    def add_meal_section(self, meal_name, meal_type, mainwindow):
        meal_label = QLabel(meal_name, self)
        meal_label.setStyleSheet("font: 20pt Times New Roman")
        meal_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(meal_label)

        meal_layout = QVBoxLayout()

        foods_ate = self.db.get_ate_food_by_type(mainwindow.current_user_id, meal_type)
        trash = []

        for food_ate in foods_ate:
            food_data = self.db.get_product_by_id(food_ate['product_id'], food_ate['eating_id'])
            for food in food_data:
                food['eat_id'] = food_ate['eating_id']
                food['product_count'] = food_ate['product_count']
                if food not in trash:
                    food_card_widget = QWidget()
                    vertical_layout = QVBoxLayout(food_card_widget)
                    vertical_layout.setContentsMargins(0, 0, 0, 0)

                    food_name_label = QLabel(food["product_name"])
                    vertical_layout.addWidget(food_name_label)

                    calory = float(food['calory'])/100 * float(food_ate['product_count'])
                    calory = round(calory)
                    food_calory_label = QLabel(f"Калории: {calory}")
                    self.calory_eated += calory
                    vertical_layout.addWidget(food_calory_label)

                    protein = float(food['protein'])/100 * float(food_ate['product_count'])
                    protein = round(protein, 1)
                    food_protein_label = QLabel(f"Белки: {protein}")
                    self.proein_eated += round(protein, 1)
                    vertical_layout.addWidget(food_protein_label)

                    fats = float(food['fats'])/100 * float(food_ate['product_count'])
                    fats = round(fats, 1)
                    food_fats_label = QLabel(f"Жиры: {fats}")
                    self.fats_eated += round(fats, 1)
                    vertical_layout.addWidget(food_fats_label)

                    carbohydrates = float(food['carbohydrates'])/100 * float(food_ate['product_count'])
                    carbohydrates = round(carbohydrates, 1)
                    food_carbohydrates_label = QLabel(f"Углеводы: {carbohydrates}")
                    self.carbohydrates_eated += round(carbohydrates, 1)
                    vertical_layout.addWidget(food_carbohydrates_label)

                    remove_food_button = QPushButton('Удалить')
                    food_data = {
                        'calory': calory,
                        'protein': protein,
                        'fats': fats,
                        'carbohydrates': carbohydrates,
                        'eating_id': food['eat_id']
                    }
                    remove_food_button.clicked.connect(
                        lambda cheked, widget=food_card_widget, food_data=food_data: self.remove_food_from_diary(widget,
                                                                                                                 food_data,
                                                                                                                 mainwindow))
                    vertical_layout.addWidget(remove_food_button)

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

    def remove_food_from_diary(self, widget, food_data, mainwindow):
        print(food_data)
        calory = food_data['calory']
        protein = food_data['protein']
        fats = food_data['fats']
        carbohydrates = food_data['carbohydrates']
        eating_id = int(food_data['eating_id'])
        self.calory_eated -= calory
        self.proein_eated -= protein
        self.fats_eated -= fats
        self.carbohydrates_eated -= carbohydrates
        self.proein_eated = round(self.proein_eated, 1)
        self.fats_eated = round(self.fats_eated, 1)
        self.carbohydrates_eated = round(self.carbohydrates_eated, 1)
        self.db.remove_eating(eating_id)
        self.calory_counter_label.setText(f'Калории: {self.calory_eated} из {mainwindow.calory_can_eat}'
                                          f'\nБелки: {self.proein_eated}\nЖиры: {self.fats_eated}\nУглеводы: {self.carbohydrates_eated}')
        widget.deleteLater()

    def switch_form(self, case):
        self.mainwindow.forms_switch(case)

    def count_calory(self, mainwindow):
        user_id = mainwindow.current_user_id
        data = self.db.get_user_by_id(user_id)
        weight_data = self.db.get_user_weight(user_id)
        user_birthdate = data[0]['user_birthdate']
        now = datetime.now()
        user_age = now.year - user_birthdate.year - ((now.month, now.day) < (user_birthdate.month, user_birthdate.day))
        if data[0]['user_gender'] == 'Мужской':
            mainwindow.calory_can_eat = round(66.5 + (13.75 * weight_data) + (5.003 * data[0]['user_height']) - (6.775 * user_age))
        else:
            mainwindow.calory_can_eat = round(655.1 + (9.563 * weight_data) + (1.85 * data[0]['user_height']) - (4.676 * user_age))
