from flask import render_template,request

from flask import Flask, render_template, Response,  request, session, redirect, url_for, send_from_directory, flash

import os
import sys

from flask import Flask
from werkzeug.utils import secure_filename


from bar_qr_code_detector import *

app = Flask(__name__)


UPLOAD_FOLDER="static/Saved_Images"
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'JPG'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

@app.route("/")
def index():
  return render_template("index.html")




@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
 	  
      filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
      # print(filepath)
      f.save(filepath)

      barcode=barcode_no(filepath,filename)
      detected_name='det_'+filename





      return render_template("upload.html", display_detection = detected_name, fname = filename,barcode=barcode)      






if __name__ == '__main__':
   app.run()
