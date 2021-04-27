from PyQt5 import QtCore, QtGui, QtWidgets,uic
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
import sys



class Ui_Enter_supplier(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Ui_Enter_supplier, self).__init__(parent)
        uic.loadUi("ui/newSupplier.ui",self)
        self.show()
        
        #self.ismet = QtWidgets.QLabel(self.parent, text = "Nesto")
        
              
        self.pushButton_saveSupp.clicked.connect(self.enter_new_product)
        self.pushButton_saveSupp.clicked.connect(self.message_reg)
        self.pushButton_saveSupp.clicked.connect(self.closeing)
        
    def initWIndow(self):
        self.lineEdit_name = QtWidgets.QLineEdit(self)
        self.lineEdit_location = QtWidgets.QLineEdit(self)
        self.lineEdit_address = QtWidgets.QLineEdit(self)

    def enter_new_product(self):
        
        
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mismet1985",
        database = "the_warehouse"
        )

        mycursor = mydb.cursor()

        name = self.lineEdit_name.text()
        location = self.lineEdit_location.text()
        address = self.lineEdit_address.text()

        

        sql_enter_supplier = "INSERT INTO supplier (supplier_name,supplier_location,supplier_address) VALUES (%s,%s,%s)"
        values = (name,location,address)
        mycursor.execute(sql_enter_supplier, values)
        mydb.commit()


    def message_reg(self):
        msg = QMessageBox()
        msg.setWindowTitle("Enter")
        msg.setText("New Supplier saved to system!")
        x = msg.exec_()

    def closeing(self):
        self.close()


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_Enter_supplier()
    myapp.show
    sys.exit(app.exec_())


