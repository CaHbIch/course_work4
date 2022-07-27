from flask import request
from flask_restx import Namespace, Resource
from project.container import user_service, auth_service
from project.setup.api.models import user
from project.tools.security import decode_token, auth_required

api = Namespace('user')


@api.route("/")
class UserView(Resource):
    @auth_required
    @api.marshal_with(user, code=200, description='OK')
    def get(self):
        """
        Get user by id.
        """
        token = request.headers["Authorization"].split("Bearer ")[-1]
        uid = decode_token(token)["id"]
        return user_service.get_item(uid), 200

    @auth_required
    def patch(self):
        """Обновления профиля пользователя."""
        token = request.headers["Authorization"].split("Bearer ")[-1]
        uid = decode_token(token)["id"]
        data = request.get_json()
        user_service.update_part(data, uid)
        return "", 204


@api.route('/password/')
class AuthLogin(Resource):
    def post(self):
        """Авторизация пользователя"""
        req_json = request.json
        email = req_json.get('email')
        password = req_json.get('password')
        if None in [email, password]:
            return "Нужно email и пароль", 400
        tokens = auth_service.generate_tokens(email, password)
        if tokens != False:
            return tokens, 201
        else:
            return "Ошибка в запросе", 400

