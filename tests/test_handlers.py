import collections
import datetime
import pytest

import jsonio


def test_datetime_handler_as_dicts():
    """
    Test encoding/decoding datetime objects.

    This test demonstrates how `jsonio` handles datetime objects.
    """
    timestamp = datetime.datetime.now()
    before = {"timestamp": timestamp}
    encoded = jsonio.dumps(before, indent=2)
    after = jsonio.loads(encoded)
    assert before == after


def test_datetime_handler_with_dataclasses():
    """
    Test encoding/decoding date/time objects as dataclasses.

    This class demonstrates how the date/time handler works in
    conjunction with the dataclass handler.
    """
    if jsonio.processor.dataclasses:
        timestamp = datetime.datetime.now()
        before = {"timestamp": timestamp}
        encoded = jsonio.dumps(before, indent=2)
        after = jsonio.loads(encoded, dataclass=True)
        assert after.timestamp == timestamp


def test_ordered_dict_handler():
    """
    Test encoding/decoding JSON OrderedDict objects.

    This test demonstrates how `jsonio` handles OrderedDict objects.
    """
    before = collections.OrderedDict([("b", 2), ("a", 1)])
    encoded = jsonio.dumps(before, indent=2)
    after = jsonio.loads(encoded)
    assert before == after


def test_ordered_dict_handler_raises_value_error_with_dataclasses():
    """
    Test ordered dict encoding/decoding with active dataclass handler.

    This test demonstrates the error handling when using ordered dict
    objects with the dataclass handler (mutually exclusive options).
    """
    with pytest.raises(ValueError):
        before = collections.OrderedDict([("b", 2), ("a", 1)])
        encoded = jsonio.dumps(before, indent=2)
        jsonio.loads(encoded, ordered=True, dataclass=True)


def test_preserving_order_from_json_file(json_path):
    """
    Test loading a JSON document and preserving the order.

    This test demonstrates how to preserve the order of the keys when
    loading a JSON document.
    """
    data = jsonio.read(json_path, ordered=True)
    assert isinstance(data, collections.OrderedDict)
    assert list(data.keys()) == ["timestamp", "datestamp"]
