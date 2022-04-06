import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util
from swagger_server.logic import accounts


def create_user(body):  # noqa: E501
    """Create user

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    res = accounts.create_user(body)
    if res:
        return 'OK!', 200
    else:
        return 'Username (phone) already in use', 404


def forced_logout_user(username):  # noqa: E501
    """Logout user by username

     # noqa: E501

    :param username:
    :type username: str

    :rtype: None
    """
    res = accounts.forced_user_logout(username)
    if res:
        return 'OK!', 200
    else:
        return 'You must be logged in with an administrator account', 400


def login_user(username, password):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username:
    :type username: str
    :param password:
    :type password: str

    :rtype: str
    """
    res = accounts.user_login(username, password)
    if res:
        return 'OK!', 200
    else:
        return 'Invalid username/password', 404


def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    res = accounts.user_logout()
    if res:
        return 'OK!', 200
    else:
        return 'You need to login', 404
