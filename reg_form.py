from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QWidget, QPushButton, QComboBox, QStatusBar, QDateEdit
from database_connection import DatabaseConnection
from PyQt5.QtGui import QIntValidator, QDoubleValidator

# Доработать поле для ввода веса (если длина больше 4, то проверить на наличие точки)

class RegForm(QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.connection = None
        self.statusbar = None
        self.reg_confirm_button = None
        self.person_password_line_edit = None
        self.person_age_line_edit = None
        self.person_weight_line_edit = None
        self.person_height_line_edit = None
        self.person_login_line_edit = None
        self.person_lastname_line_edit = None
        self.person_name_line_edit = None
        self.centralwidget = None
        self.reg_form_back_button = None
        self.person_gender_combobox = None
        self.setupUi(mainwindow)

    def setupUi(self, mainwindow):
        mainwindow.setObjectName("MainWindow")
        mainwindow.resize(1377, 865)
        self.centralwidget = QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.reg_form_back_button = QPushButton(self.centralwidget)
        self.reg_form_back_button.setGeometry(QtCore.QRect(0, 0, 121, 61))
        self.reg_form_back_button.setObjectName("reg_form_back_button")
        self.reg_form_back_button.setText("Назад")
        self.reg_form_back_button.clicked.connect(lambda: self.back_to_main_window(mainwindow))
        self.person_name_line_edit = QLineEdit(self.centralwidget)
        self.person_name_line_edit.setGeometry(QtCore.QRect(530, 210, 331, 41))
        self.person_name_line_edit.setObjectName("person_name_line_edit")
        self.person_name_line_edit.setPlaceholderText('Введите имя')
        self.person_name_line_edit.setMaxLength(45)
        self.person_lastname_line_edit = QLineEdit(self.centralwidget)
        self.person_lastname_line_edit.setGeometry(QtCore.QRect(530, 260, 331, 41))
        self.person_lastname_line_edit.setObjectName("person_lastname_line_edit")
        self.person_lastname_line_edit.setPlaceholderText('Введите фамилию')
        self.person_lastname_line_edit.setMaxLength(45)
        self.person_login_line_edit = QLineEdit(self.centralwidget)
        self.person_login_line_edit.setGeometry(QtCore.QRect(530, 310, 331, 41))
        self.person_login_line_edit.setObjectName("person_login_line_edit")
        self.person_login_line_edit.setPlaceholderText('Введите логин')
        self.person_login_line_edit.setMaxLength(45)
        self.person_height_line_edit = QLineEdit(self.centralwidget)
        self.person_height_line_edit.setGeometry(QtCore.QRect(530, 410, 331, 41))
        self.person_height_line_edit.setObjectName("person_height_line_edit")
        self.person_height_line_edit.setPlaceholderText('Введите рост')
        self.person_height_line_edit.setValidator(QIntValidator(1, 272, self))
        self.person_height_line_edit.setMaxLength(3)
        self.person_weight_line_edit = QLineEdit(self.centralwidget)
        self.person_weight_line_edit.setMaxLength(6)
        self.person_weight_line_edit.setGeometry(QtCore.QRect(530, 460, 331, 41))
        self.person_weight_line_edit.setObjectName("person_weight_line_edit")
        self.person_weight_line_edit.setPlaceholderText('Введите вес')
        self.person_weight_line_edit.setValidator(QDoubleValidator(1.0, 800.0, 2, self))
        self.person_age_line_edit = QDateEdit(self.centralwidget)
        self.person_age_line_edit.setDate(QDate.currentDate())
        self.person_age_line_edit.setDisplayFormat("dd-MM-yyyy")
        self.person_age_line_edit.setCalendarPopup(True)
        self.person_age_line_edit.setGeometry(QtCore.QRect(530, 510, 331, 41))
        self.person_age_line_edit.setObjectName("person_age_line_edit")
        self.person_password_line_edit = QLineEdit(self.centralwidget)
        self.person_password_line_edit.setGeometry(QtCore.QRect(530, 360, 331, 41))
        self.person_password_line_edit.setObjectName("person_password_line_edit")
        self.person_password_line_edit.setPlaceholderText('Введите пароль')
        self.person_password_line_edit.setMaxLength(45)
        self.person_password_line_edit.setEchoMode(QLineEdit.Password)
        self.reg_confirm_button = QPushButton(self.centralwidget)
        self.reg_confirm_button.setGeometry(QtCore.QRect(630, 620, 141, 71))
        self.reg_confirm_button.setObjectName("reg_confirm_button")
        self.reg_confirm_button.setText("Продолжить")
        self.reg_confirm_button.clicked.connect(lambda: self.confirm_reg(mainwindow))
        self.person_gender_combobox = QComboBox(self.centralwidget)
        self.person_gender_combobox.setGeometry(QtCore.QRect(530, 560, 331, 41))
        self.person_gender_combobox.setObjectName("person_gender_combobox")
        self.person_gender_combobox.addItem("Мужской")
        self.person_gender_combobox.addItem("Женский")
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)
        self.setCentralWidget(self.centralwidget)

    def confirm_reg(self, mainwindow):
        try:
            fields_check = self.check_empty_fields
            if fields_check:
                name = self.person_name_line_edit.text()
                surname = self.person_lastname_line_edit.text()
                login = self.person_login_line_edit.text()
                password = self.person_password_line_edit.text()
                height = self.person_height_line_edit.text()
                weight = self.person_weight_line_edit.text()
                age = self.person_age_line_edit.text()
                gender = self.person_gender_combobox.currentText()
                # print('hello')
                db = DatabaseConnection()
                db.save_user_account(name, surname, login, password, height, weight, age, gender)
                self.back_to_main_window(mainwindow)
            else:
                print(fields_check)
        except Exception as e:
            print(e)

    def check_empty_fields(self):
        name = self.person_name_line_edit.text().isalpha()
        surname = self.person_lastname_line_edit.text().isalpha()
        login = self.is_empty(self.person_login_line_edit.text())
        password = self.is_empty(self.person_password_line_edit.text())
        height = self.person_height_line_edit.text().isdigit()
        weight = self.isfloat(self.person_weight_line_edit.text())
        age = self.is_empty(self.person_age_line_edit.text())
        check_age_logic = self.check_age()
        if name and surname and not login and not password and height and weight and not age and check_age_logic:
            return True
        else:
            if not name:
                self.person_name_line_edit.setStyleSheet("border: 2px solid red;")
                self.person_name_line_edit.setPlaceholderText('Заполните поле')
            if not surname:
                self.person_lastname_line_edit.setStyleSheet("border: 2px solid red;")
                self.person_lastname_line_edit.setPlaceholderText('Заполните поле')
            if login:
                self.person_login_line_edit.setStyleSheet("border: 2px solid red;")
                self.person_login_line_edit.setPlaceholderText('Заполните поле')
            if password:
                self.person_password_line_edit.setStyleSheet("border: 2px solid red;")
                self.person_password_line_edit.setPlaceholderText('Заполните поле')
            if not height:
                self.person_height_line_edit.setStyleSheet("border: 2px solid red;")
                self.person_height_line_edit.setPlaceholderText('Заполните поле')
            if not weight:
                self.person_weight_line_edit.setStyleSheet("border: 2px solid red;")
                self.person_weight_line_edit.setPlaceholderText('Заполните поле')
            if age or not check_age_logic:
                self.person_age_line_edit.setStyleSheet("border: 2px solid red;")
            return False

    def check_age(self):
        age = self.person_age_line_edit.text()
        age_list = age.split('-')
        if int(age_list[0]) >= 1900 and int(age_list[1]) <= 12:
            match age_list[1]:
                case '01' if age_list[2] <= 31:
                    return True
                case '02' if age_list[2] <= 29:
                    if age_list[0] % 4 == 0 and age_list[2] <= 29:
                        return True
                    elif age_list[0] % 4 != 0 and age_list[2] <= 28:
                        return True
                case '03' if age_list[2] <= 31:
                    return True
                case '04' if age_list[2] <= 30:
                    return True
                case '05' if age_list[2] <= 31:
                    return True
                case '06' if age_list[2] <= 30:
                    return True
                case '07' if age_list[2] <= 31:
                    return True
                case '08' if age_list[2] <= 31:
                    return True
                case '09' if age_list[2] <= 30:
                    return True
                case '10' if age_list[2] <= 31:
                    return True
                case '11' if age_list[2] <= 30:
                    return True
                case '12' if age_list[2] <= 31:
                    return True
                case _:
                    return False
        else:
            return False

    def clear_elements(self):
        self.person_name_line_edit.setStyleSheet("")
        self.person_name_line_edit.clear()
        self.person_name_line_edit.setPlaceholderText('Введите имя')

        self.person_lastname_line_edit.setStyleSheet("")
        self.person_lastname_line_edit.clear()
        self.person_lastname_line_edit.setPlaceholderText('Введите фамилию')

        self.person_login_line_edit.setStyleSheet("")
        self.person_login_line_edit.clear()
        self.person_login_line_edit.setPlaceholderText('Введите логин')

        self.person_password_line_edit.setStyleSheet("")
        self.person_password_line_edit.clear()
        self.person_password_line_edit.setPlaceholderText('Введите пароль')

        self.person_height_line_edit.setStyleSheet("")
        self.person_height_line_edit.clear()
        self.person_height_line_edit.setPlaceholderText('Введите рост')

        self.person_weight_line_edit.setStyleSheet("")
        self.person_weight_line_edit.clear()
        self.person_weight_line_edit.setPlaceholderText('Введите вес')

        self.person_age_line_edit.setStyleSheet("")
        self.person_age_line_edit.clear()

    def back_to_main_window(self, mainwindow):
        try:
            mainwindow.forms_switch('reg_back')
            self.clear_elements()
        except Exception as e:
            print(e)

    def is_empty(self, string):
        if len(string) == 0:
            return True
        else:
            return False

    def isfloat(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False
