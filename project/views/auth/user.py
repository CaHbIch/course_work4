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

    def patch(self):
        """ Update user info """
        data = request.json
        token = request.headers["Authorization"].split("Bearer ")[-1]
        return user_service.update_user(data=data, refresh_token=token), 201


