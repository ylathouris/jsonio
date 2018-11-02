![Coverage](coverage.svg)

---

# jsonlib

The `jsonlib` package provides utility functions for reading and writing JSON data. It supports the following features:

* [Easy Read/Write](#readwrite)
* [Functions Like The `json` Library](#json)
* [Supports `datetime/date` Objects](#datetime)
* [Supports `dataclasses` (Python 3.7+)](#dataclass)
* [Supports `OrderedDict` Objects](#ordereddict)

</br>

### <a name="readwrite"></a>Easy Read/Write

**Read**

```python
import jsonlib

data = jsonlib.read('/foo/bar.json')
```

**Write**

```python
import jsonlib

jsonlib.write({'foo': 'bar'}, '/foo/bar.json')
```

</br>


### <a name="json"></a>Functions Like The `json` Library

**Load**

```python
import jsonlib

with open('/foo/bar.json', 'r') as jsonfile:
    data = jsonlib.load(jsonfile)
```

**Loads**

```python
import jsonlib

data = jsonlib.loads('{"foo": "bar"}')
```

**Dump**

```python
import jsonlib

with open('/foo/bar.json', 'w') as jsonfile:
    jsonlib.dump({'foo': 'bar'}, jsonfile)
```

**Dumps**

```python
import jsonlib

data = {
    'apple': 'crumble',
    'banana': 'split',
}

# Use standard options.
text = jsonlib.dumps(data, jsonfile, indent=2, sort_keys=True)
```

</br>


### <a name="datetime"></a>Supports `date/datetime` Objects


```python
import datetime
import jsonlib

before = {
    'date': datetime.date.today(),
    'timestamp': datetime.datetime.now(),
}

jsonlib.write(before, '/foo/bar.json')
after = jsonlib.read('/foo/bar.json')
assert before == after  # True
```

</br>


### <a name="dataclasses"></a>Supports `dataclasses` (Python 3.7+)

```python
from dataclasses import dataclass
import jsonlib


@dataclass
class Fruit:
    apple: str
    banana: str


before = Fruit(apple='Fuji', banana='Lady Finger')

jsonlib.write(before, '/foo/bar.json')
after = jsonlib.read('/foo/bar.json')
assert before == after  # True
```

</br>


### <a name="ordereddict"></a>Supports `OrderedDict` Objects

```python
import collections
import jsonlib

before = collections.OrderedDict([('banana', 'split'), ('apple', 'crumble')])

text = jsonlib.dumps(before, indent=2)
after = jsonlib.loads(text, ordered=True)
assert before == after  # True
```
