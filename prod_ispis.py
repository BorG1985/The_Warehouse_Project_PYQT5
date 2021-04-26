from PyQt5 import QtCore, QtGui, QtWidgets,uic
import mysql.connector


class Ui_Form2(QtWidgets.QMainWindow):
    def __init__(self,parent):
        super().__init__()
        
        self.parent = parent
        #self.ismet = QtWidgets.QLabel(self.parent, text = "Nesto")
        self.tabela_ispis2 = QtWidgets.QTableWidget(50, 7, self)
       
        self.parent.ispisBtn_2.clicked.connect(self.tabela2)
        #self.parent.pushButton.clicked.connect(self.nova2)


    # def nova(self):
    #     self.parent.label.setText('Blabla')        

    # def nova2(self):
    #     self.parent.naziv.setText("Mikrofon")

    def tabela2(self):        
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mismet1985",
        database = "the_warehouse"
        )

        mycursor = mydb.cursor()

        sql_list = "SELECT * FROM products"
        mycursor.execute(sql_list)

        pro_list = mycursor.fetchall()
        self.parent.tabela_ispis2.setRowCount(0)

        for row_number, row_data in enumerate(pro_list):
            self.parent.tabela_ispis2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.parent.tabela_ispis2.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))


