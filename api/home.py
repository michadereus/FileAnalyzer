import os
import sys

from werkzeug.utils import secure_filename

sys.path.append('../')
from database.gateway import gateway as Gateway
from util.accesss_control import validate_api_key
from util.response_builder import response_builder
from flask import Blueprint, request, flash, redirect, url_for, render_template
import json

UPLOAD_FOLDER = 'FileAnalyzer/fileUploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

home_bp = Blueprint('home_bp', __name__)


# @home_bp.route('/register', methods=['POST'])
# def register():
#     gate = Gateway()
#     if request.method == 'POST':
#         postDetails = request.form
#         name = postDetails['name']
#         passW = postDetails['pass']

#         res, code = gate.register(name, passW)
#         return response_builder(res, code)



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
            return redirect('file/uploader')
        else:
            return redirect('login')

    return render_template('index.html')



