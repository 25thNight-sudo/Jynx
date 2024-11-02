import qrcode

def generate_qr_code(qrlink):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qrlink)
    qr.make(fit=True)

    # Save the QR code image with a name derived from the link
    filename = qrlink[12:18] + ".png"
    qrpng = qr.make_image(fill_color="red", back_color="white")
    qrpng.save(filename)
    
    return filename  # Return the filename of the saved QR code
