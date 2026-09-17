import sys
from PyQt5.QtWidgets import (
    QOpenGLWidget,
    QApplication
)
from PyQt5.QtOpenGL import QGLFormat


import skia
from OpenGL import GL

class SKANVAS(QOpenGLWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.grContext = None
        self.superficie = None



    """
    Configura los recursos y el estado de OpenGl, llamado antes de la primera llamada
        a resizeGL o paintGL"""
    def initializeGL(self):
        print("initializeGL llamado con exito", flush=True)
        
        # PROBLEMA 1: esto por alguna razon sin importar si es windows o linux devuelve None lo que jode todo lo que sigue:
        self.makeCurrent()
        #  GrGLInterface.MakeEGL() deberia funcionar para KDE y tambien para Windows pero para alguna chingadera que use X11 necesitaria usar el otro asi que posteriormente investiga en la aplicacion grande si quieres hacer un if para verificar el sistema operativo mas a dondo
        interface = skia.GrGLInterface.MakeEGL() # esto deberia arreglar los problemas dehallar el contexto de GL
        self.grContext = skia.GrDirectContext.MakeGL(interface)

        print(f'self.grContext creado : {self.grContext}', flush=True)

    """
    Configura el VIEWPORT, la proyeccion etc
    se invoca cada que se redimenciona el widget
    cuando se muestra por primera vez
    """
    def resizeGL(self, w, h):

        self.makeCurrent()
        print('resizeGL llamado con exito', flush=True)
        print(f'resizeGL w: {w}, h: {h}', flush=True)

        
    # esto devuelve un integer equivalente a la variable del estado del sistema grafico
    # en este caso deveria dar el valor del frambebufferobject activo que se supone deberia usar esta aplicacion
    #  de normal deveria ser 0 pero en la practica quien sabe porque cada quien lleva sus propios procesos y yo que me quiero arrancar un huevo
        fbo_id = GL.glGetIntegerv(GL.GL_FRAMEBUFFER_BINDING)


        fb_info = skia.GrGLFramebufferInfo(fbo_id, GL.GL_RGBA8)

        ratio = self.devicePixelRatio()
    # esto genera el ancho y alto del frame buffer a partir del ratio de pixeles en que este echo el propio SKANVAS
        fb_ancho, fb_alto = int(w * ratio), int(h * ratio)



        backend_render_target = skia.GrBackendRenderTarget(
            fb_ancho,
            fb_alto,
            0, # numero de samples? no se que es un sample
            8, # numero de bits del stencil  como usamos GL_RGBA8 supongo que son 8 bits del stencil 
            fb_info
        )


        self.superficie = skia.Surface.MakeFromBackendRenderTarget(
            self.grContext,                     # un contexto de dibujado con la grafica especifico (en este caso el de OpenGL)
            backend_render_target,              # La localizacion del Framebuffer a utilizar para dibujar?
            skia.kBottomLeft_GrSurfaceOrigin,   # el encoder de como se leen los pixeles para dibujar supongo el 0,0 desde donde empieza? 
            skia.kRGBA_8888_ColorType,     # el espacio de color RGBA de 8 bits?
            skia.ColorSpace.MakeSRGB()
        )


        if not self.superficie:
            print(
            self.grContext,                     '\n',
            backend_render_target,              '\n',
            skia.kTopLeft_EncodedOrigin,        '\n',     
            skia.ColorSpace.MakeSRGB(),
            flush=True
        )


    """
    renderiza la escena OpenGL. LLamado siempre que el widget necesita actualizarse
    """

    def paintGL(self):
        self.makeCurrent()

        canvas = self.superficie.getCanvas()
        # "limpia" el canvas llenandolo de un color usando BlendMode.kSrc
        canvas.clear(skia.ColorWHITE)

        canvas.drawCircle(150, 150, 50, skia.Paint(Color=skia.ColorRED))
    
        # llamar para asegurar que todo el dibujo ah sido asociado al contexto y se haya enviado a la API:
        self.superficie.flushAndSubmit()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Asegurar el buffer stencil en Qt 
    fmt  = QGLFormat.defaultFormat()
    fmt.setStencil(True)
    QGLFormat.setDefaultFormat(fmt)

    widget = SKANVAS()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec_())