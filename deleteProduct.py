from PyQt5 import QtCore, QtGui, QtWidgets,uic

import mysql.connector

from PyQt5.QtWidgets import QMessageBox
import sys

class Ui_delete_product(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Ui_delete_product, self).__init__(parent)
        uic.loadUi("ui/delete_product_Form.ui",self)
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
        
        product_to_delete=self.lineEdit_PID.text()
        
        sql_erase_product = "DELETE FROM products WHERE idproducts = %s"
        values = (product_to_delete,)
        mycursor.execute(sql_erase_product, values)
        mydb.commit()
    
    def message_reg(self):
        msg = QMessageBox()
        msg.setWindowTitle("Enter")
        msg.setText("Product deleted!")
        x = msg.exec_()

    def closeing(self):
        self.close()


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_delete_product()
    myapp.show
    sys.exit(app.exec_())


