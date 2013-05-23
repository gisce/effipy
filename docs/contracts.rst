Contracts
=========

.. autoclass:: effipy.contracts.Contracts
   :members: delete, get
   :inherited-members:
   :exclude-members: create

   .. py:function:: create(dict)
   
     Create a new contract with a dict that will be converted to JSON.
     
     >>> ef.customer(1234).contracts().create()
     
     :param dict dict: A dictionary with contract data like the following:
     
     .. code-block:: javascript
        
        {
          "id": "IdentificadorContrato",
          "customerId": "IdentificadorCliente",
          "version": "2",
          "start": 1332806400,
          "end": 1362009600,
          "tariffId": "2.0A",
          "power": 3300,
          "activityCode": "CNAE",
          "usagePointId": "ES0987543210987654ZF"
        }
