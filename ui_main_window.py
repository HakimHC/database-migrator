# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\legol\Desktop\database_migration\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(777, 679)
        mainWindow.setStyleSheet("QWidget {\n"
"    background-color: #212121;\n"
"    color: #ffffff;\n"
"    font: 12pt \"Microsoft JhengHei UI\";\n"
"    font-weight: bold;\n"
"    border: 1px solid #ffffff;\n"
"    border-color: #1777ff;\n"
"    padding: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: #2196f3;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 350, 479))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.sqlcon = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.sqlcon.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.sqlcon.setObjectName("sqlcon")
        self.verticalLayout.addWidget(self.sqlcon)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.mongocon = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.mongocon.setObjectName("mongocon")
        self.verticalLayout.addWidget(self.mongocon)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.dbn = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.dbn.setObjectName("dbn")
        self.verticalLayout.addWidget(self.dbn)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 455, 361, 63))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 40, 361, 401))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 68))
        self.menubar.setObjectName("menubar")
        self.menuSQL_SERVER_TO_MONGODB_MIGRATOR = QtWidgets.QMenu(self.menubar)
        self.menuSQL_SERVER_TO_MONGODB_MIGRATOR.setObjectName("menuSQL_SERVER_TO_MONGODB_MIGRATOR")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSQL_SERVER_TO_MONGODB_MIGRATOR.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label.setText(_translate("mainWindow", "SQL SERVER CONNECTION STRING"))
        self.label_2.setText(_translate("mainWindow", "MONGODB CONNECTION STRING"))
        self.label_3.setText(_translate("mainWindow", "NEW DATABASE NAME"))
        self.pushButton.setText(_translate("mainWindow", "PushButton"))
        self.label_4.setText(_translate("mainWindow", "This application uses PyODBC to get \n"
"all the information from a \n"
"SQL Server Database \n"
"(every table, and all data they contain)\n"
"and copies all the data to a \n"
"new MongoDB database.\n"
"Currently it only supports \n"
"SQL Server and only with \n"
"ODBC connection strings, \n"
"this is the first version.\n"
""))
        self.menuSQL_SERVER_TO_MONGODB_MIGRATOR.setTitle(_translate("mainWindow", "SQL SERVER TO MONGODB MIGRATOR"))
