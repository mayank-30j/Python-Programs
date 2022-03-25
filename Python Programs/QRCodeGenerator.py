import qrcode as qr

data = "I want to start a business and I will be a millionaire"

# img = qr.make(data)
# img.save("C:/Users/mayan/OneDrive/Desktop/Mayank's folder/myqrcode.png")

QR = qr.QRCode(version=1, border=3, box_size=10)

QR.add_data(data)
QR.make(fit=True)
img = QR.make_image(fill_color='Blue', back_color='White')
img.save('QRcode2.png')  # You need to give full path to save the image generated
