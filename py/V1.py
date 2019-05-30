
from Ventana1 import *
import imags_rc
from pymongo import MongoClient
import sys
from PyQt5.QtWidgets import QWidget, QTableWidget,QTableWidgetItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Ui_MainWindow(object):

    def abrir(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=ventana2()
        self.ui.setupUi(self.ventana)

        self.ventana.show()

    
    def obtener(self):
        host = "localhost"
        puerto = "27017"
        usuario = "parzibyte"
        palabra_secreta = "hunter2"
        base_de_datos = "suicides"
        cliente = MongoClient("mongodb://{}:{}".format(host, puerto))
        base_de_datos1 = cliente[base_de_datos]
        a=base_de_datos1.rates.find({},{"_id":0,"country":1,"year":1,"sex":1,"age":1,"suicides_no":1,"population":1,"suicides_per_100k":1,"gdp_per_capita":1,"generation":1}).limit(20)
        i=0

        for rates in a:
            self.tableWidget.setItem(i,0, QTableWidgetItem(rates["country"]))
            self.tableWidget.setItem(i,1, QTableWidgetItem(str(rates["year"])))
            self.tableWidget.setItem(i,2, QTableWidgetItem(rates["sex"]))
            self.tableWidget.setItem(i,3, QTableWidgetItem(rates["age"]))
            self.tableWidget.setItem(i,4, QTableWidgetItem(str(rates["suicides_no"])))
            self.tableWidget.setItem(i,5, QTableWidgetItem(str(rates["population"])))
            self.tableWidget.setItem(i,6, QTableWidgetItem(str(rates["suicides_per_100k"])))
            self.tableWidget.setItem(i,7, QTableWidgetItem(str(rates["gdp_per_capita"])))
            self.tableWidget.setItem(i,8, QTableWidgetItem(rates["generation"]))

            i=i+1
        """self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(a):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
"""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1220, 550)
        MainWindow.setStyleSheet("background-color: rgb(222, 255, 253);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btconsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btconsultar.setGeometry(QtCore.QRect(10, 80, 231, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 107, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 107, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 107, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 107, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 107, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 107, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 107, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 107, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 107, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btconsultar.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btconsultar.setFont(font)
        self.btconsultar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btconsultar.setStyleSheet("background-color: rgb(0, 107, 189);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btconsultar.setIcon(icon)
        self.btconsultar.setIconSize(QtCore.QSize(50, 50))
        self.btconsultar.setCheckable(False)
        self.btconsultar.setChecked(False)
        self.btconsultar.setAutoDefault(True)
        self.btconsultar.setDefault(True)
        self.btconsultar.setFlat(False)
        self.btconsultar.setObjectName("btconsultar")
        self.btmodificar = QtWidgets.QPushButton(self.centralwidget)
        self.btmodificar.setGeometry(QtCore.QRect(10, 170, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btmodificar.setFont(font)
        self.btmodificar.setStyleSheet("background-color: rgb(0, 107, 189);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("actualizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btmodificar.setIcon(icon1)
        self.btmodificar.setIconSize(QtCore.QSize(50, 50))
        self.btmodificar.setObjectName("btmodificar")
        self.bteliminar = QtWidgets.QPushButton(self.centralwidget)
        self.bteliminar.setGeometry(QtCore.QRect(10, 260, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bteliminar.setFont(font)
        self.bteliminar.setStyleSheet("background-color: rgb(0, 107, 189);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap('borrar.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bteliminar.setIcon(icon2)
        self.bteliminar.setIconSize(QtCore.QSize(50, 50))
        self.bteliminar.setObjectName("bteliminar")
        self.btinsertar = QtWidgets.QPushButton(self.centralwidget)
        self.btinsertar.setGeometry(QtCore.QRect(10, 350, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btinsertar.setFont(font)
        self.btinsertar.setStyleSheet("background-color: rgb(0, 107, 189);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("modificar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btinsertar.setIcon(icon3)
        self.btinsertar.setIconSize(QtCore.QSize(50, 50))
        self.btinsertar.setObjectName("btinsertar")
        anio=1988
        
        self.btinsertar.clicked.connect(self.abrir)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 0, 550, 41))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(250, 40, 926, 477))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(("Pais","Año","Sexo","Edad","No. Suicidios","Poblacion","suicides_per_100k","gdp_per_capita","generation"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.obtener()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Inicio", "Inicio"))
        self.btconsultar.setText(_translate("MainWindow", "Consultar Datos"))
        self.btmodificar.setText(_translate("MainWindow", "Modificar Datos"))
        self.bteliminar.setText(_translate("MainWindow", "Eliminar Datos"))
        self.btinsertar.setText(_translate("MainWindow", "Insertar Datos"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; text-decoration: underline; color:#2b2828;\">MENU</span></p></body></html>"))
        
            
     


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

