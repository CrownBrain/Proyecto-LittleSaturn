from PyQt5.Qt import QSize
from PyQt5.QtWidgets import (
    QPushButton, QLayout, QGridLayout
)
from PyQt5.QtGui import QIcon
from numpy import floor
from typing import Callable, Optional
class IconBoton(QPushButton):
    def __init__(self, icon_path:
        str = r"RESOURCES/ICONS/littleSaturn.svg",
        size: int = 32 ,
        contenedor = QLayout,
        Funcion =  Callable, 
        tooltip: Optional[str] = None, 
        grid_cols: Optional[int] = None
    ):
        super().__init__()
        
        self.setIcon(QIcon(icon_path))
        size_icon = int(floor(size * 0.9)) 
        self.setIconSize(QSize(size_icon, size_icon))
        self.setFixedSize(QSize(size, size))
        self.clicked.connect(Funcion)
        
        
        if tooltip:
            self.setToolTip(tooltip)
            
        if contenedor is not None:
            self._agregar_a_conenedor(contenedor, gridcols= grid_cols)
            
            
    def _agregar_a_conenedor(self, Container:QLayout, gridcols:Optional[int]):
        if isinstance(Container, QGridLayout) and gridcols:
            TotalItems = Container.count()
            fila = TotalItems // gridcols
            col = TotalItems % gridcols
            Container.addWidget(self, fila, col)
        else:
            Container.addWidget(self)