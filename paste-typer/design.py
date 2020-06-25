# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(499, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_mainarea = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mainarea.setObjectName("horizontalLayout_mainarea")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_mainarea.addWidget(self.plainTextEdit)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnAddToHistory = QtWidgets.QToolButton(self.centralwidget)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.btnAddToHistory.setIcon(icon)
        self.btnAddToHistory.setObjectName("btnAddToHistory")
        self.verticalLayout_2.addWidget(self.btnAddToHistory)
        self.btnClearText = QtWidgets.QToolButton(self.centralwidget)
        self.btnClearText.setToolTip("")
        icon = QtGui.QIcon.fromTheme("edit-clear")
        self.btnClearText.setIcon(icon)
        self.btnClearText.setObjectName("btnClearText")
        self.verticalLayout_2.addWidget(self.btnClearText)
        self.horizontalLayout_mainarea.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_mainarea)
        self.horizontalLayout_buttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName("horizontalLayout_buttons")
        self.select_window_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_window_btn.setObjectName("select_window_btn")
        self.horizontalLayout_buttons.addWidget(self.select_window_btn)
        self.simulateTypeButton = QtWidgets.QPushButton(self.centralwidget)
        self.simulateTypeButton.setObjectName("simulateTypeButton")
        self.horizontalLayout_buttons.addWidget(self.simulateTypeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_buttons)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 499, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Paste typer"))
        self.label_2.setText(_translate("MainWindow", "History"))
        self.label.setText(_translate("MainWindow", "Enter the text you want to be typed:"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Enter text here"))
        self.btnAddToHistory.setText(_translate("MainWindow", "..."))
        self.btnClearText.setText(_translate("MainWindow", "..."))
        self.select_window_btn.setText(_translate("MainWindow", "Select target window"))
        self.simulateTypeButton.setText(_translate("MainWindow", "Simulate pasting text"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))