# useful-creator

A part of the `useful` Python modules collection dedicated to creating object instances from a configuration dictionary. Working with dictionaries instead of `JSON` or `Yaml` allows us to decouple from handling/parsing configuration files. The general idea is

```python
creator = Creator(...)
configuration = {...}
obj = creator.create(configuration)
```

where `Creator` is an implementation of the `useful.creator.BaseCreator` class. At the moment, provided implementations are:

* `RegistryCreator`
* `GenericCreator`

***

## `RegistryCreator`

`RegistryCreator(registry)` implementation requires a `registry` object that provides a mapping from string values to class objects ready to be instantiated, i.e. `cls = registry[key]`. `registry` argument can be a simple Python `dict`. This way, we have to register every class implementation we want to allow to be created from a config dictionary. This also gives us the freedom to use simpler names in configuration files, for example:

```python
from useful.creator import RegistryCreator

import example


class SomeExample:
    def __init__(self, argument):
        self.argument = argument

    def test(self):
        print("SomeExample:", self.argument)


configuration = {
    "Example": {
        "argument": 1
    }
}

registry = {}
registry["Another"] = example.AnotherExample
registry["Example"] = SomeExample

creator = RegistryCreator(registry)
obj = creator.create(configuration)
obj.test()
```

which would output

```python
SomeExample: 1
````

Using RegistryCreator allows us to simply use names `Example` or `Another` in configuration dictionaries. In general, the configuration format is

```json
{
    str: dict
}
```

Here is another example configuration

```json
{
    "name": {
        "param": "eters",
        "other": 123
    }
}
```

where `name` is interpreted as a key in the registry, and the dictionary value under that key is unpacked (`**kwargs`). The end result is basically

```python
cls = registry["name"]
obj = cls(param="eters", other=123)
```

## `GenericCreator`

This implementation requires a more verbose configuration, but doesn't need a prior registration of classes. Here is a simple usage example

```python
from useful.creator import GenericCreator

configuration = {
    "class": {
        "name": "ClassName",
        "module": "class.module"
    },
    "params": {
        "param": "eters",
        "other": 123
    }
}

creator = GenericCreator()
obj = creator.create(configuration)
```

which would basically execute

```python
obj = class.module.ClassName(param="eters", other=123)
```
