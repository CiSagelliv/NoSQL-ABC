"""   
    Corrección de interfaz xD perdón chicos
"""

import sys
from PyQt5.QtWidgets import (QVBoxLayout, QApplication, QDialog, QLabel, QLineEdit, QTextEdit, QPushButton, QMessageBox, QGridLayout)
from PyQt5.QtCore import (pyqtSlot, pyqtSignal, Qt)


class updateWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setLayout(QVBoxLayout())

        self.layout().addLayout(self.createWindow())
        self.layout().addWidget(self.updateButton())
        self.setGeometry(300, 0, 450, 0)
        self.setWindowTitle("Actualización de datos")
        self.show()

    def createWindow(self):
        grid = QGridLayout()

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

        self.txt_country = QLineEdit(self)
        self.txt_year = QLineEdit(self)
        self.txt_sex = QLineEdit(self)
        self.txt_age = QLineEdit(self)
        self.txt_suicides_no = QLineEdit(self)
        self.txt_population = QLineEdit(self)
        self.txt_suicides_per_100k = QLineEdit(self)
        self.txt_country_year = QLineEdit(self)
        self.txt_HDI_for_year = QLineEdit(self)
        self.txt_gdp_for_year = QLineEdit(self)
        self.txt_gdp_per_capita = QLineEdit(self)
        self.txt_generation = QLineEdit(self)

        grid.addWidget(lb_country, 0, 0)
        grid.addWidget(lb_year, 1, 0)
        grid.addWidget(lb_sex, 2, 0)
        grid.addWidget(lb_age, 3, 0)
        grid.addWidget(lb_suicides_no, 4, 0)
        grid.addWidget(lb_population, 5, 0)
        grid.addWidget(lb_suicides_per_100k, 6, 0)
        grid.addWidget(lb_country_year, 7, 0)
        grid.addWidget(lb_HDI_for_year, 8, 0)
        grid.addWidget(lb_gdp_for_year, 9, 0)
        grid.addWidget(lb_gdp_per_capita, 10, 0)
        grid.addWidget(lb_generation, 11, 0)

        grid.addWidget(self.txt_country, 0, 1)
        grid.addWidget(self.txt_year, 1, 1)
        grid.addWidget(self.txt_sex, 2, 1)
        grid.addWidget(self.txt_age, 3, 1)
        grid.addWidget(self.txt_suicides_no, 4, 1)
        grid.addWidget(self.txt_population, 5, 1)
        grid.addWidget(self.txt_suicides_per_100k, 6, 1)
        grid.addWidget(self.txt_country_year, 7, 1)
        grid.addWidget(self.txt_HDI_for_year, 8, 1)
        grid.addWidget(self.txt_gdp_for_year, 9, 1)
        grid.addWidget(self.txt_gdp_per_capita, 10, 1)
        grid.addWidget(self.txt_generation, 11, 1)

        return grid

    def updateButton(self):
        buttonUpdate = QPushButton("Update", self)
        buttonUpdate.clicked.connect(self.updateData)
        return buttonUpdate

    def updateData(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = updateWindow()
    sys.exit(app.exec())







