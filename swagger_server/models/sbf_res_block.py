# coding: utf-8
# type: ignore
# pylint: disable-all
from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SBFResBlock(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, blocks: object = None, close_context: str = "true"):  # noqa: E501
        """SBFResBlock - a model defined in Swagger

        :param blocks: The blocks of this SBFResBlock.  # noqa: E501
        :type blocks: object
        :param close_context: The close_context of this SBFResBlock.  # noqa: E501
        :type close_context: str
        """
        self.swagger_types = {
            'blocks': object,
            'close_context': str
        }

        self.attribute_map = {
            'blocks': 'blocks',
            'close_context': 'closeContext'
        }

        self._blocks = blocks
        self._close_context = close_context

    @classmethod
    def from_dict(cls, dikt) -> 'SBFResBlock':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SBFResBlock of this SBFResBlock.  # noqa: E501
        :rtype: SBFResBlock
        """
        return util.deserialize_model(dikt, cls)

    @property
    def blocks(self) -> object:
        """Gets the blocks of this SBFResBlock.


        :return: The blocks of this SBFResBlock.
        :rtype: object
        """
        return self._blocks

    @blocks.setter
    def blocks(self, blocks: object):
        """Sets the blocks of this SBFResBlock.


        :param blocks: The blocks of this SBFResBlock.
        :type blocks: object
        """

        self._blocks = blocks

    @property
    def close_context(self) -> str:
        """Gets the close_context of this SBFResBlock.


        :return: The close_context of this SBFResBlock.
        :rtype: str
        """
        return self._close_context

    @close_context.setter
    def close_context(self, close_context: str):
        """Sets the close_context of this SBFResBlock.


        :param close_context: The close_context of this SBFResBlock.
        :type close_context: str
        """

        self._close_context = close_context
