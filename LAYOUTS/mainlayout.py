from PyQt5.QtWidgets import(
    QVBoxLayout
)

from LAYOUTS.cinta_opciones.cinta import CINTA
from WIDGETS.GLCanvas import Canvas

class MAINLAYOUT(QVBoxLayout): 
    def __init__(self):
        super().__init__()
        
        
        self.cinta = CINTA()
        self.canva = Canvas()
        self.addWidget(self.cinta)
        self.addWidget(self.canva)
        