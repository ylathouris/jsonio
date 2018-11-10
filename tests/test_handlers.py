
import collections
import datetime
import json
import tempfile
import os
import uuid

import jsonio


def test_datetime_handler():
    """
    Test encoding/decoding datetime objects.

    This test demonstrates how `jsonio` handles datetime objects.
    """
    timestamp = datetime.datetime.now()
    before = {'timestamp': timestamp}
    encoded = jsonio.dumps(before, indent=2)
    after = jsonio.loads(encoded)
    assert before == after


def test_ordered_dict_handler():
    """
    Test encoding/decoding JSON OrderedDict objects.

    This test demonstrates how `jsonio` handles OrderedDict objects.
    """
    before = collections.OrderedDict([('b', 2), ('a', 1)])
    encoded = jsonio.dumps(before, indent=2)
    after = jsonio.loads(encoded)
    assert before == after
