from PyQt5 import QtCore, QtGui, QtWidgets,uic
from emp_ispis2 import Ui_Form
from prod_ispis import Ui_Form2
from enter_new_employee2 import Ui_Enter_employee
from change_employee_info2 import Ui_Change_employee
from delete_entry import Ui_delete_employee
from enter_new_product import Ui_Enter_product
import sys
from change_product_info import Ui_Change_product



class Ui_GlavniProzor(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/mainWin.ui",self)
        self.show()

        
        self.openTableEmployee = Ui_Form(self)
        self.openTableProduct = Ui_Form2(self)
        
        self.enterNewE.clicked.connect(self.openWinEnterNewEmployee)
        self.changeEmpInfo.clicked.connect(self.openWinEnterChangeEmployee)
        self.deleteEmpInfo.clicked.connect(self.openWinDeleteEmployee)
        self.pushButton_close.clicked.connect(self.closeing)

        self.enterNewP_2.clicked.connect(self.openWinEnterNewProduct)
        self.changeProductInfo_2.clicked.connect(self.openWinChangeProduct)

        
    
    def openWinEnterNewEmployee(self):
        
        self.win = Ui_Enter_employee()
        self.win.show()

    def openWinEnterChangeEmployee(self):
        
        self.win = Ui_Change_employee()
        self.win.show()

    def openWinDeleteEmployee(self):
        self.win = Ui_delete_employee()
        self.win.show()

    def closeing(self):
        self.close()

    def openWinEnterNewProduct(self):
        self.win =Ui_Enter_product()
        self.win.show()

    def openWinChangeProduct(self):
        self.win = Ui_Change_product()
        self.win.show()
        


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_GlavniProzor()
    myapp.show
    sys.exit(app.exec_())
