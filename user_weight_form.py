from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class UserWeightForm(QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.statusbar = None
        self.weight_ghraphic_widget = None
        self.user_new_height_save_button = None
        self.user_new_height_line_edit = None
        self.horizontalLayout_2 = None
        self.horizontalLayoutWidget_2 = None
        self.label_3 = None
        self.user_height_statistic = None
        self.label_2 = None
        self.label = None
        self.IMT_count_button = None
        self.weight_line_edit = None
        self.height_line_edit = None
        self.verticalLayout = None
        self.horizontalLayout = None
        self.horizontalLayoutWidget = None
        self.Tittle_IMT_label = None
        self.menu_button = None
        self.centralwidget = None
        self.IMT_widget = None
        self.setup_ui(mainwindow)

    def setup_ui(self, mainwindow):
        mainwindow.setObjectName("MainWindow")
        mainwindow.resize(1380, 867)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IMT_widget = QtWidgets.QWidget(self.centralwidget)
        self.IMT_widget.setGeometry(QtCore.QRect(0, 0, 1371, 271))
        self.IMT_widget.setObjectName("IMT_widget")
        self.menu_button = QtWidgets.QPushButton(self.IMT_widget)
        self.menu_button.setGeometry(QtCore.QRect(0, 0, 151, 61))
        self.menu_button.setObjectName("menu_button")
        self.Tittle_IMT_label = QtWidgets.QLabel(self.IMT_widget)
        self.Tittle_IMT_label.setGeometry(QtCore.QRect(154, 10, 1211, 41))
        self.Tittle_IMT_label.setObjectName("Tittle_IMT_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.IMT_widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 90, 771, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.height_line_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.height_line_edit.setObjectName("height_line_edit")
        self.verticalLayout.addWidget(self.height_line_edit)
        self.weight_line_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.weight_line_edit.setObjectName("weight_line_edit")
        self.verticalLayout.addWidget(self.weight_line_edit)
        self.IMT_count_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.IMT_count_button.setObjectName("IMT_count_button")
        self.verticalLayout.addWidget(self.IMT_count_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.user_height_statistic = QtWidgets.QWidget(self.centralwidget)
        self.user_height_statistic.setGeometry(QtCore.QRect(-1, 270, 1371, 581))
        self.user_height_statistic.setObjectName("user_height_statistic")
        self.label_3 = QtWidgets.QLabel(self.user_height_statistic)
        self.label_3.setGeometry(QtCore.QRect(4, 9, 1361, 41))
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.user_height_statistic)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 50, 1371, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.user_new_height_line_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.user_new_height_line_edit.setObjectName("user_new_height_line_edit")
        self.horizontalLayout_2.addWidget(self.user_new_height_line_edit)
        self.user_new_height_save_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.user_new_height_save_button.setObjectName("user_new_height_save_button")
        self.horizontalLayout_2.addWidget(self.user_new_height_save_button)
        self.weight_ghraphic_widget = QtWidgets.QWidget(self.user_height_statistic)
        self.weight_ghraphic_widget.setGeometry(QtCore.QRect(9, 139, 1361, 441))
        self.weight_ghraphic_widget.setObjectName("weight_ghraphic_widget")
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)
