## [python simple dependency injection](./dependency_injection.py)

A minimal dependency injector for python

## How to use

Create an injectable class

```python
from dependency_injection import Injectable

class Service(Injectable):

    def __init__(self) -> None:
        self._values = list()

    def add_value(self, value) -> None:
        self._values.append(value)
```

Then inject the service into a class

```python
from dependency_injection import Inject
from service import Service

class MyClass:

    service = Inject(Service)

    def add_value(self, value):
        self.service.add_value(value)
```

Or access directly the singleton instance:

```python
from service import Service

if __name__ == "__main__":
    Service.Instance.add_value("value1")
```
