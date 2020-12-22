#import libraries
import cv2
from pyzbar import pyzbar


def read_barcode(frame):
    barcodes = pyzbar.decode(frame)                                     #decode() function returns a list of namedtuple called Decoded which contains the fields data, type, rect, polygon
    for barcode in barcodes:
        x, y, w, h = barcode.rect                                       #gives the rectangle dimensions
        # 1
        barcode_info = barcode.data.decode('utf-8')                     #The decoded string is in bytes. You need to decode it using utf8 to get a string.
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)    #drawing a rectangle on the recognised bar/qr code


    return frame,  barcode_info , barcode


#2

frame=cv2.imread('qr1.png')                              #reading image
frame, barcode_info, barcode = read_barcode(frame)       #reading the barcode
if barcode.type=="QRCODE":                               #checking if we have qr or bar code
    print("Recognized QR Code:" + barcode_info)          #printing the recognised bar/qr code
else:
    print("Recognized Bar Code:" + barcode_info)
cv2.imshow('Barcode/QR code reader', frame)              #display image

cv2.waitKey(0)                                           #wait till enter is pressed
cv2.destroyAllWindows()                                  #close all windows opened