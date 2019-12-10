import sys
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QMessageBox
from designe import Ui_MainWindow
import core


class Sato(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.load_to_sato)
        self.type_printer = core.get_type_printer()
        if self.type_printer == 1:
            self.pushButton.setText('Печать от датчика')
            self.label_3.setText('Непрерывный режим печати')
        elif self.type_printer == 0:
            self.pushButton.setText('Непрерывный режим печати')
            self.label_3.setText('Печать по датчику')
        else:
            self.label_3.setText('НЕКОРЕКТНЫЕ ПАРАМЕТРЫ!')

    def load_to_sato(self):
        """
        1 - fast mode (Continuous) 
        0 - dispenser mode

        """
        if self.type_printer == 1: # 1 - fast mode (Continuous)
            core.download_config_to_printer(0)
        elif self.type_printer == 0: # 0 - dispenser mode
            core.load_config_from_printer(type_printer)
            core.download_config_to_printer(1)
            core.restart_printer()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sato_app = Sato()
    sys.exit(app.exec_())
