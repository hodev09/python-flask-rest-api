# src/shared/Authentication.py

import os
import jwt
import datetime
from flask import json, Response, request, g
from functools import wraps
from ..models.UserModel import UserModel


class Auth:
    """
    Auth class
    """

    @staticmethod
    def generate_token(user_id):
        """
        Generate Token Method
        """
        try:
            print(user_id)
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            print('generate_token_called..line 27')
            secret = os.getenv('JWT_SECRET_KEY')
            token = jwt.encode(
                payload,
                secret,
                'HS256'
            ).decode("utf-8")
            return token
        except Exception as e:
            return Response(
                mimetype="application/json",
                response=json.dumps({'error': 'error in getting user tokens'}, e),
                status=404
            )

    @staticmethod
    def decode_token(token):
        """
        Decode token method
        """
        re = {'data': {}, 'error': {}}
        try:
            secret = os.getenv('JWT_SECRET_KEY')
            payload = jwt.decode(token, secret)
            print(payload)
            re['data'] = {'user_id': payload['sub']}
            return re
        except jwt.ExpiredSignatureError as e1:
            re['error'] = {'message': 'token expired, please login again'}
            return re
        except jwt.InvalidTokenError:
            re['error'] = {'message': 'Invalid token, please try again with a new token'}
            return re

    # decorator
    @staticmethod
    def auth_required(func):
        """
        Auth decorator
        """

        @wraps(func)
        def decorated_auth(*args, **kwargs):
            if 'api-token' not in request.headers:
                return Response(
                    mimetype="application/json",
                    response=json.dumps({'error': 'Authentication token is not available, please login to get one'}),
                    status=400
                )
            token = request.headers.get('api-token')
            print(token)
            print('reached line 78 ')
            data = Auth.decode_token(token)
            print(data)
            if data['error']:
                return Response(
                    mimetype="application/json",
                    response=json.dumps(data['error']),
                    status=400
                )

            user_id = data['data']['user_id']
            check_user = UserModel.get_one_user(user_id)
            if not check_user:
                return Response(
                    mimetype="application/json",
                    response=json.dumps({'error': 'user does not exist, invalid token'}),
                    status=400
                )
            g.user = {'id': user_id}
            return func(*args, **kwargs)

        return decorated_auth
