#import module

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
#add some data to show when scanned
qr.add_data('lutinwa.github.io/lennox.me')
qr.make(fit=True)

#make image
img = qr.make_image(fill_color="black", back_color="white")
filename = #anyname.type

#save image with extension .png
img.save(filename)