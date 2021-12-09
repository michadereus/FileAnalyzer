import json
from flask import Blueprint, request, flash, redirect, url_for, render_template
from util.response_builder import response_builder
from util.accesss_control import validate_api_key
from database.gateway import gateway as Gateway
import os
import sys

from werkzeug.utils import secure_filename

sys.path.append('../')

UPLOAD_FOLDER = 'FileAnalyzer/fileUploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

file_bp = Blueprint('file_bp', __name__)
globalId = -1;

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@file_bp.route('/file/uploader', methods=['GET', 'POST'])
def upload_file():

   # if globalId < 0:
       # return redirect('login')
    gate = Gateway()
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            return redirect("upload.html")

        file = request.files['file']
        if file and allowed_file(file.filename):
            path = "FileUploads/files"
            pExist = os.path.exists(path)
            if not pExist:
                os.makedirs(path)
            filename = secure_filename(file.filename)
            file.save(path + "/" + filename)
            fileP = path + "/" + filename

            #return redirect('file/uploader/'+ str(userId))
            #TODO: REDIRECT TO ALL THE FILES IN THE LIST
            return redirect('uploader')
    return render_template('upload.html')

        
