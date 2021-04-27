from PyQt5 import QtCore, QtGui, QtWidgets,uic
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
import sys



class Ui_Change_supplier(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Ui_Change_supplier, self).__init__(parent)
        uic.loadUi("ui/changeSupplier.ui",self)
        self.show()
        
        #self.ismet = QtWidgets.QLabel(self.parent, text = "Nesto")
        
              
        self.pushButton_saveS.clicked.connect(self.change_product)
        self.pushButton_saveS.clicked.connect(self.message_reg)
        self.pushButton_saveS.clicked.connect(self.closeing)
        
    def initWIndow(self):
        self.lineEdit_ID = QtWidgets.QLineEdit(self)
        self.lineEdit_SuppName = QtWidgets.QLineEdit(self)
        self.lineEdit_supp_loc = QtWidgets.QLineEdit(self)
        self.lineEdit_supp_address = QtWidgets.QLineEdit(self)  
        

    def change_product(self):
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mismet1985",
        database = "the_warehouse"
        )

        mycursor = mydb.cursor()

        supplier_to_c = self.lineEdit_ID.text()
        name = self.lineEdit_SuppName.text()
        location = self.lineEdit_supp_loc.text()
        address = self.lineEdit_supp_address.text()
                
        sql_update_supplier = "UPDATE supplier SET supplier_name = %s, supplier_location = %s ,supplier_address = %s WHERE idsupplier = %s"
        values = (name,location,address,supplier_to_c)
        mycursor.execute(sql_update_supplier, values)
        mydb.commit()


    def message_reg(self):
        msg = QMessageBox()
        msg.setWindowTitle("Enter")
        msg.setText("New supplier informations saved to system!")
        x = msg.exec_()

    def closeing(self):
        self.close()


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_Change_supplier()
    myapp.show
    sys.exit(app.exec_())


