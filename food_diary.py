from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout, QLabel, QScrollBar, QVBoxLayout, \
    QListWidgetItem
from left_menu import LeftMenu
from database_connection import DatabaseConnection


class FoodDiary(QWidget):
    def __init__(self, mainwindow):
        super().__init__()
        self.food_list_breakfast_widget = None
        self.statusbar = None
        self.verticalScrollBar = None
        self.write_food_dinner_button = None
        self.products_widget_dinner = None
        self.dinner_label = None
        self.dinner_widget = None
        self.write_food_lunch_button = None
        self.products_widget_lunch = None
        self.lunch_label = None
        self.lunch_widget = None
        self.write_food_breakfast_button = None
        self.products_widget_breakfast = None
        self.breakfast_label = None
        self.breakfast_widget = None
        self.calory_label_9 = None
        self.carbohydrates_count_label = None
        self.carbohydrates_label = None
        self.fats_count_label = None
        self.fats_label = None
        self.protein_count_label = None
        self.protein_label = None
        self.calory_count_label = None
        self.formLayout = None
        self.formLayoutWidget = None
        self.menu_button = None
        self.left_menu = None
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

        self.formLayoutWidget = QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(1160, 10, 161, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        # self.formLayout = QFormLayout(self.formLayoutWidget)
        # self.formLayout.setContentsMargins(0, 0, 0, 0)
        # self.formLayout.setObjectName("formLayout")
        #
        # self.calory_count_label = QLabel(self.formLayoutWidget)
        # self.calory_count_label.setObjectName("calory_count_label")
        # self.formLayout.setWidget(0, QFormLayout.FieldRole, self.calory_count_label)
        #
        # self.protein_label = QLabel(self.formLayoutWidget)
        # self.protein_label.setObjectName("protein_label")
        # self.formLayout.setWidget(1, QFormLayout.LabelRole, self.protein_label)
        #
        # self.protein_count_label = QLabel(self.formLayoutWidget)
        # self.protein_count_label.setObjectName("protein_count_label")
        # self.formLayout.setWidget(1, QFormLayout.FieldRole, self.protein_count_label)
        #
        # self.fats_label = QLabel(self.formLayoutWidget)
        # self.fats_label.setObjectName("fats_label")
        # self.formLayout.setWidget(3, QFormLayout.LabelRole, self.fats_label)
        #
        # self.fats_count_label = QLabel(self.formLayoutWidget)
        # self.fats_count_label.setObjectName("fats_count_label")
        # self.formLayout.setWidget(3, QFormLayout.FieldRole, self.fats_count_label)
        #
        # self.carbohydrates_label = QLabel(self.formLayoutWidget)
        # self.carbohydrates_label.setObjectName("carbohydrates_label")
        # self.formLayout.setWidget(5, QFormLayout.LabelRole, self.carbohydrates_label)
        #
        # self.carbohydrates_count_label = QLabel(self.formLayoutWidget)
        # self.carbohydrates_count_label.setObjectName("carbohydrates_count_label")
        # self.formLayout.setWidget(5, QFormLayout.FieldRole, self.carbohydrates_count_label)
        #
        # self.calory_label_9 = QLabel(self.formLayoutWidget)
        # self.calory_label_9.setObjectName("calory_label_9")
        # self.formLayout.setWidget(0, QFormLayout.LabelRole, self.calory_label_9)

        self.breakfast_widget = QWidget(self)
        self.breakfast_widget.setGeometry(QtCore.QRect(0, 170, 1331, 161))
        self.breakfast_widget.setObjectName("breakfast_widget")
        self.breakfast_label = QLabel(self.breakfast_widget)
        self.breakfast_label.setGeometry(QtCore.QRect(0, 5, 1331, 21))
        self.breakfast_label.setObjectName("breakfast_label")
        self.breakfast_label.setText('Завтрак')

        self.products_widget_breakfast = QWidget(self.breakfast_widget)
        self.products_widget_breakfast.setGeometry(QtCore.QRect(-1, 40, 1331, 41))
        self.products_widget_breakfast.setObjectName("products_widget_breakfast")

        self.write_food_breakfast_button = QPushButton(self.breakfast_widget)
        self.write_food_breakfast_button.setGeometry(QtCore.QRect(0, 80, 1331, 51))
        self.write_food_breakfast_button.setObjectName("write_food_breakfast_button")
        self.write_food_breakfast_button.setText('Добавить')
        self.write_food_breakfast_button.clicked.connect(lambda: mainwindow.forms_switch('food_list_breakfast'))

        self.lunch_widget = QWidget(self)
        self.lunch_widget.setGeometry(QtCore.QRect(0, 330, 1331, 161))
        self.lunch_widget.setObjectName("lunch_widget")
        self.lunch_label = QLabel(self.lunch_widget)
        self.lunch_label.setText('Обед')
        self.lunch_label.setGeometry(QtCore.QRect(0, 5, 1331, 21))
        self.lunch_label.setObjectName("lunch_label")

        self.products_widget_lunch = QWidget(self.lunch_widget)
        self.products_widget_lunch.setGeometry(QtCore.QRect(-1, 40, 1331, 41))
        self.products_widget_lunch.setObjectName("products_widget_lunch")

        self.write_food_lunch_button = QPushButton(self.lunch_widget)
        self.write_food_lunch_button.setGeometry(QtCore.QRect(0, 90, 1331, 51))
        self.write_food_lunch_button.setObjectName("write_food_lunch_button")
        self.write_food_lunch_button.setText('Добавить')
        self.write_food_lunch_button.clicked.connect(lambda: mainwindow.forms_switch('food_list_lunch'))

        self.dinner_widget = QWidget(self)
        self.dinner_widget.setGeometry(QtCore.QRect(0, 500, 1331, 151))
        self.dinner_widget.setObjectName("dinner_widget")
        self.dinner_label = QLabel(self.dinner_widget)
        self.dinner_label.setGeometry(QtCore.QRect(0, 5, 1331, 21))
        self.dinner_label.setObjectName("dinner_label")
        self.dinner_label.setText('Ужин')

        self.products_widget_dinner = QWidget(self.dinner_widget)
        self.products_widget_dinner.setGeometry(QtCore.QRect(-1, 40, 1331, 41))
        self.products_widget_dinner.setObjectName("products_widget_dinner")

        self.write_food_dinner_button = QPushButton(self.dinner_widget)
        self.write_food_dinner_button.setGeometry(QtCore.QRect(0, 80, 1331, 51))
        self.write_food_dinner_button.setObjectName("write_food_dinner_button")
        self.write_food_dinner_button.setText('Добавить')
        self.write_food_dinner_button.clicked.connect(lambda: mainwindow.forms_switch('food_list_dinner'))

        self.verticalScrollBar = QScrollBar(self)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1335, 0, 21, 831))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

    def show_left_menu(self):
        self.left_menu.show()
        self.left_menu.raise_()
        self.menu_button.hide()

    def hide_left_menu(self):
        self.left_menu.hide()
        self.menu_button.show()

    def write_ate_today_food(self, mainwindow):
#         Завтрак
        breakfast_food_ate = self.db.get_ate_food_by_type(mainwindow.current_user_id, 'breakfast')
        breakfast_food_data = self.db.
        food_card_widget = QWidget()
        food_card_widget.setGeometry(QtCore.QRect(0, 0, 1011, 111))

        vertical_layout = QVBoxLayout(food_card_widget)
        vertical_layout.setContentsMargins(0, 0, 0, 0)

        food_name_label = QLabel(breakfast_food_ate["product_name"])
        vertical_layout.addWidget(food_name_label)

        food_calory_label = QLabel(f"Калории: {breakfast_food_ate['calory']}")
        vertical_layout.addWidget(food_calory_label)

        food_protein_label = QLabel(f"Белки: {breakfast_food_ate['protein']}")
        vertical_layout.addWidget(food_protein_label)

        food_fats_label = QLabel(f"Жиры: {breakfast_food_ate['fats']}")
        vertical_layout.addWidget(food_fats_label)

        food_carbohydrates_label = QLabel(f"Углеводы: {breakfast_food_ate['carbohydrates']}")
        vertical_layout.addWidget(food_carbohydrates_label)

        choice_food_button = QPushButton('Выбрать')
        # choice_food_button.clicked.connect(lambda checked, food=food: self.choose_food(food, mainwindow))
        vertical_layout.addWidget(choice_food_button)

        self.list_item = QListWidgetItem()
        self.list_item.setSizeHint(food_card_widget.sizeHint())
        self.food_list_breakfast_widget.addItem(self.list_item)
        self.food_list_breakfast_widget.setItemWidget(self.list_item, food_card_widget)
#         Обед

#         Ужин
