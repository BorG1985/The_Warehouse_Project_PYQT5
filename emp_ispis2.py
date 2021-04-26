from PyQt5 import QtCore, QtGui, QtWidgets,uic

import mysql.connector


class Ui_Form(QtWidgets.QMainWindow):
    def __init__(self,parent):
        super().__init__()
        
        self.parent = parent
        #self.ismet = QtWidgets.QLabel(self.parent, text = "Nesto")
        self.tabela_ispis = QtWidgets.QTableWidget(50, 8, self)
       
        self.parent.ispisBtn.clicked.connect(self.tabela)
        #self.parent.pushButton.clicked.connect(self.nova2)


    # def nova(self):
    #     self.parent.label.setText('Blabla')        

    # def nova2(self):
    #     self.parent.naziv.setText("Mikrofon")

    def tabela(self):        
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mismet1985",
        database = "the_warehouse"
        )

        mycursor = mydb.cursor()

        sql_list = "SELECT * FROM employees"
        mycursor.execute(sql_list)

        emp_list = mycursor.fetchall()
        self.parent.tabela_ispis.setRowCount(0)

        for row_number, row_data in enumerate(emp_list):
            self.parent.tabela_ispis.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.parent.tabela_ispis.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))


