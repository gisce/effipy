UsagePoints
===========

.. autoclass:: effipy.usagepoints.UsagePoints
   :members:
   :undoc-members:
   :inherited-members:
   :exclude-members: create

   .. py:function:: create(dict)
   
     Create a new Usagepoint with a dict that will be converted to JSON.
     
     :param dict dict: A dictionary with Usagepoint data like the following:
     
     .. code-block:: javascript
     
        {
          "id": "ES0987543210987654ZF",
          "address": {
            "street": "Calle y número",
            "postalCode": "CodigoPostal",
            "city": "Nombre ciudad",
            "cityCode": "Código INE ciudad",
            "province": "Nombre provincia",
            "provinceCode": "Código INE provincia",
            "country": "España",
            "countryCode": "ES. Codigo según ISO 3166",
            "parcelNumber": "Referencia catastral"
          }
        }
