import connexion
import six

from swagger_server.models.create_order import CreateOrder  # noqa: E501
from swagger_server import util
from swagger_server.logic import users


def create_order(body):  # noqa: E501
    """Create order

     # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = CreateOrder.from_dict(connexion.request.get_json())  # noqa: E501
    b = users.create_order(body)
    if b == 0:
        return 'The order has been created', 200
    elif b == 1:
        return 'You need to login', 400
    elif b == 2:
        return 'The ordered product is not available in this store', 404


def get_order_history():  # noqa: E501
    """Displaying order history

     # noqa: E501


    :rtype: List[OrderHistory]
    """
    b, res = users.get_order_history()
    if b:
        return res, 200
    else:
        return 'You need to login', 400


def get_shops():  # noqa: E501
    """Get shops

     # noqa: E501


    :rtype: None
    """
    b, res = users.get_shops()
    if b:
        return res, 200
    else:
        return 'You need to login', 400
