from PyQt5 import QtCore, QtGui, QtWidgets,uic
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
import sys



class Ui_Change_employee(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Ui_Change_employee, self).__init__(parent)
        uic.loadUi("ui/change_employee_info.ui",self)
        self.show()
        
        #self.ismet = QtWidgets.QLabel(self.parent, text = "Nesto")
        
              
        self.pushButton_save_changes_employee.clicked.connect(self.change_employee)
        self.pushButton_save_changes_employee.clicked.connect(self.message_reg)
        self.pushButton_save_changes_employee.clicked.connect(self.closeing)
        
    def initWIndow(self):
        self.lineEdit_employee_ID = QtWidgets.QLineEdit(self)
        self.lineEdit_name = QtWidgets.QLineEdit(self)
        self.lineEdit_last_name = QtWidgets.QLineEdit(self)
        self.lineEdit_address = QtWidgets.QLineEdit(self)
        self.lineEdit_sector = QtWidgets.QLineEdit(self)
        self.lineEdit_permisions = QtWidgets.QLineEdit(self)
        self.lineEdit_username = QtWidgets.QLineEdit(self)
        self.lineEdit_password = QtWidgets.QLineEdit(self)
        

    def change_employee(self):
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mismet1985",
        database = "the_warehouse"
        )

        mycursor = mydb.cursor()

        employee_to_c = self.lineEdit_employee_ID.text()
        name = self.lineEdit_name.text()
        last_name = self.lineEdit_last_name.text()
        address = self.lineEdit_address.text()
        sector = self.lineEdit_sector.text()
        permisions = self.lineEdit_permisions.text()
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

                
        sql_update_employee = "UPDATE employees SET employee_name = %s ,employee_last_name = %s,employee_address = %s,employee_sector = %s,idpermisions = %s,employee_username = %s,employee_password = %s WHERE idemployees = %s"
        values = (name,last_name,address,sector,permisions,username,password,employee_to_c)
        mycursor.execute(sql_update_employee, values)
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
    myapp = Ui_Change_employee()
    myapp.show
    sys.exit(app.exec_())


