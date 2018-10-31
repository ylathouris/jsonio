
"""JSON Helpers"""

import collections
import datetime
import dateutil.parser
import json

try:
    import dataclasses
except ImportError:
    dataclasses = None


__all__ = [
    'read',
    'write',
    'load',
    'loads',
    'dump',
    'dumps',
    'encode',
    'decode',
]


def encode(obj):
    """
    Encode the given object so it can be serialized to JSON.

    Args:
        obj: Object to be serialized.

    Returns:
        object: JSON serializable object.
    """
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return {'datatype': type(obj).__name__, 'data': obj.isoformat()}
    elif dataclasses and dataclasses.is_dataclass(obj):
        return {'datatype': 'dataclass', 'data': obj.__dict__}

    return obj


def decode(obj):
    """
    Decode the given object to it's original form.

    Args:
        obj: JSON serialized object to be decoded.

    Returns:
        object: Deserialized object.
    """
    if 'datatype' in obj and 'data' in obj:
        if obj['datatype'] == 'datetime':
            return dateutil.parser.parse(obj['data'])
        elif obj['datatype'] == 'date':
            return dateutil.parser.parse(obj['data']).date()
        elif obj['datatype'] == 'dataclass':
            data = obj['data']
            objtype = dataclasses.make_dataclass('Dataclass', data.keys())
            obj = objtype(**data)

    return obj


def read(path, **kwargs):
    """
    Read JSON data from the file at the given path.

    Args:
        path (str): Path to JSON file.

    Returns:
        dict: Loaded JSON data.
    """
    with open(path, 'r') as json_file:
        return load(json_file, **kwargs)


def load(fileobj, **kwargs):
    """
    Load JSON data from the given file.

    Args:
        fileobj (file): File object.

    Returns:
        dict: Loaded JSON data.
    """
    options = _resolve_load_options(kwargs)
    return json.load(fileobj, **options)


def loads(text, **kwargs):
    """
    Load JSON data from the given text.

    Args:
        text (str): File contents.

    Returns:
        dict: Loaded JSON data.
    """
    options = _resolve_load_options(kwargs)
    return json.loads(text, **options)


def _resolve_load_options(options):
    """
    Resolve the JSON load options.

    Args:
        options (dict): Options passed to `json.loads`

    Returns:
        dict: JSON load Options
    """
    options.setdefault('object_hook', decode)
    ordered = options.pop('ordered', False)
    if ordered:
        options.setdefault('object_pairs_hook', collections.OrderedDict)

    return options


def write(data, path, **kwargs):
    """
    Dump JSON data to the given file.

    Args:
        data (dict): Data to be dumped to file.
        path (str): Path to JSON file.

    Returns:
        str: JSON formatted data.
    """
    with open(path, 'w') as json_file:
        return dump(data, json_file, **kwargs)


def dump(data, fileobj, **kwargs):
    """
    Dump JSON data to the given file.

    Args:
        data (dict): Data to be dumped to file.
        path (str): Path to JSON file.

    Returns:
        str: JSON formatted data.
    """
    kwargs.setdefault('default', encode)
    return json.dump(data, fileobj, **kwargs)


def dumps(data, **kwargs):
    """
    Dump JSON data to plain text.

    Args:
        data (dict): Data to be dumped to plain text (i.e. file contents).

    Returns:
        str: JSON data as plain text.
    """
    kwargs.setdefault('default', encode)
    return json.dumps(data, **kwargs)
