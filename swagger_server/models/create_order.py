# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CreateOrder(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, shop: int=None, goods: object=None, area: int=None):  # noqa: E501
        """CreateOrder - a model defined in Swagger

        :param shop: The shop of this CreateOrder.  # noqa: E501
        :type shop: int
        :param goods: The goods of this CreateOrder.  # noqa: E501
        :type goods: object
        :param area: The area of this CreateOrder.  # noqa: E501
        :type area: int
        """
        self.swagger_types = {
            'shop': int,
            'goods': object,
            'area': int
        }

        self.attribute_map = {
            'shop': 'shop',
            'goods': 'goods',
            'area': 'area'
        }

        self._shop = shop
        self._goods = goods
        self._area = area

    @classmethod
    def from_dict(cls, dikt) -> 'CreateOrder':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateOrder of this CreateOrder.  # noqa: E501
        :rtype: CreateOrder
        """
        return util.deserialize_model(dikt, cls)

    @property
    def shop(self) -> int:
        """Gets the shop of this CreateOrder.


        :return: The shop of this CreateOrder.
        :rtype: int
        """
        return self._shop

    @shop.setter
    def shop(self, shop: int):
        """Sets the shop of this CreateOrder.


        :param shop: The shop of this CreateOrder.
        :type shop: int
        """

        self._shop = shop

    @property
    def goods(self) -> object:
        """Gets the goods of this CreateOrder.


        :return: The goods of this CreateOrder.
        :rtype: object
        """
        return self._goods

    @goods.setter
    def goods(self, goods: object):
        """Sets the goods of this CreateOrder.


        :param goods: The goods of this CreateOrder.
        :type goods: object
        """

        self._goods = goods

    @property
    def area(self) -> int:
        """Gets the area of this CreateOrder.


        :return: The area of this CreateOrder.
        :rtype: int
        """
        return self._area

    @area.setter
    def area(self, area: int):
        """Sets the area of this CreateOrder.


        :param area: The area of this CreateOrder.
        :type area: int
        """

        self._area = area
