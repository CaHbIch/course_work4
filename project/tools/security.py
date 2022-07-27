import base64
import hashlib
import hmac
from typing import Union

import jwt
from flask import current_app, abort, request


def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


def compare_passwords(hash_user: Union[str, bytes], input_password: str):
    """ Проверка пароля из request, пароля в БД """
    return hmac.compare_digest(
        base64.b64decode(hash_user),
        hashlib.pbkdf2_hmac(
            'sha256',
            input_password.encode('utf-8'),
            salt=current_app.config["PWD_HASH_SALT"],
            iterations=current_app.config["PWD_HASH_ITERATIONS"],
        )
    )


def decode_token(token: str):
    decoded_token = {}
    try:
        decoded_token = jwt.decode(
            jwt=token,
            key=current_app.config["SECRET_KEY"],
            algorithms=current_app.config["ALGORITM"]
            )
    except Exception:
        abort(401)
    return decoded_token


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=current_app.config["ALGORITM"])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper
