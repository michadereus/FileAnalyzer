import os
import sys

from werkzeug.utils import secure_filename

sys.path.append('../')
from database.gateway import gateway as Gateway
from util.accesss_control import validate_api_key
from util.response_builder import response_builder
from flask import Blueprint, request, flash, redirect, url_for
import json

UPLOAD_FOLDER = 'FileAnalyzer/fileUploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

home_bp = Blueprint('home_bp', __name__)


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


@home_bp.route('/login', methods=['POST'])
def login():
    gate = Gateway()
    if request.method == 'POST':
        postDetails = request.form
        name = postDetails['name']
        passW = postDetails['pass']

        res, code = gate.login(name, passW)
        return response_builder(res, code)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@home_bp.route('/uploader', methods=['GET', 'POST'])
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
