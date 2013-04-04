Development
===========

Testing
-------

Tox is used to run the tests. Travis automatically verifies commits. It uses
python 2.7 and pep8.

.. code-block:: bash

    # Run the tests against python 2.7.
    tox

    # Run the tests against python 2.7 with code coverage.
    tox -e cover

    # Run the tests against a bunch of python versions.
    tox -e py25,py26,py27,py31,py32,py33,pypy
