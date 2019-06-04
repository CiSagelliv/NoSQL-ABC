import sys
import database as db
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu,
                             QActionGroup, QAction, QMessageBox, QLabel, QLineEdit, QComboBox)
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtCore import (pyqtSlot, pyqtSignal, Qt)


class consultarWidget(QDialog):
    def __init__(self, parent=None):
        super(consultarWidget, self).__init__(parent)

        self.setWindowTitle("Realizar consulta de datos")
        self.setWindowIcon(QIcon("Qt.png"))
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint |
                            Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(1200, 348)

        self.initUI()

    def initUI(self):

        self.tabla = QTableWidget(self)

        # Establecer el número de columnas
        self.tabla.setColumnCount(9)

        # Establecer el número de filas
        self.tabla.setRowCount(50)

        # Alineación del texto del encabezado
        self.tabla.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
                                                          Qt.AlignCenter)

        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.tabla.horizontalHeader().setHighlightSections(False)

        # Hacer que la última sección visible del encabezado ocupa todo el espacio disponible
        self.tabla.horizontalHeader().setStretchLastSection(True)

        # Ocultar encabezado vertical
        self.tabla.verticalHeader().setVisible(False)

        # Dibujar el fondo usando colores alternados
        self.tabla.setAlternatingRowColors(True)

        # Establecer altura de las filas
        self.tabla.verticalHeader().setDefaultSectionSize(20)
        
        # self.tabla.verticalHeader().setHighlightSections(True)
        nombreColumnas = ("País","Año","Sexo","Edad","No. de Suicidios","Población","suicides_per_100k","gdp_per_capita","Generación")

        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)
        
        # Menú contextual
        self.tabla.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabla.customContextMenuRequested.connect(self.menuContextual)
        
        # Establecer ancho de las columnas
        for indice, ancho in enumerate((120, 120, 120, 120, 120, 120, 120, 120, 120), start=0):
            self.tabla.setColumnWidth(indice, ancho)

            self.tabla.resize(1070, 240)
            self.tabla.move(20, 56)

    #Botones
        botonMostrarDatos = QPushButton("Mostrar datos", self)
        botonMostrarDatos.setFixedWidth(140)
        botonMostrarDatos.move(20, 20)

        botonBuscarDatos = QPushButton("Buscar", self)
        botonBuscarDatos.clicked.connect(self.Buscar)
        botonBuscarDatos.setFixedWidth(50)
        botonBuscarDatos.move(970, 20)

        EtiquetaBuscar = QLabel("Buscar: ", self)
        EtiquetaBuscar.setFixedWidth(50)
        EtiquetaBuscar.move(430, 19)

        self.EspacioTexto = QLineEdit(self)
        self.EspacioTexto.setFixedWidth(200)
        self.EspacioTexto.move(750, 20)
        
        

        self.comboBox = QComboBox(self)
        self.comboBox.setFixedWidth(200)
        self.comboBox.move(400,20)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Seleccione uno")
        self.comboBox.addItem("country")
        self.comboBox.addItem("year")
        self.comboBox.addItem("sex")
        self.comboBox.addItem("age")
        self.comboBox.addItem("population")
        self.comboBox.addItem("suicides_per_100k")
        self.comboBox.addItem("suicides_no")
        self.comboBox.addItem("generation")
        self.comboBox.addItem("gdp_per_capita")




        menu = QMenu()
        for indice, columna in enumerate(nombreColumnas, start=0):
            accion = QAction(columna, menu)
            accion.setCheckable(True)
            accion.setChecked(True)
            accion.setData(indice)

            menu.addAction(accion)

        botonMostrarOcultar = QPushButton("Motrar/ocultar columnas", self)
        botonMostrarOcultar.setFixedWidth(180)
        botonMostrarOcultar.setMenu(menu)
        botonMostrarOcultar.move(170, 20)

        botonCerrar = QPushButton("Cerrar", self)
        botonCerrar.setFixedWidth(80)
        botonCerrar.move(1000, 306)

        #eventos de botones
        botonMostrarDatos.clicked.connect(self.datosTabla)
        botonCerrar.clicked.connect(self.close)
        botonBuscarDatos.clicked.connect(self.on_click)
        self.EspacioTexto.textChanged.connect(self.on_click)

        menu.triggered.connect(self.mostrarOcultar)
        
    
    @pyqtSlot()
    def on_click(self):
        try:
            textboxValue = self.EspacioTexto.text()
            item = self.comboBox.currentText()
        
            if(item=="year"):
                b=int(textboxValue)
                a = db.find(item,b).limit(50)
            elif(item=="suicides_no"):
                b=int(textboxValue)
                a = db.find(item,b).limit(50)
            elif(item=="population"):
                b=int(textboxValue)
                a = db.find(item,b).limit(50)
            elif(item=="suicides_per_100k"):
                b=float(textboxValue)
                a = db.find(item,b).limit(50)
            elif(item=="gdp_per_capita"):
                b=int(textboxValue)
                a = db.find(item,b).limit(50)
            elif(item=="generation"):
                b=int(textboxValue)
                a = db.find(item,b).limit(50)
            elif(item=="age"):
                print("ffgdfgfd")
                b= {'$regex': textboxValue}
                a = db.find(item,b).limit(50)
                
            else:
                a = db.find(item,textboxValue).limit(50)


            for i, rates in enumerate (a):
                self.tabla.setItem(i,0, QTableWidgetItem(rates["country"]))
                self.tabla.setItem(i,1, QTableWidgetItem(str(rates["year"])))
                self.tabla.setItem(i,2, QTableWidgetItem(rates["sex"]))
                self.tabla.setItem(i,3, QTableWidgetItem(rates["age"]))
                self.tabla.setItem(i,4, QTableWidgetItem(str(rates["suicides_no"])))
                self.tabla.setItem(i,5, QTableWidgetItem(str(rates["population"])))
                self.tabla.setItem(i,6, QTableWidgetItem(str(rates["suicides_per_100k"])))
                self.tabla.setItem(i,7, QTableWidgetItem(str(rates["gdp_per_capita"])))
                self.tabla.setItem(i,8, QTableWidgetItem(rates["generation"]))
            
        
        


        

            row = 0
            for endian in a:
                self.tabla.setRowCount(row + 1)
            
                idDato = QTableWidgetItem(endian[0])
                idDato.setTextAlignment(4)
            
                self.tabla.setItem(row, 0, idDato)
                self.tabla.setItem(row, 1, QTableWidgetItem(endian[1]))
                self.tabla.setItem(row, 2, QTableWidgetItem(endian[2]))
                self.tabla.setItem(row, 3, QTableWidgetItem(endian[3]))
                self.tabla.setItem(row, 4, QTableWidgetItem(endian[4]))
                self.tabla.setItem(row, 5, QTableWidgetItem(endian[5]))

                row += 1
        
        except Exception as e:
            pass
        
    def datosTabla(self):
        a = db.findAll().limit(50)

        for i, rates in enumerate (a):
            self.tabla.setItem(i,0, QTableWidgetItem(rates["country"]))
            self.tabla.setItem(i,1, QTableWidgetItem(str(rates["year"])))
            self.tabla.setItem(i,2, QTableWidgetItem(rates["sex"]))
            self.tabla.setItem(i,3, QTableWidgetItem(rates["age"]))
            self.tabla.setItem(i,4, QTableWidgetItem(str(rates["suicides_no"])))
            self.tabla.setItem(i,5, QTableWidgetItem(str(rates["population"])))
            self.tabla.setItem(i,6, QTableWidgetItem(str(rates["suicides_per_100k"])))
            self.tabla.setItem(i,7, QTableWidgetItem(str(rates["gdp_per_capita"])))
            self.tabla.setItem(i,8, QTableWidgetItem(rates["generation"]))

        row = 0
        for endian in a:
            self.tabla.setRowCount(row + 1)
            
            idDato = QTableWidgetItem(endian[0])
            idDato.setTextAlignment(4)
            
            self.tabla.setItem(row, 0, idDato)
            self.tabla.setItem(row, 1, QTableWidgetItem(endian[1]))
            self.tabla.setItem(row, 2, QTableWidgetItem(endian[2]))
            self.tabla.setItem(row, 3, QTableWidgetItem(endian[3]))
            self.tabla.setItem(row, 4, QTableWidgetItem(endian[4]))
            self.tabla.setItem(row, 5, QTableWidgetItem(endian[5]))

            row += 1

    def mostrarOcultar(self, accion):
        columna = accion.data()
        
        if accion.isChecked():
            self.tabla.setColumnHidden(columna, False)
        else:
            self.tabla.setColumnHidden(columna, True)


    def menuContextual(self, posicion):
        indices = self.tabla.selectedIndexes()

        if indices:
            menu = QMenu()

            itemsGrupo = QActionGroup(self)
            itemsGrupo.setExclusive(True)
            
            menu.addAction(QAction("Copiar todo", itemsGrupo))

            columnas = [self.tabla.horizontalHeaderItem(columna).text()
                        for columna in range(self.tabla.columnCount())
                        if not self.tabla.isColumnHidden(columna)]

            copiarIndividual = menu.addMenu("Copiar individual") 
            for indice, item in enumerate(columnas, start=0):
                accion = QAction(item, itemsGrupo)
                accion.setData(indice)
                
                copiarIndividual.addAction(accion)

            itemsGrupo.triggered.connect(self.copiarTableWidgetItem)
            
            menu.exec_(self.tabla.viewport().mapToGlobal(posicion))

    def Buscar (self):
        a = db.findAll().limit(50)
        i=0
        for i in a:
            self.tableWidget.setItem(i,0, QTableWidgetItem(rates["country"]))
            self.tableWidget.setItem(i,1, QTableWidgetItem(str(rates["year"])))
            self.tableWidget.setItem(i,2, QTableWidgetItem(rates["sex"]))
            self.tableWidget.setItem(i,3, QTableWidgetItem(rates["age"]))
            self.tableWidget.setItem(i,4, QTableWidgetItem(str(rates["suicides_no"])))
            self.tableWidget.setItem(i,5, QTableWidgetItem(str(rates["population"])))
            self.tableWidget.setItem(i,6, QTableWidgetItem(str(rates["suicides_per_100k"])))
            self.tableWidget.setItem(i,7, QTableWidgetItem(str(rates["gdp_per_capita"])))
            self.tableWidget.setItem(i,8, QTableWidgetItem(rates["generation"]))


if __name__ == "__main__":

    import sys

    aplicacion = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10)
    aplicacion.setFont(fuente)
    ventana = consultarWidget()
    ventana.show()

    sys.exit(aplicacion.exec_())