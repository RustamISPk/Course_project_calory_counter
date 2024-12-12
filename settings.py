# -*- coding: utf-8 -*-
from datetime import datetime
from time import strptime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit, QComboBox, QDateEdit

from database_connection import DatabaseConnection
from left_menu import LeftMenu


class UserSettings(QWidget):
    def __init__(self, mainwindow):
        super().__init__()

        self.left_menu = None
        self.user_data_save = None
        self.user_gender_combobox = None
        self.user_age_line_edit = None
        self.user_height_line_edit = None
        self.user_weight_line_edit = None
        self.verticalLayout = None
        self.verticalLayoutWidget = None
        self.menu_button = None
        self.db = DatabaseConnection()
        self.birth_date = None
        self.mainwindow = mainwindow
        self.initUI(mainwindow)

    def initUI(self, mainwindow):
        try:
            self.birth_date = self.db.get_user_birth_date(mainwindow.current_user_id)
            self.birth_date = datetime.strptime(self.birth_date, '%d-%m-%Y')
            self.setGeometry(100, 100, 1380, 867)
            self.setWindowTitle('Настройки пользователя')

            self.menu_button = QPushButton('Меню', self)
            self.menu_button.setGeometry(0, 0, 141, 61)
            self.menu_button.clicked.connect(lambda: self.show_left_menu())

            self.verticalLayoutWidget = QWidget(self)
            self.verticalLayoutWidget.setGeometry(550, 270, 231, 191)
            self.left_menu = LeftMenu(self)
            self.left_menu.hide()

            self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)

            self.user_height_line_edit = QLineEdit(self.verticalLayoutWidget)
            self.user_height_line_edit.setPlaceholderText('Рост')
            self.user_height_line_edit.setMaxLength(3)
            self.user_height_line_edit.setValidator(QIntValidator(1, 272, self))
            self.verticalLayout.addWidget(self.user_height_line_edit)

            self.user_weight_line_edit = QLineEdit(self.verticalLayoutWidget)
            self.user_weight_line_edit.setPlaceholderText('Вес')
            self.user_weight_line_edit.setMaxLength(6)
            self.user_weight_line_edit.setValidator(QDoubleValidator(1.0, 800.0, 2, self))
            self.verticalLayout.addWidget(self.user_weight_line_edit)

            self.user_age_line_edit = QDateEdit(self.verticalLayoutWidget)
            self.user_age_line_edit.setDate(self.birth_date)
            self.user_age_line_edit.setDisplayFormat("dd-MM-yyyy")
            self.user_age_line_edit.setCalendarPopup(True)
            self.user_age_line_edit.setGeometry(QtCore.QRect(530, 510, 331, 41))
            self.user_age_line_edit.setObjectName("user_age_line_edit")
            self.verticalLayout.addWidget(self.user_age_line_edit)

            self.user_gender_combobox = QComboBox(self.verticalLayoutWidget)
            self.user_gender_combobox.addItem('Мужской')
            self.user_gender_combobox.addItem('Женский')
            self.verticalLayout.addWidget(self.user_gender_combobox)

            self.user_data_save = QPushButton('Сохранить', self.verticalLayoutWidget)
            self.user_data_save.clicked.connect(lambda: self.save_changes(mainwindow))
            self.verticalLayout.addWidget(self.user_data_save)
        except Exception as e:
            print(e)

    def save_changes(self, mainwindow):
        try:
            user_height = self.user_height_line_edit.text()
            user_weight = self.user_weight_line_edit.text()
            user_age = self.user_age_line_edit.text()
            user_gender = self.user_gender_combobox.currentText()
            if user_height != '' and user_weight != '':
                self.user_height_line_edit.setStyleSheet("")
                self.user_height_line_edit.clear()
                self.user_weight_line_edit.setStyleSheet("")
                self.user_weight_line_edit.clear()
                self.db.change_user_params(mainwindow.current_user_id, user_height, user_weight, user_age, user_gender)
            elif user_height == '' and user_weight == '':
                self.user_height_line_edit.setStyleSheet("border: 2px solid red;")
                self.user_height_line_edit.setPlaceholderText('Заполните поле!')
                self.user_weight_line_edit.setStyleSheet("border: 2px solid red;")
                self.user_weight_line_edit.setPlaceholderText('Заполните поле!')
            elif user_height == '' and user_weight != '':
                self.user_height_line_edit.setStyleSheet("border: 2px solid red;")
                self.user_height_line_edit.setPlaceholderText('Заполните поле!')
            elif user_height != '' and user_weight == '':
                self.user_weight_line_edit.setStyleSheet("border: 2px solid red;")
                self.user_weight_line_edit.setPlaceholderText('Заполните поле!')
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
