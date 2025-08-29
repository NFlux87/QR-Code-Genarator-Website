import qrcode

def qrCodeGen(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        border=4
    )

    qr.add_data(url)
    qr.make(fit=True)  

    img = qr.make_image(fill_color="black", black_color="white")
    img.save("qrcode.png")

