from PyQt5 import QtCore, QtGui, QtWidgets,uic
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
import sys



class Ui_Register_user(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Ui_Register_user, self).__init__(parent)
        uic.loadUi("ui/register.ui",self)
        self.show()
        
        #self.ismet = QtWidgets.QLabel(self.parent, text = "Nesto")
        
              
        self.pushButton_register.clicked.connect(self.enter_employee)
        self.pushButton_register.clicked.connect(self.message_reg)
        self.pushButton_register.clicked.connect(self.closeing)
        
    def initWIndow(self):
        self.lineEdit_name = QtWidgets.QLineEdit(self)
        self.lineEdit_last_name = QtWidgets.QLineEdit(self)
        self.lineEdit_address = QtWidgets.QLineEdit(self)
        self.lineEdit_sector = QtWidgets.QLineEdit(self)
        self.lineEdit_permisions = QtWidgets.QLineEdit(self)
        self.lineEdit_username = QtWidgets.QLineEdit(self)
        self.lineEdit_password = QtWidgets.QLineEdit(self)
        

    def enter_employee(self):
        
        
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mismet1985",
        database = "the_warehouse"
        )

        mycursor = mydb.cursor()

        name = self.lineEdit_name.text()
        last_name = self.lineEdit_last_name.text()
        address = self.lineEdit_address.text()
        sector = self.lineEdit_sector.text()
        permisions = self.lineEdit_permisions.text()
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        

        sql_register = "INSERT INTO employees (employee_name,employee_last_name,employee_address,employee_sector,idpermisions,employee_username,employee_password) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values = (name,last_name,address,sector,permisions,username,password)
        mycursor.execute(sql_register, values)
        mydb.commit()


    def message_reg(self):
        msg = QMessageBox()
        msg.setWindowTitle("Enter")
        msg.setText("New employee saved to system!")
        msg = msg.exec_()

    def closeing(self):
        self.close()


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_Register_user()
    myapp.show
    sys.exit(app.exec_())


