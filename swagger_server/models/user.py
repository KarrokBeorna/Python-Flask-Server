# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, username: str=None, full_name: str=None, email: str=None, password: str=None, phone: str=None):  # noqa: E501
        """User - a model defined in Swagger

        :param username: The username of this User.  # noqa: E501
        :type username: str
        :param full_name: The full_name of this User.  # noqa: E501
        :type full_name: str
        :param email: The email of this User.  # noqa: E501
        :type email: str
        :param password: The password of this User.  # noqa: E501
        :type password: str
        :param phone: The phone of this User.  # noqa: E501
        :type phone: str
        """
        self.swagger_types = {
            'username': str,
            'full_name': str,
            'email': str,
            'password': str,
            'phone': str
        }

        self.attribute_map = {
            'username': 'username',
            'full_name': 'fullName',
            'email': 'email',
            'password': 'password',
            'phone': 'phone'
        }

        self._username = username
        self._full_name = full_name
        self._email = email
        self._password = password
        self._phone = phone

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this User.


        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this User.


        :param username: The username of this User.
        :type username: str
        """

        self._username = username

    @property
    def full_name(self) -> str:
        """Gets the full_name of this User.


        :return: The full_name of this User.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name: str):
        """Sets the full_name of this User.


        :param full_name: The full_name of this User.
        :type full_name: str
        """

        self._full_name = full_name

    @property
    def email(self) -> str:
        """Gets the email of this User.


        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this User.


        :param email: The email of this User.
        :type email: str
        """

        self._email = email

    @property
    def password(self) -> str:
        """Gets the password of this User.


        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this User.


        :param password: The password of this User.
        :type password: str
        """

        self._password = password

    @property
    def phone(self) -> str:
        """Gets the phone of this User.


        :return: The phone of this User.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """Sets the phone of this User.


        :param phone: The phone of this User.
        :type phone: str
        """

        self._phone = phone
