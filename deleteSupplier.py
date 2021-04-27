from PyQt5 import QtCore, QtGui, QtWidgets,uic

import mysql.connector

from PyQt5.QtWidgets import QMessageBox
import sys

class Ui_delete_supplier(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Ui_delete_supplier, self).__init__(parent)
        uic.loadUi("ui/delete_supplier_Form.ui",self)
        self.show()
        
        #self.ismet = QtWidgets.QLabel(self.parent, text = "Nesto")
       
        self.pushButton_delete.clicked.connect(self.delete_product)
        self.pushButton_delete.clicked.connect(self.message_reg)
        self.pushButton_delete.clicked.connect(self.closeing)

    def initWIndow(self):
        self.lineEdit_PID = QtWidgets.QLineEdit(self)

    def delete_product(self):
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mismet1985",
        database = "the_warehouse"
        )

        mycursor = mydb.cursor()
        
        supplier_to_delete=self.lineEdit_SID.text()
        
        sql_delete_supplier = "DELETE FROM supplier WHERE idsupplier = %s"
        values = (supplier_to_delete,)
        mycursor.execute(sql_delete_supplier, values)
        mydb.commit()
    
    def message_reg(self):
        msg = QMessageBox()
        msg.setWindowTitle("Enter")
        msg.setText("Supplier deleted!")
        x = msg.exec_()

    def closeing(self):
        self.close()


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_delete_supplier()
    myapp.show
    sys.exit(app.exec_())


