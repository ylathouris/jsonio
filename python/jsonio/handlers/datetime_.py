
import datetime
import dateutil.parser

from .base import Handler



class DateTimeHandler(Handler):
    """
    DateTime JSON Handler.

    This class is used to handle the encoding/decoding
    of date/datetime objects.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize datetiime handler.
        """
        super(DateTimeHandler, self).__init__(*args, **kwargs)
        self._fmt = None

    @property
    def fmt(self):
        """
        Get/set datetime format.
        """
        return self._fmt

    @fmt.setter
    def fmt(self, fmt):
        self._fmt = str(fmt) if fmt else None

    def match(self, obj):
        """
        Check if the given object is a datetime object.

        Args:
            obj: Object to be encoded

        Returns:
            bool: True if this is a matching handler, false otherwise.
        """
        return isinstance(obj, (datetime.date, datetime.datetime))

    def encode(self, obj):
        """
        Encode the given datetime object.

        Args:
            datetime.datetime: datetime object

        Returns:
            dict: Encoded datetime object.
        """
        if not self.fmt:
            data = obj.isoformat()
        else:
            data = obj.strftime(self.fmt)

        return {"type": type(obj).__name__, "data": data}

    def decode(self, obj):
        """
        Decode the given datetime object.

        Args:
            obj (dict): Encoded datetime object.

        Returns:
            datetime.date or datetime.datetime: Decoded datetime object.
        """
        if isinstance(obj, dict):
            date_type = obj["type"]
            data = obj["data"]
        else:
            date_type = obj.type
            data = obj.data

        valid_types = ["date", "datetime"]
        if date_type not in valid_types:
            msg = "Invalid datetime encoding." "Expected type key with one of {}"
            msg = msg.format(valid_types)
            raise ValueError(msg)

        if date_type == "date":
            return dateutil.parser.parse(data).date()
        else:
            return dateutil.parser.parse(data)
