from PyQt5.QtWidgets import(
    QVBoxLayout
)

from LAYOUTS.cinta_opciones.cinta import CINTA

class MAINLAYOUT(QVBoxLayout): 
    def __init__(self):
        super().__init__()
        
        
        self.cinta = CINTA()
        
        self.addWidget(self.cinta)
        