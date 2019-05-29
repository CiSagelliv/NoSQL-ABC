"""
  Interfaz gráfica para actualización de datos 
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidget, QAction, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Actualizar datos"
        self.left = 0
        self.top = 0
        self.width = 550
        self.height = 570
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 

        self.show()

    def createTable(self):
        #Creamos la tabla
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setHorizontalHeaderLabels(["_id","country","year","sex","age","suicides_no","population","suicides_per_100k","country_year","HDI_for_year","gdp_for_year","gdp_per_capita","generation"])
        self.tableWidget.move(0,0)

"""

        Aún no sé pa' que sirve esto :c

        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

