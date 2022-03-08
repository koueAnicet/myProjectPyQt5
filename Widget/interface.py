from PyQt5.QtWidgets import QMainWindow, QApplication
from Widget.fichier import Ui_Nan

class AccountPage(QMainWindow, Ui_Nan):
    def __init__(self):
        super().__init__()
        self.setupUi(self)