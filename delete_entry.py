from PyQt5 import QtCore, QtGui, QtWidgets,uic

import mysql.connector
from PyQt5.QtWidgets import QMessageBox
import sys


class Ui_delete_employee(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Ui_delete_employee, self).__init__(parent)
        uic.loadUi("ui/delete_employee_Form.ui",self)
        self.show()
        
        #self.ismet = QtWidgets.QLabel(self.parent, text = "Nesto")
       
        self.pushButton_delete.clicked.connect(self.delete_employee)
        self.pushButton_delete.clicked.connect(self.message_reg)
        self.pushButton_delete.clicked.connect(self.closeing)

    def initWIndow(self):
        self.lineEdit_EID = QtWidgets.QLineEdit(self)

    def delete_employee(self):
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mismet1985",
        database = "the_warehouse"
        )

        mycursor = mydb.cursor()
        
        employee_to_erase=self.lineEdit_EID.text()
        
        sql_erase_employee = "DELETE FROM employees WHERE idemployees = %s"
        values = (employee_to_erase,)
        mycursor.execute(sql_erase_employee, values)
        mydb.commit()
    
    def message_reg(self):
        msg = QMessageBox()
        msg.setWindowTitle("Enter")
        msg.setText("Employee deleted!")
        x = msg.exec_()

    def closeing(self):
        self.close()


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_delete_employee()
    myapp.show
    sys.exit(app.exec_())
        

    
        


