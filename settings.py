# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1380, 867)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.menu_button.setGeometry(QtCore.QRect(0, 0, 141, 61))
        self.menu_button.setObjectName("menu_button")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(550, 270, 231, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.user_height_line_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.user_height_line_edit.setObjectName("user_height_line_edit")
        self.verticalLayout.addWidget(self.user_height_line_edit)
        self.user_weight_line_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.user_weight_line_edit.setObjectName("user_weight_line_edit")
        self.verticalLayout.addWidget(self.user_weight_line_edit)
        self.user_age_line_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.user_age_line_edit.setObjectName("user_age_line_edit")
        self.verticalLayout.addWidget(self.user_age_line_edit)
        self.user_sex_combobox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.user_sex_combobox.setObjectName("user_sex_combobox")
        self.user_sex_combobox.addItem("")
        self.user_sex_combobox.addItem("")
        self.verticalLayout.addWidget(self.user_sex_combobox)
        self.user_data_save = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.user_data_save.setObjectName("user_data_save")
        self.verticalLayout.addWidget(self.user_data_save)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_button.setText(_translate("MainWindow", "╨Ь╨╡╨╜╤О"))
        self.user_height_line_edit.setText(_translate("MainWindow", "╨Т╨░╤И ╤А╨╛╤Б╤В"))
        self.user_weight_line_edit.setText(_translate("MainWindow", "╨Т╨░╤И ╨▓╨╡╤Б"))
        self.user_age_line_edit.setText(_translate("MainWindow", "╨Т╨░╤И ╨▓╨╛╨╖╤А╨░╤Б╤В"))
        self.user_sex_combobox.setItemText(0, _translate("MainWindow", "╨Ь╤Г╨╢╤Б╨║╨╛╨╣"))
        self.user_sex_combobox.setItemText(1, _translate("MainWindow", "╨Ц╨╡╨╜╤Б╨║╨╕╨╣"))
        self.user_data_save.setText(_translate("MainWindow", "╨б╨╛╤Е╤А╨░╨╜╨╕╤В╤М"))