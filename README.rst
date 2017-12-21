`hyperschema <https://github.com/wuan/python-hyperschema>`_
===========================================================

.. image:: https://badge.fury.io/py/hyperschema.png
    :alt: PyPi-Package
    :target: https://badge.fury.io/py/hyperschema
.. image:: https://travis-ci.org/wuan/python-hyperschema.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/wuan/python-hyperschema
.. image:: https://coveralls.io/repos/wuan/python-hyperschema/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/wuan/python-hyperschema?branch=master

python client library to build a JSON hyperschema client for
`https://github.com/Mercateo/rest-schemagen <https://github.com/Mercateo/rest-schemagen>`_

Examples
========

.. code-block:: python

    root = Link(base_url).follow()

    stations = root.follow('stations')

    # create station
    new_station = stations.follow('create', {'name': 'station-name', 'longitude': 11.0, 'latitude': 49.0})

    stations = stations.update()
    for station in stations:
        print("   ", station.data)

    # delete created station
    new_station.follow('delete')
