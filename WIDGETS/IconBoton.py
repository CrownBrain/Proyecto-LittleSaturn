from PyQt5.Qt import QSize
from PyQt5.QtWidgets import (
    QPushButton, QLayout
)
from PyQt5.QtGui import QIcon
from numpy import floor
from typing import Callable, Optional
class IconBoton(QPushButton):
    def __init__(self, icon_path: str = r"RESOURCES/ICONS/littleSaturn.svg", size: int = 32 ,contenedor = QLayout, Funcion =  Callable, tooltip: Optional[str] = None):
        super().__init__()
        
        self.setIcon(QIcon(icon_path))
        size_icon = int(floor(size * 0.9)) 
        self.setIconSize(QSize(size_icon, size_icon))
        self.setFixedSize(QSize(size, size))
        
        if tooltip:
            self.setToolTip(tooltip)
            
        contenedor.addWidget(self)
        self.clicked.connect(Funcion)
        