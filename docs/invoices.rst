Invoices
========

.. autoclass:: effipy.invoices.Invoices
   :members:
   :undoc-members:
   :inherited-members:
   :exclude-members: create

   .. py:function:: create(dict)
   
     Create a new invoice with a dict that will be converted to JSON.
     
     :param dict dict: A dictionary with invoice data like the following:
     
     .. code-block:: javascript
     
         {
              "number": "Número de factura",
              "customerId": "Identificador único del cliente",
              "contractId": "Identificador único del contrato",
              "usagePointId": "ES0987543210987654ZF",
              "activityCode": "Código CNAE",
              "tariffId": "2.0A",
              "power": 5500,
              "activeEnergyConsumption": 400,
              "reactiveEnergyConsumption": 225,
              "isConsumptionEstimated": false,
              "activeEnergyCost": 200.0,
              "reactiveEnergyCost": 100.0,
              "powerCost": 300.0,
              "servicesCost": 75.0,
              "rentalsCost": 100.0,
              "otherCost": 50.0,
              "subtotal": 825.0,
              "otherTaxes": 6.75,
              "currencyCode": "Euro",
              "invoiceDate": 1363301230,
              "periodStart": 1363301020,
              "periodEnd": 13633012000,
              "vat": 173.25,
              "totalTaxes": 180.0,
              "total": 1005.0,
              "tariffType": "2.0DHA"
         }
