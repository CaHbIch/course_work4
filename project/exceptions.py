class BaseServiceError(Exception):
    code = 500


class ItemNotFound(BaseServiceError):
    code = 404


class InvalidPasswordUsage(BaseServiceError):
    status_code = 500


class ItemAlreadyExists(Exception):
    status_code = 400
