from PyQt5 import QtCore, QtGui, QtWidgets,uic
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
import sys



class Ui_Change_product(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Ui_Change_product, self).__init__(parent)
        uic.loadUi("ui/changeProduct.ui",self)
        self.show()
        
        #self.ismet = QtWidgets.QLabel(self.parent, text = "Nesto")
        
              
        self.pushButton_saveP.clicked.connect(self.change_product)
        self.pushButton_saveP.clicked.connect(self.message_reg)
        self.pushButton_saveP.clicked.connect(self.closeing)
        
    def initWIndow(self):
        self.lineEdit_ID = QtWidgets.QLineEdit(self)
        self.lineEdit_Pname = QtWidgets.QLineEdit(self)
        self.lineEdit_ptype = QtWidgets.QLineEdit(self)
        self.lineEdit_pcode = QtWidgets.QLineEdit(self)        
        self.lineEdit_pquantity = QtWidgets.QLineEdit(self)
        self.lineEdit_psupplier = QtWidgets.QLineEdit(self)
        self.lineEdit_pprice = QtWidgets.QLineEdit(self)
        

    def change_product(self):
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mismet1985",
        database = "the_warehouse"
        )

        mycursor = mydb.cursor()

        product_to_c = self.lineEdit_ID.text()
        name = self.lineEdit_Pname.text()
        ptype = self.lineEdit_ptype.text()
        code = self.lineEdit_pcode.text()
        quantity = self.lineEdit_pquantity.text()
        supplier = self.lineEdit_psupplier.text()
        price = self.lineEdit_pprice.text()
                
        sql_update_product = "UPDATE products SET product_name = %s, idproduct_type = %s ,product_code = %s ,product_quantity = %s ,idsupplier = %s,product_price = %s WHERE idproducts = %s"
        values = (name,ptype,code,quantity,supplier,price,product_to_c)
        mycursor.execute(sql_update_product, values)
        mydb.commit()


    def message_reg(self):
        msg = QMessageBox()
        msg.setWindowTitle("Enter")
        msg.setText("New employee informations saved to system!")
        x = msg.exec_()

    def closeing(self):
        self.close()


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_Change_product()
    myapp.show
    sys.exit(app.exec_())


