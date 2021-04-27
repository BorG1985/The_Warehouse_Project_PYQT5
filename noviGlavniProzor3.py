from PyQt5 import QtCore, QtGui, QtWidgets,uic
from emp_ispis2 import Ui_Form
from prod_ispis import Ui_Form2
from supplier_ispis import Ui_Form3
from enter_new_employee2 import Ui_Enter_employee
from enter_new_supplier import Ui_Enter_supplier
from change_employee_info2 import Ui_Change_employee
from change_supplier_info import Ui_Change_supplier
from delete_entry import Ui_delete_employee
from enter_new_product import Ui_Enter_product
from deleteProduct import Ui_delete_product
from deleteSupplier import Ui_delete_supplier
import sys
from change_product_info import Ui_Change_product



class Ui_GlavniProzor(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/mainWin.ui",self)
        self.show()

        
        self.openTableEmployee = Ui_Form(self)
        self.openTableProduct = Ui_Form2(self)
        self.openTableSuppliers = Ui_Form3(self)
        
        self.enterNewE.clicked.connect(self.openWinEnterNewEmployee)
        self.changeEmpInfo.clicked.connect(self.openWinEnterChangeEmployee)
        self.deleteEmpInfo.clicked.connect(self.openWinDeleteEmployee)
        self.pushButton_close.clicked.connect(self.closeing)

        self.enterNewP_2.clicked.connect(self.openWinEnterNewProduct)
        self.changeProductInfo_2.clicked.connect(self.openWinChangeProduct)
        self.deleteProInfo_2.clicked.connect(self.openWindeleteProduct)

        self.enterNewSup.clicked.connect(self.openWinEnterNewSupplier)
        self.changeSupplierInfo.clicked.connect(self.openWinchangeSupplier)
        self.deleteSupInfo.clicked.connect(self.openWindeleteSupplier)

        
    
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

    def openWindeleteProduct(self):
        self.win = Ui_delete_product()
        self.win.show()

    def openWinEnterNewSupplier(self):
        self.win = Ui_Enter_supplier()
        self.win.show()
    
    def openWinchangeSupplier(self):
        self.win = Ui_Change_supplier()
        self.win.show()
    
    def openWindeleteSupplier(self):
        self.win = Ui_delete_supplier()
        self.win.show()
        


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_GlavniProzor()
    myapp.show
    sys.exit(app.exec_())
