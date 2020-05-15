from flask import request, json, Response, Blueprint, g
from ..models.UserModel import UserModel, UserModelSchema
from ..shared.Authentication import Auth
from ..shared.ApiResponse import ApiResponse

user_api = Blueprint('users', __name__)
user_schema = UserModelSchema()


@user_api.route('/', methods=['POST'])
def create():
    """
    create user function
    """
    try:
        req_data = request.get_json()
        print(req_data)
        data = user_schema.load(req_data)

        # check if user already exists in db
        user_in_db = UserModel.get_user_by_email(data.get('email'))
        if user_in_db:
            message = {'error': 'User already exist, please supply another email address'}
            return ApiResponse.custom_response(message, 400)

        user = UserModel(data)
        user.save()

        print('line 28/ uv.py')
        ser_data = user_schema.dump(user)
        print(ser_data)

        token = Auth.generate_token(ser_data.get('id'))
        print(token)
        return ApiResponse.custom_response({'jwt_token': token}, 201)
    except Exception as e:
        print(e)
        return ApiResponse.custom_response('Some error happended'+e.__doc__, 500)


@user_api.route('/login', methods=['POST'])
def login():
    req_data = request.get_json()

    data = user_schema.load(req_data, partial=True)
    print(data)

    # if error:
    # return custom_response(error, 400)

    if not data.get('email') or not data.get('password'):
        return ApiResponse.custom_response({'error': 'email & password needed to sign in '}, 400)

    user = UserModel.get_user_by_email(data.get('email'))

    if not user:
        return ApiResponse.custom_response({'error': 'invalid credentials'}, 400)

    if not user.check_hash(data.get('password')):
        return ApiResponse.custom_response({'error': 'invalid credentials'}, 400)

    ser_data = user_schema.dump(user)

    token = Auth.generate_token(ser_data.get('id'))

    return ApiResponse.custom_response({'jwt_token': token}, 200)


@user_api.route('/', methods=['GET'])
@Auth.auth_required
def get_all():
    users = UserModel.get_all_users()
    ser_users = user_schema.dump(users, many=True).data
    return ApiResponse.custom_response(ser_users, 200)


@user_api.route('/<int:user_id>', methods=['GET'])
@Auth.auth_required
def get_a_user(user_id):
    """
    Get a single user
    """
    user = UserModel.get_one_user(user_id)
    if not user:
        return ApiResponse.custom_response({'error': 'user not found'}, 404)

    ser_user = user_schema.dump(user)
    return ApiResponse.custom_response(ser_user, 200)


@user_api.route('/me', methods=['PUT'])
@Auth.auth_required
def update():
    """
    Update user
    """
    req_data = request.get_json()
    data, error = user_schema.load(req_data, partial=True)
    if error:
        return ApiResponse.custom_response(error, 400)

    user = UserModel.get_one_user(g.user.get('id'))
    user.update(data)
    ser_user = user_schema.dump(user)
    return ApiResponse.custom_response(ser_user, 200)


@user_api.route('/me', methods=['DELETE'])
@Auth.auth_required
def delete():
    """
    Delete user
    """
    user = UserModel.get_one_user(g.user.get('id'))
    user.delete()
    return ApiResponse.custom_response({'message': 'deleted'}, 204)


@user_api.route('/me', methods=['GET'])
@Auth.auth_required
def get_me():
    print('reached here')
    """
    Get me
    """
    user = UserModel.get_one_user(g.user.get('id'))
    ser_user = user_schema.dump(user)
    return ApiResponse.custom_response(ser_user, 200)
