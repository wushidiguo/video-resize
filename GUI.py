# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hm115177\desktop\\program\\image_resize\\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 533)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(280, 60, 471, 371))
        self.image.setText("")
        self.image.setObjectName("image")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 30, 62, 15))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(21, 61, 171, 149))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.open = QtWidgets.QPushButton(self.widget)
        self.open.setObjectName("open")
        self.verticalLayout_3.addWidget(self.open)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.h_size = QtWidgets.QLineEdit(self.widget)
        self.h_size.setObjectName("h_size")
        self.verticalLayout_2.addWidget(self.h_size)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.v_size = QtWidgets.QLineEdit(self.widget)
        self.v_size.setObjectName("v_size")
        self.verticalLayout.addWidget(self.v_size)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.preview = QtWidgets.QPushButton(self.widget)
        self.preview.setObjectName("preview")
        self.horizontalLayout.addWidget(self.preview)
        self.save = QtWidgets.QPushButton(self.widget)
        self.save.setObjectName("save")
        self.horizontalLayout.addWidget(self.save)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Preview"))
        self.open.setText(_translate("MainWindow", "Open Image"))
        self.label_2.setText(_translate("MainWindow", "Width"))
        self.label_3.setText(_translate("MainWindow", "Height"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Resize Only"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Resize to Height"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Resize to Width"))
        self.preview.setText(_translate("MainWindow", "Preview"))
        self.save.setText(_translate("MainWindow", "Save Image"))


