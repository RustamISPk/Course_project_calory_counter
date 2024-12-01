from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class FoodList(QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.setupUi(mainwindow)

    def setupUi(self, mainwindow):
        mainwindow.setObjectName("MainWindow")
        mainwindow.resize(1378, 867)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.products_list_back_button = QtWidgets.QPushButton(self.centralwidget)
        self.products_list_back_button.setGeometry(QtCore.QRect(0, 10, 181, 41))
        self.products_list_back_button.setObjectName("products_list_back_button")
        self.find_products_button = QtWidgets.QPushButton(self.centralwidget)
        self.find_products_button.setGeometry(QtCore.QRect(1170, 10, 181, 41))
        self.find_products_button.setObjectName("find_products_button")
        self.find_products_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.find_products_line_edit.setGeometry(QtCore.QRect(180, 10, 991, 41))
        self.find_products_line_edit.setObjectName("find_products_line_edit")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1355, 0, 21, 861))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.change_food_mode_widget = QtWidgets.QWidget(self.centralwidget)
        self.change_food_mode_widget.setGeometry(QtCore.QRect(0, 50, 1351, 101))
        self.change_food_mode_widget.setObjectName("change_food_mode_widget")
        self.products_button = QtWidgets.QPushButton(self.change_food_mode_widget)
        self.products_button.setGeometry(QtCore.QRect(0, 0, 671, 101))
        self.products_button.setObjectName("products_button")
        self.recipes_button = QtWidgets.QPushButton(self.change_food_mode_widget)
        self.recipes_button.setGeometry(QtCore.QRect(680, 0, 671, 101))
        self.recipes_button.setObjectName("recipes_button")
        self.food_list_widget = QtWidgets.QWidget(self.centralwidget)
        self.food_list_widget.setGeometry(QtCore.QRect(170, 150, 1011, 691))
        self.food_list_widget.setObjectName("food_list_widget")
        self.food_card_widget = QtWidgets.QWidget(self.food_list_widget)
        self.food_card_widget.setGeometry(QtCore.QRect(0, 0, 1011, 111))
        self.food_card_widget.setObjectName("food_card_widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.food_card_widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.food_name_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.food_name_label.setObjectName("food_name_label")
        self.verticalLayout.addWidget(self.food_name_label)
        self.food_calory_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.food_calory_label.setObjectName("food_calory_label")
        self.verticalLayout.addWidget(self.food_calory_label)
        self.food_protein_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.food_protein_label.setObjectName("food_protein_label")
        self.verticalLayout.addWidget(self.food_protein_label)
        self.food_fats_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.food_fats_label.setObjectName("food_fats_label")
        self.verticalLayout.addWidget(self.food_fats_label)
        self.food_carbohydrates_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.food_carbohydrates_label.setObjectName("food_carbohydrates_label")
        self.verticalLayout.addWidget(self.food_carbohydrates_label)
        self.choice_food_button = QtWidgets.QPushButton(self.food_card_widget)
        self.choice_food_button.setGeometry(QtCore.QRect(800, 0, 211, 111))
        self.choice_food_button.setObjectName("choice_food_button")
        self.food_to_write_widget = QtWidgets.QWidget(self.food_list_widget)
        self.food_to_write_widget.setGeometry(QtCore.QRect(280, 130, 441, 91))
        self.food_to_write_widget.setObjectName("food_to_write_widget")
        self.formLayoutWidget = QtWidgets.QWidget(self.food_to_write_widget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 421, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.food_to_write_name_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.food_to_write_name_label.setObjectName("food_to_write_name_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.food_to_write_name_label)
        self.food_to_write_count_line_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.food_to_write_count_line_edit.setObjectName("food_to_write_count_line_edit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.food_to_write_count_line_edit)
        self.food_to_write_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.food_to_write_button.setObjectName("food_to_write_button")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.food_to_write_button)
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)
        self.setCentralWidget(self.centralwidget)
