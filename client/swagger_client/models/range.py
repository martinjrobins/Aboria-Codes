# coding: utf-8

"""
    Battery Data API

    A standard API for accessing battery experiment datasets and metadata  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: martin.robinson@cs.ox.ac.uk
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Range(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'label_name': 'str',
        'lower_bound': 'int',
        'upper_bound': 'int',
        'info': 'str'
    }

    attribute_map = {
        'id': 'id',
        'label_name': 'label_name',
        'lower_bound': 'lower_bound',
        'upper_bound': 'upper_bound',
        'info': 'info'
    }

    def __init__(self, id=None, label_name=None, lower_bound=None, upper_bound=None, info=None):  # noqa: E501
        """Range - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._label_name = None
        self._lower_bound = None
        self._upper_bound = None
        self._info = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.label_name = label_name
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        if info is not None:
            self.info = info

    @property
    def id(self):
        """Gets the id of this Range.  # noqa: E501


        :return: The id of this Range.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Range.


        :param id: The id of this Range.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def label_name(self):
        """Gets the label_name of this Range.  # noqa: E501


        :return: The label_name of this Range.  # noqa: E501
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        """Sets the label_name of this Range.


        :param label_name: The label_name of this Range.  # noqa: E501
        :type: str
        """
        if label_name is None:
            raise ValueError("Invalid value for `label_name`, must not be `None`")  # noqa: E501

        self._label_name = label_name

    @property
    def lower_bound(self):
        """Gets the lower_bound of this Range.  # noqa: E501


        :return: The lower_bound of this Range.  # noqa: E501
        :rtype: int
        """
        return self._lower_bound

    @lower_bound.setter
    def lower_bound(self, lower_bound):
        """Sets the lower_bound of this Range.


        :param lower_bound: The lower_bound of this Range.  # noqa: E501
        :type: int
        """
        if lower_bound is None:
            raise ValueError("Invalid value for `lower_bound`, must not be `None`")  # noqa: E501

        self._lower_bound = lower_bound

    @property
    def upper_bound(self):
        """Gets the upper_bound of this Range.  # noqa: E501


        :return: The upper_bound of this Range.  # noqa: E501
        :rtype: int
        """
        return self._upper_bound

    @upper_bound.setter
    def upper_bound(self, upper_bound):
        """Sets the upper_bound of this Range.


        :param upper_bound: The upper_bound of this Range.  # noqa: E501
        :type: int
        """
        if upper_bound is None:
            raise ValueError("Invalid value for `upper_bound`, must not be `None`")  # noqa: E501

        self._upper_bound = upper_bound

    @property
    def info(self):
        """Gets the info of this Range.  # noqa: E501


        :return: The info of this Range.  # noqa: E501
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this Range.


        :param info: The info of this Range.  # noqa: E501
        :type: str
        """

        self._info = info

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Range, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Range):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
