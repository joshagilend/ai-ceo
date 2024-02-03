import qrcode

# Generate a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Clementine')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img_path = "/mnt/data/clementine_qr.png"
img.save(img_path)

img_path
