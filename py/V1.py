import database as db
from Ventana1 import *
from pantalla_actu import *
import imags_rc
import sys
from PyQt5.QtWidgets import QWidget, QTableWidget,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pymongo import MongoClient
import database as db
from pantalla_insertar import *
from Ventana1 import *


class Ui_MainWindow(object):

    def abrir_modificar(self,i):
        ventana = updateWindow().exec_()

    def abrir_insertar(self):
        ventana = insertWindow().exec_()

    def eliminar(self):
    	row = self.tableWidget.currentRow()
    	if row >= 0:
    		msg = QMessageBox()
    		msg.setIcon(QMessageBox.Question)
    		msg.setText("Desea eliminar este registro")
    		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
    		reply = msg.exec_()
    		
    		if reply == QMessageBox.Yes:
    			pais = (self.tableWidget.item(row, 0).text())
    			sexo = (self.tableWidget.item(row, 2).text())
    			edad = (self.tableWidget.item(row, 3).text())
    			gene = (self.tableWidget.item(row, 8).text())
    			num = db.delete(pais,sexo,edad,gene)

    			if num > 0:
    				mensaje=QMessageBox()
    				mensaje.setText("Registro eliminado")
    				mensaje.exec_()
    				self.obtener()

    	else:
    		mensaje=QMessageBox()
    		mensaje.setText("Selecciona una fila de la tabla")
    		mensaje.exec_()

    def obtener(self):
        a = db.findAll().limit(50)

        for i, rates in enumerate(a):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(rates["country"]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(rates["year"])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(rates["sex"]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(rates["age"]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(rates["suicides_no"])))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(rates["population"])))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(rates["suicides_per_100k"])))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(str(rates["gdp_per_capita"])))
            self.tableWidget.setItem(i, 8, QTableWidgetItem(rates["generation"]))

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
        self.btconsultar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.btmodificar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.bteliminar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.bteliminar.clicked.connect(self.eliminar)
        self.btinsertar = QtWidgets.QPushButton(self.centralwidget)
        self.btinsertar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.btinsertar.clicked.connect(self.abrir_insertar)
        
        self.btmodificar.clicked.connect(self.abrir_modificar)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 0, 550, 41))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(250, 40, 926, 477))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setFont(font)

        self.tableWidget.setStyleSheet("background-color:rgb(255, 255, 255);\n"
        "gridline-color: rgb(0, 107, 189);\n"
        "selection-background-color: rgb(85, 170, 255);\n"
        "border-color: rgb(255, 0, 4);")

        self.tableWidget.setGridStyle(QtCore.Qt.DashDotLine)
        stylesheet = "::section{Background-color:rgb(0, 107, 189);border-radius:14px;}"
        self.tableWidget.horizontalHeader().setStyleSheet(stylesheet)
        self.tableWidget.verticalHeader().setStyleSheet(stylesheet)

        self.tableWidget.setHorizontalHeaderLabels(("Pais","Año","Sexo","Edad","No. Suicidios","Poblacion","suicides_per_100k","gdp_per_capita","generation"))

        MainWindow.setCentralWidget(self.centralwidget)
        
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
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
