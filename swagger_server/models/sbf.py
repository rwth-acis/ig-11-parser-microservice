# coding: utf-8
# type: ignore
# pylint: disable-all
from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SBF(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, mgs: str = None, bot_name: str = None, channel: str = None, intent: str = None, entities: object = None, email: str = None, user: str = None, time: str = None):  # noqa: E501
        """SBF - a model defined in Swagger

        :param mgs: The mgs of this SBF.  # noqa: E501
        :type mgs: str
        :param bot_name: The bot_name of this SBF.  # noqa: E501
        :type bot_name: str
        :param channel: The channel of this SBF.  # noqa: E501
        :type channel: str
        :param intent: The intent of this SBF.  # noqa: E501
        :type intent: str
        :param entities: The entities of this SBF.  # noqa: E501
        :type entities: object
        :param email: The email of this SBF.  # noqa: E501
        :type email: str
        :param user: The user of this SBF.  # noqa: E501
        :type user: str
        :param time: The time of this SBF.  # noqa: E501
        :type time: str
        """
        self.swagger_types = {
            'mgs': str,
            'bot_name': str,
            'channel': str,
            'intent': str,
            'entities': object,
            'email': str,
            'user': str,
            'time': str
        }

        self.attribute_map = {
            'mgs': 'mgs',
            'bot_name': 'botName',
            'channel': 'channel',
            'intent': 'intent',
            'entities': 'entities',
            'email': 'email',
            'user': 'user',
            'time': 'time'
        }

        self._mgs = mgs
        self._bot_name = bot_name
        self._channel = channel
        self._intent = intent
        self._entities = entities
        self._email = email
        self._user = user
        self._time = time

    @classmethod
    def from_dict(cls, dikt) -> 'SBF':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SBF of this SBF.  # noqa: E501
        :rtype: SBF
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mgs(self) -> str:
        """Gets the mgs of this SBF.


        :return: The mgs of this SBF.
        :rtype: str
        """
        return self._mgs

    @mgs.setter
    def mgs(self, mgs: str):
        """Sets the mgs of this SBF.


        :param mgs: The mgs of this SBF.
        :type mgs: str
        """

        self._mgs = mgs

    @property
    def bot_name(self) -> str:
        """Gets the bot_name of this SBF.


        :return: The bot_name of this SBF.
        :rtype: str
        """
        return self._bot_name

    @bot_name.setter
    def bot_name(self, bot_name: str):
        """Sets the bot_name of this SBF.


        :param bot_name: The bot_name of this SBF.
        :type bot_name: str
        """
        if bot_name is None:
            raise ValueError("Invalid value for `bot_name`, must not be `None`")  # noqa: E501

        self._bot_name = bot_name

    @property
    def channel(self) -> str:
        """Gets the channel of this SBF.


        :return: The channel of this SBF.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel: str):
        """Sets the channel of this SBF.


        :param channel: The channel of this SBF.
        :type channel: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def intent(self) -> str:
        """Gets the intent of this SBF.


        :return: The intent of this SBF.
        :rtype: str
        """
        return self._intent

    @intent.setter
    def intent(self, intent: str):
        """Sets the intent of this SBF.


        :param intent: The intent of this SBF.
        :type intent: str
        """
        if intent is None:
            raise ValueError("Invalid value for `intent`, must not be `None`")  # noqa: E501

        self._intent = intent

    @property
    def entities(self) -> object:
        """Gets the entities of this SBF.


        :return: The entities of this SBF.
        :rtype: object
        """
        return self._entities

    @entities.setter
    def entities(self, entities: object):
        """Sets the entities of this SBF.


        :param entities: The entities of this SBF.
        :type entities: object
        """
        if entities is None:
            raise ValueError("Invalid value for `entities`, must not be `None`")  # noqa: E501

        self._entities = entities

    @property
    def email(self) -> str:
        """Gets the email of this SBF.


        :return: The email of this SBF.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this SBF.


        :param email: The email of this SBF.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def user(self) -> str:
        """Gets the user of this SBF.


        :return: The user of this SBF.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user: str):
        """Sets the user of this SBF.


        :param user: The user of this SBF.
        :type user: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def time(self) -> str:
        """Gets the time of this SBF.


        :return: The time of this SBF.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time: str):
        """Sets the time of this SBF.


        :param time: The time of this SBF.
        :type time: str
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time
