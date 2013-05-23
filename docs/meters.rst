Meters
======

.. autoclass:: effipy.meters.Meters
   :members:
   :undoc-members:
   :inherited-members:
   :exclude-members: create

   .. py:function:: create(dict)
   
     Create a new invoice with a dict that will be converted to JSON.
     
     :param dict dict: A dictionary with invoice data like the following:
     
     .. code-block:: javascript

        {
          "id": "sample string 1",
          "usagePointId": "sample string 2"
        }
