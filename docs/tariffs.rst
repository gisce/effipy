Tariffs
=======

.. autoclass:: effipy.tariffs.Tariffs
   :members:
   :undoc-members:
   :inherited-members:
   :exclude-members: create

   .. py:function:: create(dict)
   
     Create a new tariffs with a dict that will be converted to JSON.
     
     :param dict dict: A dictionary with tariffs data like the following:
     
     .. code-block:: javascript

        {
          "id": "2.0DHA",
          "name": "Luz 10 (2.0A)",
          "tariffType": "2.0DHA",
          "version": "2",
          "start": 1363301230,
          "end": 1363304568,
          "periods": {
            "p1": {
              "activeEnergyPrice": 0.167658,
              "powerPrice": 1.824432
            },
            "p2": {
              "activeEnergyPrice": 0.05719,
              "powerPrice": 1.824432
            }
          }
        }
