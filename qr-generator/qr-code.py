import qrcode

img = qrcode.make("Hello World! This is Adriana!")
img.save("mycode.png")