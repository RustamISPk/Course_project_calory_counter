from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QLineEdit, QScrollBar, QVBoxLayout, QLabel, QFormLayout, \
    QStatusBar, QListWidget, QListWidgetItem
from database_connection import DatabaseConnection


# Добавить в базу данных поле в таблицу с продуктами type - продукт или рецепт

class FoodList(QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.list_item = None
        self.statusbar = None
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
        self.verticalLayout = None
        self.verticalLayoutWidget = None
        self.food_card_widget = None
        self.food_list_widget = None
        self.recipes_button = None
        self.products_button = None
        self.change_food_mode_widget = None
        self.verticalScrollBar = None
        self.find_products_line_edit = None
        self.find_products_button = None
        self.products_list_back_button = None
        self.centralwidget = None
        self.setupUi(mainwindow)
        self.load_food()

    def setupUi(self, mainwindow):
        mainwindow.setObjectName("MainWindow")
        mainwindow.resize(1378, 867)
        self.centralwidget = QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.products_list_back_button = QPushButton(self.centralwidget)
        self.products_list_back_button.setGeometry(QtCore.QRect(0, 10, 181, 41))
        self.products_list_back_button.setObjectName("products_list_back_button")
        self.products_list_back_button.setText('Назад')

        self.find_products_button = QPushButton(self.centralwidget)
        self.find_products_button.setGeometry(QtCore.QRect(1170, 10, 181, 41))
        self.find_products_button.setObjectName("find_products_button")
        self.find_products_button.setText('Найти')

        self.find_products_line_edit = QLineEdit(self.centralwidget)
        self.find_products_line_edit.setGeometry(QtCore.QRect(180, 10, 991, 41))
        self.find_products_line_edit.setObjectName("find_products_line_edit")
        self.find_products_line_edit.setPlaceholderText('Введите продукт')

        self.change_food_mode_widget = QWidget(self.centralwidget)
        self.change_food_mode_widget.setGeometry(QtCore.QRect(0, 50, 1351, 101))
        self.change_food_mode_widget.setObjectName("change_food_mode_widget")

        self.products_button = QPushButton(self.change_food_mode_widget)
        self.products_button.setGeometry(QtCore.QRect(0, 0, 671, 101))
        self.products_button.setObjectName("products_button")
        self.products_button.setText('Продукты')

        self.recipes_button = QPushButton(self.change_food_mode_widget)
        self.recipes_button.setGeometry(QtCore.QRect(680, 0, 671, 101))
        self.recipes_button.setObjectName("recipes_button")
        self.recipes_button.setText('Рецепты')

        self.food_list_widget = QListWidget(self.centralwidget)
        self.food_list_widget.setGeometry(QtCore.QRect(170, 150, 1011, 691))
        self.food_list_widget.setObjectName("food_list_widget")

        self.food_to_write_widget = QWidget(self.food_list_widget)
        self.food_to_write_widget.setGeometry(QtCore.QRect(280, 250, 441, 110))
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
        self.food_to_write_count_line_edit.setFixedHeight(30)  # Установите фиксированную высоту
        self.food_to_write_count_line_edit.setPlaceholderText('Количество продукта')
        self.food_to_write_count_line_edit.setVisible(True)
        self.food_to_write_button = QPushButton(self.formLayoutWidget)
        self.food_to_write_button.setObjectName("food_to_write_button")
        self.food_to_write_button.setText('Добавить')

        self.formLayout_2.addRow(self.food_to_write_name_label)
        self.formLayout_2.addRow(self.food_to_write_count_line_edit)
        self.formLayout_2.addRow(self.food_to_write_button)

        self.food_to_write_widget.hide()

        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)
        self.setCentralWidget(self.centralwidget)

    def load_food(self):
        db = DatabaseConnection()
        foods = db.find_all_food()
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
            choice_food_button.clicked.connect(lambda cheked, food=food: self.choose_food(food))
            vertical_layout.addWidget(choice_food_button)

            self.list_item = QListWidgetItem()
            self.list_item.setSizeHint(food_card_widget.sizeHint())
            self.food_list_widget.addItem(self.list_item)
            self.food_list_widget.setItemWidget(self.list_item, food_card_widget)

    def choose_food(self, food):
        self.food_to_write_name_label.setText(f"{food['product_name']}")
        self.food_to_write_widget.hide()
        self.food_to_write_widget.show()
        print(self.food_to_write_count_line_edit.isVisible())  # Должно быть True
        print(self.food_to_write_count_line_edit.size())  # Размер не должен быть (0, 0)
