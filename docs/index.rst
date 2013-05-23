EffiPy
======

EffiPy is a pythonic library to access EffiPeople REST API based on `libsaas <http://libsaas.net/>`_


Argot
-----

* Create is ``service.object().create(dict)``.
* Read all is ``service.object().get()``.
* Read one is ``service.object(identifier).get()``.
* Update all is ``service.object().update(list_of_dicts)``.
* Update one is ``service.object(identifier).update(dict)``.
* Delete is ``service.object(identifier).delete()``.


Note: All the ``get()`` methods have optional parameters limit and offset.


EffiPy API
==========

.. toctree::
   
   resource
   service
   customers
   contracts
   invoices
   tariffs
   usagepoints
   meters
