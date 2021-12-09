import sys
sys.path.append('../')
from database.gateway import gateway as Gateway, gateway
from util.accesss_control import validate_api_key
from util.response_builder import response_builder
from flask import Blueprint, request
import json

user_bp = Blueprint('user_bp', __name__)


# GET returns all users in db
@user_bp.route('api/user/', methods=['GET'])
def get_users():
    gate = gateway()
    if request.method == 'GET':     
        res,code = gate.get_users()
        # the response_builder function expects the res to be in json form
        return response_builder(res,code)

#GET returns specific user with user_id of user_id
@user_bp.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    gate = gateway()
    if request.method == 'GET':     
        res,code = gate.get_user(user_id)
        # the response_builder function expects the res to be in json form
        return response_builder(res,code)