from PyQt5.QtWidgets import (
    QDialog, QGridLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt, QSize

from WIDGETS.ICONBOTON import IconBoton

class ToolBox(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlag(Qt.Tool)
        self.setWindowTitle("Tools")
        self.setFixedSize(200, 400)
        
        self.gridBtns = QVBoxLayout()
        self.gridBtns.setSpacing(4)
        self.gridBtns.setAlignment(Qt.AlignmentFlag.AlignTop)


        self.botones = [
            #Seleccion
            IconBoton(IconPath= "RECURSOS/iconos/SeleccionarBitmap.svg", Funcion=self.SelectBitmap)
            #SeleccionNodos
            #pincel
            , IconBoton(IconPath="RECURSOS/iconos/pincel.svg", Funcion=self.Pincel)
            #borrador
            , IconBoton(IconPath="RECURSOS/iconos/borrador.svg", Funcion=self.borrador)
            #pluma
            #Cuentagotas
            #formas

        ]


        [self.gridBtns.addWidget(boton) for boton in self.botones]
    
        self.setLayout(self.gridBtns)


# por alguna razon los IconBoton estan retornando dos variables la primera no se que sea la segunda es un boolean que tampoco se que sea
    def Pincel(self, check = False):
        print("pincel")

    def borrador(self, check = False):
        
        print("borrador")

    def SelectBitmap(self, check = False):
        
        print("seleccion Bitmap")