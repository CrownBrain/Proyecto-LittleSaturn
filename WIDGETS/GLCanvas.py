from PyQt5.QtWidgets import (QOpenGLWidget, QSizePolicy)
import skia
from OpenGL import GL
import traceback

class Canvas(QOpenGLWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setMinimumSize(400, 400)
        
        self.surface = None # inicializamos aqui 

    def initializeGL(self):
        print("initializeGL llamado")
        self.gr_context = skia.GrDirectContext.MakeGL()


    def resizeGL(self, w, h):
        print(f"resizeGL llamado con w={w}, h={h}")
        try:
            if w <= 0 or h <= 0:
                print("tamaño inválido, saltando creación de surface")
                return
            
            
            fb_info = skia.GrGLFramebufferInfo(0, GL.GL_RGBA8)
            backend_rt = skia.GrBackendRenderTarget(w, h, 0, 0, fb_info)
            

            self.surface = skia.Surface.MakeFromBackendRenderTarget(
                self.gr_context, backend_rt, skia.kBottomLeft_GrSurfaceOrigin,
                skia.kRGBA_8888_ColorType, 
                skia.ColorSpace.MakeSRGB() 
            )

            print([self.gr_context, backend_rt, skia.kBottomLeft_GrSurfaceOrigin,
                skia.kRGBA_8888_ColorType, 
                skia.ColorSpace.MakeSRGB() 
            ])


            print(f"surface creada: {self.surface}")
        except Exception:
            print("ERROR dentro de resizeGL:")
            traceback.print_exc()

    def paintGL(self):
        print("paintGL llamado")
        if not hasattr(self, "surface") or self.surface is None:
            print("surface no existe todavía, saltando frame")
            return
        
        canvas = self.surface.getCanvas()
        canvas.clear(skia.ColorWHITE)
        self.gr_context.flush()