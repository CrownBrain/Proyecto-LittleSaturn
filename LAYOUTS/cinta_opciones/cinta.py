from LAYOUTS.cinta_opciones.inicio import TabInicio
from PyQt5.QtWidgets import (
    QWidget, QTabWidget, QHBoxLayout
)

from PyQt5.QtCore import Qt

class CINTA(QWidget):
    def __init__(self):
        super().__init__()
        
        self.tabs = QTabWidget()        
        TAB_inicio = TabInicio()
        
        self.tabs.addTab(TAB_inicio, "Inicio")
        
        LAYOURT = QHBoxLayout()
        LAYOURT.setAlignment(Qt.AlignLeft)
        LAYOURT.addWidget(self.tabs)
        
        self.setLayout(LAYOURT)