import json
from flask import Blueprint, request, flash, redirect, url_for
from util.response_builder import response_builder
from util.accesss_control import validate_api_key
from database.gateway import gateway as Gateway
import os
import sys

from werkzeug.utils import secure_filename

sys.path.append('../')

UPLOAD_FOLDER = 'FileAnalyzer/fileUploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

home_bp = Blueprint('file_bp', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@file_bp.route('/file/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect("upload.html")

        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save("FileUploads/" + filename)
            path = "FileUploads/" + filename
            return path
        return 'file uploaded successfully'
        
