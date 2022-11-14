import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

img_path = '../Py_Projects/qr_code/myqrcode.png'

data = 'Password for my wifi network'

def qr_encoder():
    qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color = 'red', back_color = 'white')
    img.save(img_path)

def qr_decoder():
    img = Image.open(img_path)
    result = decode(img)
    print(result)


if __name__ == '__main__':
    qr_decoder()