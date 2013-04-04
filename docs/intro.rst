Introduction
============

Installation
------------

.. code-block:: bash

    pip install hiera-py

    # Or, if you prefer easy_install:
    easy_install hiera-py

    # Or, if you prefer to install from source:
    python setup.py install

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
