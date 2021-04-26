from PyQt5 import QtCore, QtGui, QtWidgets,uic
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
from registerUser import Ui_Register_user
import sys,os



class Ui_login(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Ui_login, self).__init__(parent)
        uic.loadUi("ui/login.ui",self)
        self.show()
        
        #self.ismet = QtWidgets.QLabel(self.parent, text = "Nesto")
        
              
        self.pushButton_login.clicked.connect(self.login)
        #self.pushButton_login.clicked.connect(self.message_login)
        self.pushButton_login.clicked.connect(self.closeing)
        self.pushButton_login.clicked.connect(self.openMain)
        self.push_Rigister.clicked.connect(self.openWinRegistration)
        
    
    def initWIndow(self):
        self.line_username = QtWidgets.QLineEdit(self)
        self.line_password = QtWidgets.QLineEdit(self)


    def login(self):
        username = self.line_username.text()
        password = self.line_password.text()

        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mismet1985",
        database = "the_warehouse"
        )

        mycursor = mydb.cursor()
        sql_authentication = "SELECT * FROM employees WHERE employee_username = %s AND employee_password = %s"
        values = (username, password)
        mycursor.execute(sql_authentication,values)

        account = mycursor.fetchall()

        for i in account:
            employee_name = i[1]
            employee_last_name = i[2]
            employee_username = i[6]
            employee_password = i[7]
            idpermisions = i[5]
        
        if username == employee_username and password == employee_password:
            self.message_login()        
        else:
            self.message_errorlogin()
    
    # def register(self):
    #     try:
    #         os.system('registerUser.py')
        
    #     except:
    #         print("error")
    
    def message_login(self):
        msg = QMessageBox()
        msg.setWindowTitle("Login")
        msg.setText("You are logged in!")
        x = msg.exec_()

    def message_errorlogin(self):
        msg = QMessageBox()
        msg.setWindowTitle("Atention!")
        msg.setText("Username or password are incorrect!")
        x = msg.exec_()
    
    def openMain(self):
        os.system("noviGlavniProzor3.py")
    
    def closeing(self):
        self.close()

    def openWinRegistration(self):
        
        self.win = Ui_Register_user()
        self.win.show()
    

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_login()
    myapp.show
    sys.exit(app.exec_())
        