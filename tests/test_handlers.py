
import collections
import datetime
import json
import tempfile
import os
import uuid

import jsonlib


def test_datetime_handler():
    """
    Test encoding/decoding datetime objects.

    This test demonstrates how `jsonlib` handles datetime objects.
    """
    timestamp = datetime.datetime.now()
    before = {'timestamp': timestamp}
    encoded = jsonlib.dumps(before, indent=2)
    after = jsonlib.loads(encoded)
    assert before == after


def test_ordered_dict_handler():
    """
    Test encoding/decoding JSON OrderedDict objects.

    This test demonstrates how `jsonlib` handles OrderedDict objects.
    """
    before = collections.OrderedDict([('b', 2), ('a', 1)])
    encoded = jsonlib.dumps(before, indent=2)
    after = jsonlib.loads(encoded)
    assert before == after
