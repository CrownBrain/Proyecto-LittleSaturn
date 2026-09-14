import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MAINWINDOW(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("LittleSaturn 0.0 creacion de ventana")
        
        self.setMinimumSize(800, 600)
        self.setObjectName("MAIN")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    app.setWindowIcon(QIcon("RESOURCES/ICONS/littleSaturn.svg"))
    
    aplicacion = MAINWINDOW()
    aplicacion.show()
    
    sys.exit(app.exec())