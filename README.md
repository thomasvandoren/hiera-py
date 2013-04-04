hiera-py
========
Python interface for the hiera hierarchical database.

See the
[documentation on puppetlabs.com](http://docs.puppetlabs.com/hiera/latest/) for
more detail.

Installation
------------

```bash
pip install hiera-py

# Or, if you prefer easy_install:
easy_install hiera-py

# Or, if you prefer to install from source:
python setup.py install
```

Getting Started
---------------

```python
>>> import hiera
>>> hiera_client = hiera.HieraClient('/etc/hiera.yml', environment='dev')
>>> hiera_client.get('my_key')
'my_value'
>>> hiera_client.get('nonexistent_key')
Traceback (most recent call last):
...
hiera.exc.HieraError: Failed to retrieve key nonexistent_key. ...
```

License
-------
BSD

Authors
-------
Thomas Van Doren

Testing
-------

```bash
# Run the tests against python 2.7.
tox

# Run the tests against python 2.7 with code coverage.
tox -e cover

# Run the tests against a bunch of python versions.
tox -e py25,py26,py27,py31,py32,py33,pypy
```
