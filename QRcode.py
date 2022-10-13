import qrcode
import image

qr = qrcode.QRCode(
    version = 14,
    box_size=10,
    border=2
)

data = "https://github.com/Rikiriat19"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill= "black", back_color = "white" )
img.save("d.png")