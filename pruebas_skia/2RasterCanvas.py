import skia 
import matplotlib.pyplot as plt 
import numpy as np 

ancho, alto  = 800, 600
array = np.zeros((ancho, alto, 4), dtype = np.uint8)

with skia.Surface(array) as canvas:
    canvas.drawCircle(100, 100, 50, skia.Paint(Color = skia.ColorBLUE))


plt.imshow(array)
plt.show()
