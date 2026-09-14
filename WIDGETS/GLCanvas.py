from PyQt5.QtWidgets import QOpenGLWidget
import skia
from OpenGL import GL

class Canvas(QOpenGLWidget):
    print("funciono")
    def initializeGL(self):
        interface = skia.GrGLInterface.MakeNative()
        self.gr_context = skia.GrDirectContext.MakeGL(interface)

    def resizeGL(self, w, h):
        fb_info = skia.GrGLFramebufferInfo(0, GL.GL_RGBA8)
        backend_rt = skia.GrBackendRenderTarget(w, h, 0, 0, fb_info)
        self.surface = skia.Surface.MakeFromBackendRenderTarget(
            self.gr_context, backend_rt, skia.kBottomLeft_GrSurfaceOrigin,
            skia.kRGBA_8888_ColorType, None
        )

    def paintGL(self):
        canvas = self.surface.getCanvas()
        canvas.clear(skia.ColorWHITE)
        self.gr_context.flush()