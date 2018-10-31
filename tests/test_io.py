
import collections
import datetime
import json
import tempfile
import os
import uuid

import jsonio


def test_read_json_file(json_path):
    """
    Test reading a JSON file.

    This test demonstrates how to use ``jsonio`` to
    read a file containing JSON data.
    """
    data = jsonio.read(json_path)

    with open(json_path, 'r') as json_file:
        expected = json.load(json_file)

    assert data == expected


def test_load_json_file(json_path):
    """
    Test loading JSON data from a file object.

    This test demonstrates how to use ``jsonio`` to
    load JSON from a file object.

    Note:
        This method is similar to the `json.load` method.
    """
    with open(json_path, 'r') as json_file:
        data = jsonio.load(json_file)

    with open(json_path, 'r') as json_file:
        expected = json.load(json_file)

    assert data == expected


def test_load_json_data(json_path):
    """
    Test loading the contents of a JSON file.

    This test demonstrates how to use ``jsonio`` to
    load the contents of a JSON file.

    Note:
        This method is similar to the `json.loads` method.
    """
    with open(json_path, 'r') as json_file:
        contents = json_file.read()

    with open(json_path, 'r') as json_file:
        expected = json.load(json_file)

    data = jsonio.loads(contents)
    assert data == expected


def test_write_json_file():
    """
    Test writing data to a JSON file.

    This test demonstrates how to use ``jsonio`` to write
    out a JSON file.
    """
    root = tempfile.gettempdir()
    path = os.path.join(root, 'jsonio-{}'.format(uuid.uuid4()))
    assert not os.path.isfile(path)

    data = {'foo': 'bar'}
    jsonio.write(data, path, indent=2)
    assert os.path.isfile(path)

    os.remove(path)


def test_dump_json_file():
    """
    Test dumping data to JSON file.

    This test demonstrates how to use ``jsonio`` to dump data
    to a JSON file.

    Note:
        This method is similar to the `json.dump` method.
    """
    root = tempfile.gettempdir()
    path = os.path.join(root, 'jsonio-{}'.format(uuid.uuid4()))
    assert not os.path.isfile(path)

    data = {'foo': 'bar'}
    with open(path, 'w') as json_file:
        jsonio.dump(data, json_file, indent=2)
        assert os.path.isfile(path)

    os.remove(path)


def test_dump_json_to_string():
    """
    Test dumping data to a JSON formatted string.

    This test demonstrates how to use ``jsonio`` to dump data
    to a JSON formatted string.

    Note:
        This method is similar to the `json.dumps` method.
    """
    data = {'foo': 'bar'}
    text = jsonio.dumps(data, indent=2)
    assert isinstance(text, str)


def test_datetime_io():
    """
    Test reading/writing JSON files with datetime objects.

    This test demonstrates how `jsonio` handles datetime objects.
    """
    root = tempfile.gettempdir()
    path = os.path.join(root, 'jsonio-{}'.format(uuid.uuid4()))
    assert not os.path.isfile(path)

    timestamp = datetime.datetime.now()
    before = {'timestamp': timestamp}
    jsonio.write(before, path, indent=2)
    assert os.path.isfile(path)

    after = jsonio.read(path)
    assert before == after

    os.remove(path)


def test_ordered_dict_io():
    """
    Test reading/writing JSON files with OrderedDict objects.

    This test demonstrates how `jsonio` handles OrderedDict objects.
    """
    root = tempfile.gettempdir()
    path = os.path.join(root, 'jsonio-{}'.format(uuid.uuid4()))
    assert not os.path.isfile(path)

    before = collections.OrderedDict([('banana', 'split'), ('apple', 'crumble')])
    jsonio.write(before, path, indent=2)
    assert os.path.isfile(path)

    after = jsonio.read(path)
    assert before == after

    os.remove(path)
