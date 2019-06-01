"""   
    Corrección de interfaz xD perdón chicos
"""

import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit, QTextEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import (pyqtSlot, pyqtSignal, Qt)

class updateWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.createWindow()

        self.setGeometry(300,0,550,570)
        self.setWindowTitle("Actualización de datos")
        self. show()

    def createWindow(self):

        lb_country = QLabel("Country")
        lb_year = QLabel("Year")
        lb_sex = QLabel("Sex")
        lb_age = QLabel("Age")
        lb_suicides_no = QLabel("Suicides_no")
        lb_population = QLabel("Population")
        lb_suicides_per_100k = QLabel("Suicides_per_100k")
        lb_country_year = QLabel("Country_year")
        lb_HDI_for_year = QLabel("HDI_for_year")
        lb_gdp_for_year = QLabel("gdp_for_year")
        lb_gdp_per_capita = QLabel("Cgdp_per_capita")
        lb_generation = QLabel("Generation")

        txt_country = QLineEdit(self)
        txt_year = QLineEdit(self)
        txt_sex = QLineEdit(self)
        txt_age = QLineEdit(self)
        txt_suicides_no = QLineEdit(self)
        txt_population = QLineEdit(self)
        txt_suicides_per_100k = QLineEdit(self)
        txt_country_year = QLineEdit(self)
        txt_HDI_for_year = QLineEdit(self)
        txt_gdp_for_year = QLineEdit(self)
        txt_gdp_per_capita = QLineEdit(self)
        txt_generation = QLineEdit(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = updateWindow()
    sys.exit(app.exec())



