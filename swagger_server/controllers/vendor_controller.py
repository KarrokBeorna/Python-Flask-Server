import connexion
import six

from swagger_server.models.add_shop import AddShop  # noqa: E501
from swagger_server import util
from swagger_server.logic import vendors


def add_product(id_market, product, price):  # noqa: E501
    """Add product

     # noqa: E501

    :param id_market:
    :type id_market: int64
    :param product: 
    :type product: str
    :param price: 
    :type price: int

    :rtype: None
    """
    res = vendors.add_product(id_market, product, price)
    if res == 0:
        return 'OK!', 200
    elif res == 1:
        return 'You don\'t have a store with this ID', 400
    elif res == 2:
        return 'You need to login', 404


def add_shop(body):  # noqa: E501
    """Add shop

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AddShop.from_dict(connexion.request.get_json())  # noqa: E501
    res = vendors.add_shop(body)
    if res:
        return 'OK!', 200
    else:
        return 'You need to login', 400


def get_shop_history():  # noqa: E501
    """Displaying shop history

     # noqa: E501


    :rtype: None
    """
    b, res = vendors.get_shop_history()
    if res:
        return res, 200
    else:
        return 'You need to login', 400
