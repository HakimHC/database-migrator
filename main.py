from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui

from database_migrator import ss_to_mongo


class MyGui(QMainWindow):
    def __init__(self):
        super(MyGui, self).__init__()
        uic.loadUi('main_window.ui', self)

        self.setWindowIcon(QtGui.QIcon('logo.svg'))

        self.show()

        self.setWindowTitle('SQL to MongoDB')

        self.pushButton.clicked.connect(self.onClick)

    def onClick(self):
        if len(self.sqlcon.text()) < 1 or len(self.mongocon.text()) < 1 or len(self.dbn.text()) < 1:
            msg = QMessageBox() 
            msg.setWindowIcon(QtGui.QIcon('logo.svg'))
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Some fields are missing information. ")
            msg.setWindowTitle("Error")

            retval = msg.exec_()
        else:
            sqlcon = self.sqlcon.text()
            mongocon = self.mongocon.text()
            dbn = self.dbn.text()

            try:
                ss_to_mongo(sql_connection_string=sqlcon, mongo_conn=mongocon, database_name=dbn)
                msg = QMessageBox() 
                msg.setWindowIcon(QtGui.QIcon('logo.svg'))
                msg.setIcon(QMessageBox.Information)
                msg.setText("Succesful.")
                msg.setWindowTitle(":D")

                msg.exec()
                

            except:
                msg = QMessageBox() 
                msg.setWindowIcon(QtGui.QIcon('logo.svg'))
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error. ")
                msg.setWindowTitle("Error")

                msg.exec()


def main():
    app = QApplication([])
    window = MyGui()
    app.exec_()

if __name__ == '__main__':
    main()