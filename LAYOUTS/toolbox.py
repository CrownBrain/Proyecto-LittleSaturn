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
        
        self.gridbtn = QGridLayout()
        self.gridbtn.setSpacing(4)
        self.gridbtn.setAlignment(Qt.AlignTop)
            
        boton_size = 32
        
        self.botones =[
         # Pincel
          IconBoton(icon_path=r"RESOURCES/ICONS/DARK/pincelD.svg", size=boton_size, contenedor=self.gridbtn, Funcion=pincelprueba, grid_cols=2) 
        # Pluma
        , IconBoton(icon_path=r"RESOURCES/ICONS/DARK/plumaD.svg" , size=boton_size, contenedor=self.gridbtn, Funcion=plumaprueba, grid_cols=2) 
    ]
        self.setLayout(self.gridbtn)
        
def pincelprueba():
        print("pincel")
def plumaprueba():
        print("pluma")