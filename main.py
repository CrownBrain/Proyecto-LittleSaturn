import sys
import argparse
from Canvas import SKANVAS
from SUBWINDOWS.toolbox import ToolBox

from PyQt5.QtWidgets import (
    QApplication, QMainWindow
)
from pathlib import Path


Autor = "GAMO"
Proyecto = "LittleSaturn"
version = "0.0"
PredStyle = "Dark"

dirMain = Path(__file__).resolve().parent
dirStyles = dirMain / "Style"


# detectar el sistema operativo:
SYSoper = sys.platform




class MAIN(QMainWindow):
    def __init__(self, estilo = PredStyle):
        super().__init__()

        self.setWindowTitle(f"{Proyecto}{version} Canvas importado")
        self.setMinimumSize(300, 300)
        self.resize(800, 600)
        self.setObjectName("MAIN")

        # por si las dudas no cargues nada antes de cargar el canvas
        CANVAS = SKANVAS()
        self.setCentralWidget(CANVAS)


        
        self.ToolBoxWindow = ToolBox(self)
        self.ToolBoxWindow.show()

        
        
        

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=f"{Proyecto} App")
    parser.add_argument(
        "--estilo", "-e",
        default=PredStyle,
        help=f"Especifciar el estilo de la aplicacion (dark, Light, ...), Default = {PredStyle}"
    )
    
    args = parser.parse_args()
    estilo = args.estilo

    AppID = f"{Autor}.{Proyecto}.{version}"

    if SYSoper == "win32":
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(AppID)

     
    app = QApplication(sys.argv)

    StyleSheet = dirStyles / f"{estilo}.qss"
    
    if StyleSheet.is_file():
        with open(StyleSheet) as hoja:
            app.setStyleSheet(hoja.read())
    else:
        raise print(f"StyleSheet : {StyleSheet} no encontrada")


    aplicacion = MAIN()
    aplicacion.show()
    sys.exit(app.exec_())