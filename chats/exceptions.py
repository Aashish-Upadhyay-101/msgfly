from rest_framework.exceptions import APIException


class LoginRequiredException(APIException):
    status_code = 401 
    default_detail = "Please login to access this feature"