from PyQt5.Qt import QSize
from PyQt5.QtWidgets import(
    QPushButton, QLayout
)
from PyQt5.QtGui import QIcon
from typing import Callable, Optional

class IconBoton(QPushButton):
    def __init__(self,
        IconPath: str = "RECURSOS/littleSaturn.svg",
        size: int = 32,
        contenedor: Optional[QLayout] = None,
        Funcion: Callable = lambda : print(f"No hay Funcion asignada en {self}"),
        ToolTip: Optional[str] = None, 
    ):
        super().__init__()


        self.setIcon(QIcon(IconPath))
        TamañoIcono = int(size * 0.9)
        self.setIconSize(QSize(TamañoIcono, TamañoIcono))
        self.setFixedSize(QSize(size, size))
        self.clicked.connect(Funcion)

        if ToolTip:
            self.setToolTip(ToolTip)

        if contenedor is not None:
            contenedor.addWidget(self)