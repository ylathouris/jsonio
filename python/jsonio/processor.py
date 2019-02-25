
import collections
import logging

try:
    import dataclasses
except ImportError:
    dataclasses = None

from .handlers import DateTimeHandler


logger = logging.getLogger(__name__)


class BaseProcessor(object):
    """
    Base Processor

    The base processor object provides the common functionality for
    the encoder and decoder objects. For example;

        * Dataclasses: A toggle for supporting dataclasses (py37+)
        * Custom Handlers: Methods for adding/removing custom handlers
    """

    def __init__(self):
        """Initialize encoder"""
        self._dataclasses = False
        self._handlers = collections.OrderedDict()

    @property
    def dataclasses(self):
        """
        Get dataclasses state.

        This property is used to indicate whether or not dataclasses
        should be encoded/decoded.

        bool: Dataclasses state
        """
        return self._dataclasses

    @dataclasses.setter
    def dataclasses(self, value):
        self._dataclasses = bool(value)

    @property
    def handlers(self):
        """
        Get handlers

        collections.OrderedDict: Handlers
        """
        if not self._handlers:
            msg = 'Initializing date/time handler'
            logger.debug(msg)
            self._handlers['datetime'] = DateTimeHandler()

        return self._handlers


class Encoder(BaseProcessor):
    """
    Encoder

    The encoder class is used to encode JSON data. It provides
    built-in support for encoding dataclasses. It also provides
    support for adding custom handlers to encode various other
    object types.
    """

    def encode(self, obj):
        """
        Encode JSON object.

        Args:
            obj (object): Object to encode.

        Returns:
             str: JSON encoded object.
        """
        for handler in self.handlers.values():
            if handler.active:
                if handler.match(obj):
                    return {
                        "$jsonio-key": handler.name,
                        "$jsonio-value": handler.encode(obj),
                    }

        return obj

    def __call__(self, obj):
        return self.encode(obj)


class Decoder(BaseProcessor):
    """
    Decoder

    The decoder class is used to decode JSON data. It provides
    built-in support for decoding dataclasses. It also provides
    support for adding custom handlers to decode various other
    object types.
    """

    def __init__(self, *args, **kwargs):
        """Initialize decoder"""
        super(Decoder, self).__init__(*args, **kwargs)
        self._ordered = False

    @property
    def ordered(self):
        """
        Get ordered state.

        This property is used to indicate whether or not the order
        of the JSON data will be preserved.

        Note:
            This option cannot be used with `dataclasses`

        bool: Ordered state
        """
        return self._ordered

    @ordered.setter
    def ordered(self, value):
        self._ordered = bool(value)

    @staticmethod
    def _create_dataclass(obj, plain_dict=False):
        """
        Create data class for the given object.

        Args:
            obj (dict): Encoded dataclass object.
            plain_dict (bool): Set to `True` when object is a plain dict.

        Returns:
            dataclass: Decoded dataclass object.
        """
        if plain_dict:
            items = obj
            name = "Obj"
        else:
            name = obj["class_name"]
            items = obj["data"]

        cls = dataclasses.make_dataclass(name, items.keys())
        return cls(**items)

    def decode(self, obj):
        """
        Decode JSON object.

        Args:
            obj (object): Some object to be decoded.

        Returns:
            object: Decoded value.
        """
        # Handle tagged entries.
        if "$jsonio-value" in obj:
            key = obj.get("$jsonio-key")
            handler = self.handlers.get(key)
            if handler and handler.active:
                obj = handler.decode(obj["$jsonio-value"])

        # Handle OrderedDict objects (i.e. not compatible with dataclasses)
        if isinstance(obj, collections.OrderedDict):
            return obj

        # Handle plain dict objects.
        if isinstance(obj, dict) and self.dataclasses:
            obj = self._create_dataclass(obj, plain_dict=True)

        return obj

    def __call__(self, obj):
        return self.decode(obj)
