
import abc
import logging
import six


logger = logging.getLogger(__name__)



@six.add_metaclass(abc.ABCMeta)
class Handler(object):
    """
    JSON Handler

    This is an abstract class. It defines the required interface
    for a JSON handler. All subclasses must implement any abstract
    methods and/or properties.
    """

    def __init__(self, name=None):
        """
        Initialize handler.

        Args:
            name (str, optional): Handler name.
        """
        self._name = name
        self._active = True

    @property
    def name(self):
        """
        Get/set handler name.

        str: Handler name.
        """
        if not self._name:
            cls_name = self.__class__.__name__
            self._name = cls_name.replace("Handler", "").lower()

        return self._name

    @name.setter
    def name(self, name):
        self._name = str(name)

    @property
    def active(self):
        """
        Get/set active state.

        bool: True if active, fales otherwise.
        """
        return self._active

    @active.setter
    def active(self, active):
        self._active = bool(active)

    @abc.abstractmethod
    def match(self, obj):
        """
        Match the given object.

        This method is used to determine whether this
        handler is used for the given object.

        Args:
            obj: Object to be encoded

        Returns:
            bool: True if this is a matching handler, false otherwise.
        """
        pass

    @abc.abstractmethod
    def encode(self, obj):
        """
        Encode the given object.

        Args:
            obj: Object to be encoded

        Returns:
            object: Encoded data object.
        """
        pass

    @abc.abstractmethod
    def decode(self, obj):
        """
        Decode the given object.

        Args:
            obj: Object to be decoded

        Returns:
            object: Decoded data object.
        """
        pass
