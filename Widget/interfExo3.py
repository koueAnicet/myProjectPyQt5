from PyQt5.QtWidgets import QMainWindow, QApplication
from Widget.exercice3 import Ui_MainWindow

class AccountPage(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AccountPage, self).__init__()
        self.setupUi(self)