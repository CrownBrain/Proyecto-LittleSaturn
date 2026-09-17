import sys
import skia
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *  # O PyQt5.QtWidgets
from PyQt5.QtOpenGL import QGLFormat
from PyQt5.QtWidgets import QOpenGLWidget
from OpenGL import GL

class SkiaWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.context_skia = None
        self.surface = None

    def initializeGL(self):
        # Qt configura automáticamente el contexto de OpenGL adecuado
        interface = skia.GrGLMakeNativeInterface()
        self.context_skia = skia.GrDirectContext.MakeGL(interface)

    def resizeGL(self, w, h):
        if not self.context_skia:
            return

        fbo_id = GL.glGetIntegerv(GL.GL_FRAMEBUFFER_BINDING)
        
        # Escala para pantallas HiDPI si aplica
        ratio = self.devicePixelRatio()
        fb_w, fb_h = int(w * ratio), int(h * ratio)

        backend_render_target = skia.GrBackendRenderTarget(
            fb_w,
            fb_h,
            0,  # samples
            8,  # stencil
            skia.GrGLFramebufferInfo(fbo_id, GL.GL_RGBA8)
        )

        self.surface = skia.Surface.MakeFromBackendRenderTarget(
            self.context_skia,
            backend_render_target,
            skia.kBottomLeft_GrSurfaceOrigin,
            skia.kRGBA_8888_ColorType,
            skia.ColorSpace.MakeSRGB()
        )

    def paintGL(self):
        if not self.surface:
            return

        with self.surface as canvas:
            canvas.clear(skia.ColorWHITE)
            canvas.drawCircle(150, 150, 60, skia.Paint(Color=skia.ColorRED))

        self.surface.flushAndSubmit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Asegurar buffer de Stencil en Qt
    fmt = QGLFormat.defaultFormat()
    fmt.setStencil(True)
    QGLFormat.setDefaultFormat(fmt)

    widget = SkiaWidget()
    widget.resize(640, 480)
    widget.show()
    sys.exit(app.exec_())