# -*- coding: utf-8 -*-
"""
Project: GUI Base Converter Tool
Description: A Python-based tool for converting numbers between different bases with a PyQt GUI.
             This tool supports conversion between integers, binary, and hexadecimal formats.
Version: 1.0.0
Author: Luke Wait
Date: July 25, 2023
License: MIT License

Dependencies (requirements.txt):
PyQt5==5.15.9
pyqt5-tools==5.15.9.3.3

GitHub Repository: https://github.com/LukeWait/base-converter

Form implementation generated from reading ui file 'pyqt_gui.ui'
Created by: PyQt5 UI code generator 5.15.9
WARNING: Any manual changes made to this file will be lost when pyuic5 is run again.
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 330)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.label.setObjectName("label")
        self.inputField = QtWidgets.QLineEdit(self.centralwidget)
        self.inputField.setGeometry(QtCore.QRect(40, 10, 231, 20))
        self.inputField.setObjectName("inputField")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(310, 10, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 31, 16))
        self.label_2.setObjectName("label_2")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(430, 10, 111, 23))
        self.convertButton.setObjectName("convertButton")
        self.intOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.intOutput.setGeometry(QtCore.QRect(10, 60, 121, 261))
        self.intOutput.setReadOnly(True)
        self.intOutput.setObjectName("intOutput")
        self.intOutput.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.binOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.binOutput.setGeometry(QtCore.QRect(140, 60, 271, 261))
        self.binOutput.setReadOnly(True)
        self.binOutput.setObjectName("binOutput")
        self.binOutput.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.hexOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.hexOutput.setGeometry(QtCore.QRect(420, 60, 121, 261))
        self.hexOutput.setReadOnly(True)
        self.hexOutput.setObjectName("hexOutput")
        self.hexOutput.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 121, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 40, 271, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 40, 121, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Base Converter Tool"))
        self.label.setText(_translate("MainWindow", "Input:"))
        self.label_2.setText(_translate("MainWindow", "Type:"))
        self.convertButton.setText(_translate("MainWindow", "Convert"))
        self.label_3.setText(_translate("MainWindow", "Integer"))
        self.label_4.setText(_translate("MainWindow", "Binary"))
        self.label_5.setText(_translate("MainWindow", "Hex"))
