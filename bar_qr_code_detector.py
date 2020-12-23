#import libraries
import numpy as np
import cv2
from pyzbar.pyzbar import decode

def read_barcode(frame):
    barcodes = decode(frame)                                     #decode() function returns a list of namedtuple called Decoded which contains the fields data, type, rect, polygon
    for barcode in barcodes:
        x, y, w, h = barcode.rect                                       #gives the rectangle dimensions
        # 1
        barcode_info =barcode.data.decode('utf-8')                     #The decoded string is in bytes. You need to decode it using utf8 to get a string.
        cv2.rectangle(frame, (x, y), (x ,y-7), (0, 255, 0), 2)    #drawing a rectangle on the recognised bar/qr code


    return frame,  barcode_info , barcode

def get_optimal_font_scale(text, width):
    for scale in reversed(range(0, 60, 1)):
        textSize = cv2.getTextSize(text, fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=scale/10, thickness=1)
        new_width = textSize[0][0]
        if (new_width <= width):
            return scale/9
    return 1

#2

def barcode_no(filepath):

    frame=cv2.imread(filepath)                             #reading image
    frame, barcode_info, barcode = read_barcode(frame)       #reading the barcode
    if barcode.type=="QRCODE":                               #checking if we have qr or bar code
        print("Recognized QR Code:" + barcode_info)          #printing the recognised bar/qr code
    else:
        print("Recognized Bar Code:" + barcode_info)

    # write the text on the image
        
    fontThickness = 1                                        # setting thickness of the font
    font_color = (0,255,0)                                   # setting the font color
    font = cv2.FONT_HERSHEY_SIMPLEX                          # setting the font 
    imageWidth,imageHeight = frame.shape[0],frame.shape[1]   # getting the size of image
    text = barcode_info
    scale = get_optimal_font_scale(text,imageWidth)          # this value can be from 0 to 1 (0,1] to change the size of the text relative to the image
    fontScale = min(imageWidth,imageHeight)/(25/scale)       # defining font scale


    cv2.putText(frame, text, (5,13) , font, scale, font_color,fontThickness)
    cv2.imwrite('static/Saved_Images/down.jpg',frame)

    return text

# cv2.imshow('Barcode/QR code reader', frame)              #display image

# cv2.waitKey(0)                                           #wait till enter is pressed
# cv2.destroyAllWindows()                                  #close all windows opened
