Install
-------

with pip (recommended):
^^^^^^^^^^^^^^^^^^^^^^^
*Optional* use `virtualenv <http://pypi.python.org/pypi/virtualenv>`_:

- ``virtualenv venv``
- ``source venv/bin/activate``

``[sudo] pip install oopen``


with easy_install:
^^^^^^^^^^^^^^^^^^

``sudo easy_install oopen``


from source:
^^^^^^^^^^^^
*update version numbers where appropriate*

`Download latest release from PyPI <http://pypi.python.org/pypi/oopen/>`_

``tar -xvzf oopen-x.x.x.tar.gz``

``cd oopen-x.x.x``

``[sudo] python setup.py install``

from git:
^^^^^^^^^
*Useful for specifying an exact commit, or for local development.*

``pip install-e git+https://github.com/ajhekman/OOpen#egg=oopen``

*you may also specify a tag or commit hash after the URL*

``pip install -e git+https://github.com/ajhekman/OOpen@0.1.1#egg=oopen``

``pip install -e git+https://github.com/ajhekman/OOpen@47f6e43cfc6391c06ae2a9eda6f63300c1b0558c#egg=oopen``


Uninstall:
----------

``pip uninstall oopen``
