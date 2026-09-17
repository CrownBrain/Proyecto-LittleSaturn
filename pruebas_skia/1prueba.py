import skia 

superficie = skia.Surface(200, 200)

with superficie as canvas:
    rect = skia.Rect(32, 32, 96, 96)
    paint = skia.Paint(
        Color = skia.ColorYELLOW, 
        StrokeWidth = 5, 
        Style = skia.Paint.kFill_Style)

    canvas.drawRect(rect, paint)


image = superficie.makeImageSnapshot()
image.save("Render_Out.png", skia.kPNG)

