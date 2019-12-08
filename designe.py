# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designe.ui',
# licensing of 'designe.ui' applies.
#
# Created: Sun Dec  8 14:17:55 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 60, 280, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 120, 281, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 230, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setText("Powered by dyomin@hlebprom.ru")
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(60, 190, 311, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.comboBox.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Управление режимом SATO v.1.0", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Выбирите режим работы принтера:", None, -1))
        self.comboBox.setCurrentText(QtWidgets.QApplication.translate("MainWindow", "Печать по сигналу от датчика", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Печать по сигналу от датчика", None, -1))
        self.comboBox.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Непрерывная печать", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Отправить", None, -1))

