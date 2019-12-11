import sys
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QMessageBox
from designe import Ui_MainWindow
import core
import config
import logging


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='log.log')
logger = logging.getLogger('My APP')
logger.info('Start APP')


class Sato(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.load_to_sato)
        self.init_window()

    def init_window(self):
        self.type_printer = core.get_type_printer()
        if self.type_printer == 1:
            self.pushButton.setText('Печать от датчика')
            self.label_3.setText('Непрерывный режим печати')
        elif self.type_printer == 0:
            self.pushButton.setText('Непрерывный режим печати')
            self.label_3.setText('Печать по датчику')
        else:
            self.label_3.setText('НЕКОРРЕКТНЫЕ ПАРАМЕТРЫ!')


    def load_to_sato(self):
        """
        1 - fast mode (Continuous) 
        0 - dispenser mode

        """
        data = core.get_advanced_config()
        if self.type_printer == 1: # 1 - fast mode (Continuous)
            data_modif = core.change_config(data=data, param=config.param_dispenser_mode)
        elif self.type_printer == 0: # 0 - dispenser mode
            data_modif = core.change_config(data=data, param=config.param_continuous_mode)
        else:
            logger.error('Error type printer config')
            raise Exception()
        if core.send_data(data_modif) == 200:
            if core.restart_printer() == 200:
                self.init_window()
            else:
                logger.error('Restart printer False')
                raise Exception()
        else:
            logger.error('Send data to printer False')
            raise Exception()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sato_app = Sato()
    sys.exit(app.exec_())
