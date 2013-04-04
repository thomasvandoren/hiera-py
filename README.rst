hiera-py
========
Python interface for the hiera hierarchical database.

.. image:: https://travis-ci.org/thomasvandoren/hiera-py.png?branch=master
    :target: https://travis-ci.org/thomasvandoren/hiera-py

See the `documentation on puppetlabs.com
<http://docs.puppetlabs.com/hiera/latest/>`_ for more detail.

Installation
------------

.. code-block:: bash

    pip install hiera-py

    # Or, if you prefer easy_install:
    easy_install hiera-py

    # Or, if you prefer to install from source:
    python setup.py install

Supported python versions
~~~~~~~~~~~~~~~~~~~~~~~~~

* 2.7
* PyPy

Eventually, I would like to support 3.x and 2.6+.

Getting Started
---------------

.. code-block:: pycon

    >>> import hiera
    >>> hiera_client = hiera.HieraClient('/etc/hiera.yml', environment='dev')
    >>> hiera_client.get('my_key')
    'my_value'
    >>> hiera_client.get('nonexistent_key')
    Traceback (most recent call last):
    ...
    hiera.exc.HieraError: Failed to retrieve key nonexistent_key. ...

License
-------
BSD

Authors
-------
Thomas Van Doren

Testing
-------

.. code-block:: bash

    # Run the tests against python 2.7.
    tox

    # Run the tests against python 2.7 with code coverage.
    tox -e cover

    # Run the tests against a bunch of python versions.
    tox -e py25,py26,py27,py31,py32,py33,pypy
