import sys
sys.path.append('../')
from database.gateway import gateway as Gateway
from util.accesss_control import validate_api_key
from util.response_builder import response_builder
from flask import Blueprint, request
import json

user_bp = Blueprint('user_bp', __name__)



@user_bp.route('/user/<user_id>', methods=['GET'])
def login(user_id):
    # creating gateway instance
    gate = gateway()
    # request: defined when 
    if request.method == 'GET':     
        res,code = gate.get_user(user_id, password)
        # the response_builder function expects the res to be in json form
        return response_builder(res,code)

