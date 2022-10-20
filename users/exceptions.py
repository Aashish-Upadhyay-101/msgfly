from rest_framework.exceptions import APIException

class UserNotFoundException(APIException):
    status_code = 404 
    default_detail = "User with that email doesn't exist"


    