Introduction
============


.. image:: https://readthedocs.org/projects/circuitpython-adt7410/badge/?version=latest
    :target: https://circuitpython-adt7410.readthedocs.io/
    :alt: Documentation Status


.. image:: https://img.shields.io/pypi/v/circuitpython-adt7410.svg
    :alt: latest version on PyPI
    :target: https://pypi.python.org/pypi/circuitpython-adt7410

.. image:: https://static.pepy.tech/personalized-badge/circuitpython-adt7410?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Pypi%20Downloads
    :alt: Total PyPI downloads
    :target: https://pepy.tech/project/circuitpython-adt7410

.. image:: https://github.com/jposada202020/CircuitPython_ADT7410/workflows/Build%20CI/badge.svg
    :target: https://github.com/jposada202020/CircuitPython_ADT7410/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

CircuitPython Driver for the Analog Devices ADT7410 Temperature Sensor


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Community Bundle library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.


Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/circuitpython-adt7410/>`_.
To install for current user:

.. code-block:: shell

    pip3 install circuitpython-adt7410

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-adt7410

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install circuitpython-adt7410

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install adt7410

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

Take a look at the examples directory

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://circuitpython-adt7410.readthedocs.io/>`_.
