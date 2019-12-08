import sys
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QMessageBox
from designe import Ui_MainWindow
import time
import random


class Sato(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.load_to_sato)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.sato_mode)

    def load_to_sato(self):
        print('load config')
        for i in range(0, 101):
          #  time.sleep(0.1)
            self.progressBar.setValue(i)
        msg = QMessageBox.information(None, 'Info', 'text')
        msg.show()


    def sato_mode(self):
        print(self.comboBox.currentIndex())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sato_app = Sato()
    sys.exit(app.exec_())
