from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from database_connection import DatabaseConnection
from left_menu import LeftMenu


class UserWeightForm(QWidget):
    def __init__(self, mainwindow):
        try:
            super().__init__()
            self.ax = None
            self.figure = None
            self.mainwindow = mainwindow
            self.left_menu = None
            self.weight_ghraphic_widget = None
            self.user_new_weight_save_button = None
            self.user_new_weight_line_edit = None
            self.horizontalLayout_2 = None
            self.horizontalLayoutWidget_2 = None
            self.weight_statistic_label = None
            self.user_height_statistic = None
            self.IMT_data_label = None
            self.IMT_count_label = None
            self.IMT_count_button = None
            self.weight_line_edit = None
            self.height_line_edit = None
            self.verticalLayout = None
            self.horizontalLayout = None
            self.horizontalLayoutWidget = None
            self.Tittle_IMT_label = None
            self.menu_button = None
            self.IMT_widget = None
            self.db = DatabaseConnection()
            # self.count_calory(mainwindow)
            self.setup_ui(mainwindow)
            self.load_data_for_graphic(mainwindow)
        except Exception as e:
            print(e)

    def setup_ui(self, mainwindow):
        self.setObjectName("User  WeightForm")
        self.resize(1920, 1080)

        self.IMT_widget = QWidget(self)
        self.IMT_widget.setGeometry(QtCore.QRect(0, 0, 1850, 350))
        self.IMT_widget.setObjectName("IMT_widget")

        self.left_menu = LeftMenu(self)
        self.left_menu.hide()

        self.menu_button = QPushButton(self.IMT_widget)
        self.menu_button.setGeometry(QtCore.QRect(0, 0, 151, 61))
        self.menu_button.setText('Меню')
        self.menu_button.setObjectName("menu_button")
        self.menu_button.clicked.connect(lambda: self.show_left_menu())

        self.Tittle_IMT_label = QLabel(self.IMT_widget)
        self.Tittle_IMT_label.setGeometry(QtCore.QRect(154, 10, 1450, 41))
        self.Tittle_IMT_label.setObjectName("Tittle_IMT_label")
        self.Tittle_IMT_label.setText('Индекс массы тела')
        self.Tittle_IMT_label.setAlignment(Qt.AlignCenter)
        self.Tittle_IMT_label.setStyleSheet("font: 20pt Times New Roman")

        self.horizontalLayoutWidget = QWidget(self.IMT_widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 90, 1920, 250))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.height_line_edit = QLineEdit(self.horizontalLayoutWidget)
        self.height_line_edit.setObjectName("height_line_edit")
        self.height_line_edit.setPlaceholderText('Введите ваш рост')
        self.height_line_edit.setMaxLength(3)
        self.height_line_edit.setValidator(QIntValidator(1, 272, self))
        self.verticalLayout.addWidget(self.height_line_edit)

        self.weight_line_edit = QLineEdit(self.horizontalLayoutWidget)
        self.weight_line_edit.setObjectName("weight_line_edit")
        self.weight_line_edit.setPlaceholderText('Введите ваш вес')
        self.weight_line_edit.setValidator(QDoubleValidator(1.0, 800.0, 2, self))
        self.weight_line_edit.setMaxLength(4)
        self.verticalLayout.addWidget(self.weight_line_edit)

        self.IMT_count_button = QPushButton(self.horizontalLayoutWidget)
        self.IMT_count_button.setObjectName("IMT_count_button")
        self.IMT_count_button.setText('Рассчитать')
        self.IMT_count_button.clicked.connect(lambda: self.count_IMT(mainwindow))
        self.verticalLayout.addWidget(self.IMT_count_button)

        self.height_line_edit.setFixedWidth(400)
        self.weight_line_edit.setFixedWidth(400)
        self.IMT_count_button.setFixedWidth(400)
        self.height_line_edit.setFixedHeight(45)
        self.weight_line_edit.setFixedHeight(45)
        self.IMT_count_button.setFixedHeight(45)
        self.horizontalLayout.setStretch(0, 0)
        self.horizontalLayout.setStretch(1, 0)
        self.horizontalLayout.setStretch(2, 0)
        self.horizontalLayout.setStretch(3, 0)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.IMT_count_label = QLabel(self.horizontalLayoutWidget)
        self.IMT_count_label.setObjectName("label")
        self.IMT_count_label.setText(f'Ваш ИМТ:{round(mainwindow.IMT, 2)}')
        self.IMT_count_label.setStyleSheet("font: 15pt Times New Roman")

        self.horizontalLayout.addWidget(self.IMT_count_label)

        self.IMT_data_label = QLabel(self.horizontalLayoutWidget)
        self.IMT_data_label.setObjectName("label_2")
        self.IMT_data_label.setText("от 18,5 до 24,9 - нормальный вес \nот 25 до 29,9 - избыточный весот \n30 - "
                                    "ожирение")
        self.IMT_data_label.setStyleSheet("font: 15pt Times New Roman")
        self.horizontalLayout.addWidget(self.IMT_data_label)

        self.user_height_statistic = QWidget(self)
        self.user_height_statistic.setGeometry(QtCore.QRect(-1, 350, 1850, 581))
        self.user_height_statistic.setObjectName("user_height_statistic")

        self.weight_statistic_label = QLabel(self.user_height_statistic)
        self.weight_statistic_label.setGeometry(QtCore.QRect(4, 9, 1850, 41))
        self.weight_statistic_label.setText("Статистика веса")
        self.weight_statistic_label.setStyleSheet("font: 20pt Times New Roman")
        self.weight_statistic_label.setAlignment(Qt.AlignCenter)
        self.weight_statistic_label.setObjectName("label_3")

        self.horizontalLayoutWidget_2 = QWidget(self.user_height_statistic)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 50, 500, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.user_new_weight_line_edit = QLineEdit(self.horizontalLayoutWidget_2)
        self.user_new_weight_line_edit.setObjectName("user_new_height_line_edit")
        self.user_new_weight_line_edit.setPlaceholderText('Введите ваш текущий вес')
        self.user_new_weight_line_edit.setValidator(QDoubleValidator(1.0, 800.0, 2, self))
        self.user_new_weight_line_edit.setMaxLength(4)
        self.horizontalLayout_2.addWidget(self.user_new_weight_line_edit)

        self.user_new_weight_save_button = QPushButton(self.horizontalLayoutWidget_2)
        self.user_new_weight_save_button.setObjectName("user_new_height_save_button")
        self.user_new_weight_save_button.setText('Добавить')
        self.user_new_weight_save_button.clicked.connect(lambda: self.write_weight(mainwindow))
        self.horizontalLayout_2.addWidget(self.user_new_weight_save_button)

        self.weight_ghraphic_widget = QWidget(self.user_height_statistic)
        self.weight_ghraphic_widget.setGeometry(QtCore.QRect(9, 139, 1850, 441))
        self.weight_ghraphic_widget.setObjectName("weight_ghraphic_widget")

    def show_left_menu(self):
        self.left_menu.show()
        self.left_menu.raise_()
        self.menu_button.hide()

    def hide_left_menu(self):
        self.left_menu.hide()
        self.menu_button.show()

    def switch_form(self, case):
        self.mainwindow.forms_switch(case)

    def write_weight(self, mainwindow):
        if self.user_new_weight_line_edit.text() != '' and not self.user_new_weight_line_edit.text().startswith(','):
            weight = self.user_new_weight_line_edit.text()
            weight = weight.replace(',', '.')
            user_id = mainwindow.current_user_id
            self.db.write_user_new_weight(user_id, weight)
            self.user_new_weight_line_edit.clear()
            self.user_new_weight_line_edit.setStyleSheet("")
            self.user_new_weight_line_edit.setPlaceholderText('Введите ваш текущий вес')
            self.switch_form('user_weight')
        elif self.user_new_weight_line_edit.text() == '':
            self.user_new_weight_line_edit.clear()
            self.user_new_weight_line_edit.setStyleSheet("border: 2px solid red;")
            self.user_new_weight_line_edit.setPlaceholderText('Заполните поле!')
        elif self.user_new_weight_line_edit.text().startswith(','):
            self.user_new_weight_line_edit.clear()
            self.user_new_weight_line_edit.setStyleSheet("border: 2px solid red;")
            self.user_new_weight_line_edit.setPlaceholderText('Неправильно введен вес!')

    def count_IMT(self, mainwindow):
        if self.height_line_edit.text() != '' and self.weight_line_edit.text() != '':
            height = self.height_line_edit.text()
            weight = self.weight_line_edit.text()
            if not height.startswith('0') and not weight.startswith(','):
                height = int(height) / 100
                weight = float(self.weight_line_edit.text())
                mainwindow.IMT = weight / (height * height)
                self.IMT_count_label.setText(f'Ваш ИМТ: {round(mainwindow.IMT, 2)}')
                self.height_line_edit.clear()
                self.height_line_edit.setStyleSheet("")
                self.height_line_edit.setPlaceholderText('Введите ваш рост')
                self.weight_line_edit.clear()
                self.weight_line_edit.setStyleSheet("")
                self.weight_line_edit.setPlaceholderText('Введите ваш вес')
            elif height.startswith('0') and not weight.startswith(','):
                self.height_line_edit.clear()
                self.height_line_edit.setStyleSheet("border: 2px solid red;")
                self.height_line_edit.setPlaceholderText('Неправильно введен рост!')
            elif weight.startswith(',') and not height.startswith('0'):
                self.weight_line_edit.clear()
                self.weight_line_edit.setStyleSheet("border: 2px solid red;")
                self.weight_line_edit.setPlaceholderText('Неправильно введен вес!')
            else:
                self.height_line_edit.clear()
                self.height_line_edit.setStyleSheet("border: 2px solid red;")
                self.height_line_edit.setPlaceholderText('Неправильно введен рост!')
                self.weight_line_edit.clear()
                self.weight_line_edit.setStyleSheet("border: 2px solid red;")
                self.weight_line_edit.setPlaceholderText('Неправильно введен вес!')
        else:
            elements = [self.height_line_edit, self.weight_line_edit]
            for element in elements:
                if element.text() == '':
                    element.setStyleSheet("border: 2px solid red;")
                    element.setPlaceholderText('Заполните поле!')

    def load_data_for_graphic(self, mainwindow):
        user_id = mainwindow.current_user_id
        user_weight_data = self.db.load_graphic_data(user_id)
        graphic_data = []
        for user in user_weight_data:
            graphic_data.append([user['weight_date'],
                                 user['user_weight']])
        self.plot_graphic(graphic_data)

    def plot_graphic(self, datas):
        dates = []
        weights = []
        for data in datas:
            dates.append(data[0])
            weights.append(data[1])

        if self.figure is not None:
            self.figure.clear()

        self.figure = plt.Figure(figsize=(15, 5), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self.weight_ghraphic_widget)
        self.ax = self.figure.add_subplot(111)
        self.ax.plot(dates, weights, marker='o', linestyle='-', color='b')
        self.ax.set_title('Изменение веса')
        self.ax.set_xlabel('Дата')
        self.ax.set_ylabel('Вес (кг)')
        self.ax.grid(True)
        layout = QVBoxLayout(self.weight_ghraphic_widget)
        layout.addWidget(self.canvas)
        self.canvas.draw()

