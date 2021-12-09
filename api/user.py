import sys
sys.path.append('../')
from database.gateway import gateway as Gateway
from util.accesss_control import validate_api_key
from util.response_builder import response_builder
from flask import Blueprint, request
import json

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user/register', methods=['POST'])
def register():
    gate = Gateway()
    if request.method == 'POST':
        postDetails = request.form
        name = postDetails['name']
        passW = postDetails['pass']

        res, code = gate.register(name, passW)
        return response_builder(res, code)


@user_bp.route('/user/login', methods=['GET'])
def login():
    gate = Gateway()
    if request.method == 'GET':
        postDetails = request.form
        name = postDetails['name']
        passW = postDetails['pass']

        res, code = gate.login(name, passW)
        return response_builder(res, code)

# GET returns all users in db
# @user_bp.route('/user', methods=['GET'])
# def get_users():
#     gate = gateway()
#     if request.method == 'GET':     
#         res,code = gate.get_users()
#         # the response_builder function expects the res to be in json form
#         return response_builder(res,code)

#GET returns specific user with user_id of user_id
# @user_bp.route('/user/<user_id>', methods=['GET'])
# def get_user(user_id):
#     gate = gateway()
#     if request.method == 'GET':     
#         res,code = gate.get_user(user_id)
#         # the response_builder function expects the res to be in json form
#         return response_builder(res,code)