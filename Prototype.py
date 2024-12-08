from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QStackedWidget, QVBoxLayout
from qt_material import apply_stylesheet
from auth_form import AuthForm
from food_diary import FoodDiary
from food_list import FoodList
from left_menu import LeftMenu
from reg_auth_form import RegAuthForm
from reg_form import RegForm
from user_weight_form import UserWeightForm


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = None
        self.stack = None
        self.Widget = None
        self.window7 = None
        self.window5 = None
        self.window6 = None
        self.window4 = None
        self.window3 = None
        self.window2 = None
        self.window1 = None
        self.current_user_id = None
        self.UIinit()

    def UIinit(self):
        self.Widget = QWidget()
        self.stack = QStackedWidget()

        self.window1 = RegAuthForm(self)
        self.window2 = RegForm(self)
        self.window3 = AuthForm(self)
        self.window4 = FoodDiary(self)
        self.window5 = FoodList(self)
        self.window6 = LeftMenu(self)
        self.window7 = UserWeightForm(self)

        self.stack.addWidget(self.window1)
        self.stack.addWidget(self.window2)
        self.stack.addWidget(self.window3)
        self.stack.addWidget(self.window4)
        self.stack.addWidget(self.window5)
        self.stack.addWidget(self.window6)
        self.stack.addWidget(self.window7)
        self.stack.setCurrentWidget(self.window1)

        self.setCentralWidget(self.Widget)
        self.layout = QVBoxLayout(self.Widget)
        self.layout.addWidget(self.stack)

    def forms_switch(self, data):
        match data:
            case 'reg':
                self.stack.setCurrentWidget(self.window2)
            case 'auth':
                self.stack.setCurrentWidget(self.window3)
            case 'reg_back':
                self.stack.setCurrentWidget(self.window1)
            case 'auth_back':
                self.stack.setCurrentWidget(self.window1)
            case 'food_diary':
                self.stack.setCurrentWidget(self.window4)
            case 'food_list':
                self.stack.setCurrentWidget(self.window5)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(1920, 1080)
    apply_stylesheet(app, theme='dark_purple.xml')
    window.showMaximized()
    sys.exit(app.exec_())
