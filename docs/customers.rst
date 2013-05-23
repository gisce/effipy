Customers
=========

.. autoclass:: effipy.customers.Customers
   :members:
   :undoc-members:
   :inherited-members:
   :exclude-members: create

   .. py:function:: create(dict)
   
     Create a new customer withi a dict that will be converted to JSON.
     
     :param dict dict: A dictionary with customer data like the following:
     
     .. code-block:: javascript
     
          {
           "id": "Identificador unico cliente",
           "fiscalId": "CIF, NIF, Pasaporte",
           "firstName": "Nombre",
           "firstSurname": "Primer apellido",
           "secondSurname": "Segundo apellido",
           "email": "correo@cliente.com",
           "address": {
               "street": "Calle y número",
               "postalCode": "CodigoPostal",
               "city": "Nombre ciudad",
               "cityCode": "Código INE ciudad",
               "province": "Nombre provincia",
               "provinceCode": "Código INE provincia",
               "country": "España",
               "countryCode": "Codigo",
               "parcelNumber": "Referencia catastral"
            }
         }
   
