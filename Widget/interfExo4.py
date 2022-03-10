from PyQt5.QtWidgets import QMainWindow, QApplication
from Widget.exercice4 import Ui_Dialog

class AccountPage(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(AccountPage, self).__init__()
        self.setupUi(self)