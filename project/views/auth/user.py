from flask import request
from flask_restx import Namespace, Resource
from project.container import user_service
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

    def patch(self):
        """ Update user info """
        token = request.headers["Authorization"].split("Bearer ")[-1]
        access_token = decode_token(token)["id"]
        data = request.get_json()
        user_service.update_user(data, access_token)
        return "", 204


@api.route("/password/")
class UserView(Resource):

    def put(self):
        token = request.headers["Authorization"].split("Bearer ")[-1]
        access_token = decode_token(token)["id"]
        data = request.json
        user_service.update(data, access_token)
        return "", 204