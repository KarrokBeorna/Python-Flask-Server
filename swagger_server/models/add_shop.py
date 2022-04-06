# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AddShop(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, goods: object=None, area: int=None):  # noqa: E501
        """AddShop - a model defined in Swagger

        :param name: The name of this AddShop.  # noqa: E501
        :type name: str
        :param goods: The goods of this AddShop.  # noqa: E501
        :type goods: object
        :param area: The area of this AddShop.  # noqa: E501
        :type area: int
        """
        self.swagger_types = {
            'name': str,
            'goods': object,
            'area': int
        }

        self.attribute_map = {
            'name': 'name',
            'goods': 'goods',
            'area': 'area'
        }

        self._name = name
        self._goods = goods
        self._area = area

    @classmethod
    def from_dict(cls, dikt) -> 'AddShop':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AddShop of this AddShop.  # noqa: E501
        :rtype: AddShop
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this AddShop.


        :return: The name of this AddShop.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this AddShop.


        :param name: The name of this AddShop.
        :type name: str
        """

        self._name = name

    @property
    def goods(self) -> object:
        """Gets the goods of this AddShop.


        :return: The goods of this AddShop.
        :rtype: object
        """
        return self._goods

    @goods.setter
    def goods(self, goods: object):
        """Sets the goods of this AddShop.


        :param goods: The goods of this AddShop.
        :type goods: object
        """

        self._goods = goods

    @property
    def area(self) -> int:
        """Gets the area of this AddShop.


        :return: The area of this AddShop.
        :rtype: int
        """
        return self._area

    @area.setter
    def area(self, area: int):
        """Sets the area of this AddShop.


        :param area: The area of this AddShop.
        :type area: int
        """

        self._area = area