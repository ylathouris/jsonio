"""JSON Helpers"""

import collections
import json

from .processor import Encoder, Decoder


__all__ = ["read", "write", "load", "loads", "dump", "dumps", "encode", "decode"]


def read(path, **kwargs):
    """
    Read JSON data from the file at the given path.

    Args:
        path (str): Path to JSON file.

    Returns:
        dict: Loaded JSON data.
    """
    with open(path, "r") as json_file:
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
    result = json.load(fileobj, **options)
    return result


def loads(text, **kwargs):
    """
    Load JSON data from the given text.

    Args:
        text (str): File contents.

    Returns:
        dict: Loaded JSON data.
    """
    options = _resolve_load_options(kwargs)
    result = json.loads(text, **options)
    return result


def _resolve_load_options(options):
    """
    Resolve the JSON load options.

    Args:
        options (dict): Options passed to `json.loads`

    Returns:
        dict: JSON load Options
    """
    decoder = Decoder()
    decoder.dataclasses = options.pop('dataclass', False)
    decoder.ordered = options.pop('ordered', False)
    options.setdefault("object_hook", decoder)

    if decoder.ordered:
        if decoder.dataclasses:
            msg = (
                "Cannot use ordered option with dataclasses.\n"
                "Please specify one or the other."
            )
            raise ValueError(msg)

        options.setdefault("object_pairs_hook", collections.OrderedDict)

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
    with open(path, "w") as json_file:
        return dump(data, json_file, **kwargs)


def dump(data, fileobj, **kwargs):
    """
    Dump JSON data to the given file.

    Args:
        data (dict): Data to be dumped to file.
        fileobj (file): Path to JSON file.

    Returns:
        str: JSON formatted data.
    """
    encoder = kwargs.pop('encoder', Encoder())
    encoder.dataclasses = kwargs.pop('dataclass', True)
    kwargs.setdefault("default", encoder)
    return json.dump(data, fileobj, **kwargs)


def dumps(data, **kwargs):
    """
    Dump JSON data to plain text.

    Args:
        data (dict): Data to be dumped to plain text (i.e. file contents).

    Returns:
        str: JSON data as plain text.
    """
    encoder = kwargs.pop('encoder', Encoder())
    encoder.dataclasses = kwargs.pop('dataclass', True)
    kwargs.setdefault("default", encoder)
    return json.dumps(data, **kwargs)
