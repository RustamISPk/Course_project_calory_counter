from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QStatusBar, QWidget, QFormLayout, QLabel, QScrollBar
from left_menu import LeftMenu


class FoodDiary(QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
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
        self.centralwidget = None
        self.left_menu = None
        self.setupUi(mainwindow)

    def setupUi(self, mainwindow):
        mainwindow.setObjectName("MainWindow")
        mainwindow.resize(1360, 861)
        self.centralwidget = QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")

        self.left_menu = LeftMenu(self)
        self.left_menu.hide()

        self.menu_button = QPushButton(self.centralwidget)
        self.menu_button.setGeometry(QtCore.QRect(0, 0, 151, 81))
        self.menu_button.setObjectName("menu_button")
        self.menu_button.setText("Меню")
        self.menu_button.clicked.connect(lambda: self.show_left_menu())

        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(1160, 10, 161, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.calory_count_label = QLabel(self.formLayoutWidget)
        self.calory_count_label.setObjectName("calory_count_label")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.calory_count_label)
        self.protein_label = QLabel(self.formLayoutWidget)
        self.protein_label.setObjectName("protein_label")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.protein_label)
        self.protein_count_label = QLabel(self.formLayoutWidget)
        self.protein_count_label.setObjectName("protein_count_label")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.protein_count_label)
        self.fats_label = QLabel(self.formLayoutWidget)
        self.fats_label.setObjectName("fats_label")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.fats_label)
        self.fats_count_label = QLabel(self.formLayoutWidget)
        self.fats_count_label.setObjectName("fats_count_label")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.fats_count_label)
        self.carbohydrates_label = QLabel(self.formLayoutWidget)
        self.carbohydrates_label.setObjectName("carbohydrates_label")
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.carbohydrates_label)
        self.carbohydrates_count_label = QLabel(self.formLayoutWidget)
        self.carbohydrates_count_label.setObjectName("carbohydrates_count_label")
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.carbohydrates_count_label)
        self.calory_label_9 = QLabel(self.formLayoutWidget)
        self.calory_label_9.setObjectName("calory_label_9")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.calory_label_9)

        self.breakfast_widget = QWidget(self.centralwidget)
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

        self.lunch_widget = QWidget(self.centralwidget)
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

        self.dinner_widget = QWidget(self.centralwidget)
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

        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1335, 0, 21, 831))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)
        self.setCentralWidget(self.centralwidget)

    def show_left_menu(self):
        self.left_menu.show()
        self.left_menu.raise_()
        self.menu_button.hide()

    def hide_left_menu(self):
        self.left_menu.hide()
        self.menu_button.show()
