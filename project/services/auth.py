import calendar
import datetime
import jwt
from flask_restx import abort

from project.services.user import UsersService
from project.tools.constants import SECRET_KEY, ALGORITM
from project.tools.security import compare_passwords


class AuthService:
    def __init__(self, user_service: UsersService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_user_by_email(email)

        if user is None:
            abort(401, "Нет такого  Email")

        if not is_refresh:
            if not compare_passwords(user.password, password):
                abort(401, "Нет такого пароля")

        data = {"id": user.id, "email": user.email}

        # access token on 30 min
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITM)

        # refresh, 130 days

        day130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(day130.timetuple())
        refresh_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITM)

        return {"access_token": access_token, "refresh_token": refresh_token}

    def approve_refresf_token(self, refresh_token):
        data = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITM])
        email = data['email']
        user = self.user_service.get_user_by_email(email)

        if not user:
            return False
        now = calendar.timegm(datetime.datetime.utcnow().timetuple())
        expired = data['exp']
        if now > expired:
            return False
        return self.generate_tokens(email, user.password, is_refresh=True)