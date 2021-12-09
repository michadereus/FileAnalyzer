import os
import sys
import re
from werkzeug.utils import secure_filename, send_file

sys.path.append('../')
from database.gateway import gateway as Gateway
from util.accesss_control import validate_api_key
from util.response_builder import response_builder
from flask import Blueprint, request, flash, redirect, url_for, render_template
import json

UPLOAD_FOLDER = 'FileAnalyzer/fileUploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

home_bp = Blueprint('home_bp', __name__)

globalId = -1;

@home_bp.route('/home', methods=['GET'])
def homepage():
    gate = Gateway()
    # GET - return dict full of property data in order
    if request.method == 'GET':
        res, code = gate.test_gate()
        return response_builder(res, code)


@home_bp.route('/register', methods=['POST'])
def register():
    gate = Gateway()
    if request.method == 'POST':
        postDetails = request.form
        name = postDetails['name']
        passW = postDetails['pass']

        res, code = gate.register(name, passW)
        return response_builder(res, code)


@home_bp.route('/login', methods=['POST','GET'])
def login():
    gate = Gateway()
    if request.method == 'POST':
        postDetails = request.form
        name = postDetails['name']
        passW = postDetails['pass']

        gotID = gate.login(name,passW)
        if gotID > -1:

            global globalId
            globalId = gotID
            return redirect('uploader')
        else:
            return redirect('login')

    return render_template('index.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@home_bp.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    print(globalId)
    if globalId < 0:
        return redirect('login')
    gate = Gateway()
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect("upload.html")

        file = request.files['file']
        if file and allowed_file(file.filename):
            path = "FileUploads/" + str(globalId)
            pExist = os.path.exists(path)
            if not pExist:
                os.makedirs(path)
            filename = secure_filename(file.filename)
            file.save(path + "/" + filename)
            fileP = path + "/" + filename



            return render_template('upload.html')

    return render_template('upload.html')

@home_bp.route('/uploadedFiles', defaults={'req_path': ''}, methods=['GET', 'POST'])
@home_bp.route('/<path:req_path>')
def dir_listing(req_path):
    BASE_DIR = 'FileUploads/' + str(globalId)

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return "No files uploaded"

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = os.listdir(abs_path)
    return render_template('files.html', files=files)