import sys
sys.path.append('../')
from database.gateway import gateway as Gateway
from util.accesss_control import validate_api_key
from util.response_builder import response_builder
from flask import Blueprint, request
import json

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/home', methods=['GET'])
def homepage():
    gate = Gateway()
    # GET - return dict full of property data in order
    if request.method == 'GET':
        res,code = gate.get_file()
        return response_builder(res,code)

