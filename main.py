import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget)
from PyQt5.QtGui import QIcon
from CONFIG_SYS.wayland_desktop import Existe_desktop
from PyQt5.QtCore import Qt
from LAYOUTS.toolbox import TOOLBOX

from LAYOUTS.mainlayout import MAINLAYOUT
Autor = "GAMO"
Proyecto = "LittleSaturn"
version = "LittleSaturn 0.0"


class MAIN(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle(f"{Proyecto}{version} creacion de ventana")

        self.setWindowFlags(Qt.Window)
        self.setMinimumSize(800, 600)
        self.setObjectName("MAIN")
        
        self.ventana_herramientas = TOOLBOX(self)
        self.ventana_herramientas.show()


        # widget central
        contenedor_principal = QWidget()
        self.LAY = MAINLAYOUT()
        contenedor_principal.setLayout(self.LAY)
    
        self.setCentralWidget(contenedor_principal)
        
        
if __name__ == "__main__":

    # icono en windows rapidamente:
    if sys.platform == "win32":
        import ctypes
        AppId = f"{Autor}.{Proyecto}.{version}"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(AppId)

    app = QApplication(sys.argv)


    # configurar el programa de forma global:
    APP_ID = "LittleSaturn"
    app.setApplicationName(APP_ID)
    app.setOrganizationName(APP_ID)
    # extra linea para wayland
    app.setDesktopFileName(APP_ID)


    script_path = os.path.abspath(__file__)
    python_bin = sys.executable
    exec_command = f'"{python_bin}" "{script_path}"'

    # icono de forma normal en casi todo maldito wayland
    IconPathProject = os.path.join(os.path.dirname(script_path), "RESOURCES", "ICONS", "littleSaturn.svg")
    app.setWindowIcon(QIcon(IconPathProject))

    # configuracion para linux Wayland
    icon_path_wayland = os.path.join(os.path.dirname(script_path), "assets", "icono.png")
    Existe_desktop(
        app_id = APP_ID,
        app_name = version,
        exec_cmd = exec_command,
        icono_source_path = icon_path_wayland if os.path.exists(icon_path_wayland) else None,
        categoria ="Utility;Development;"

    )



    dir_main = os.path.dirname(script_path)
    with open(os.path.join(dir_main, "ESTILO.qss"), "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    aplicacion = MAIN()
    aplicacion.show()
    
    sys.exit(app.exec())
