from PyQt5.QtWidgets import (
    QDialog, QGridLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt, QSize

from WIDGETS.IconBoton import IconBoton

class TOOLBOX(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        # flag es un señalador de que ah ocurrido algo o que se cumple algo 
        
        # en este caso el tipo de la ventana:
        self.setWindowFlags(Qt.Tool)
        
        self.setWindowTitle("Tools")
        self.setFixedSize(100, 400)
        LAYOUR = QVBoxLayout()
        
        boton_size = 32
        
        Boton_Pincel = IconBoton(icon_path=r"RESOURCES/ICONS/DARK/pincelD.svg", size=boton_size, contenedor=LAYOUR, Funcion=pincelprueba)
        Boton_Pluma  = IconBoton(icon_path=r"RESOURCES/ICONS/DARK/plumaD.svg" , size=boton_size, contenedor=LAYOUR, Funcion=plumaprueba)
        
        self.setLayout(LAYOUR)
        
        
        
def pincelprueba():
        print("pincel")
def plumaprueba():
        print("pluma")