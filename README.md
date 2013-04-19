# Python library for the EffiPeople REST API.

This is a pythonic library to access EffiPeople REST API.

## Argot

* **Create** is `service.object().create(dict)`.
* **Read all** is `service.object().get()`.
* **Read one** is `service.object(identifier).get()`.
* **Update all** is `service.object().update(list_of_dicts)`.
* **Update one** is `service.object(identifier).update(dict)`.
* **Delete** is `service.object(identifier).delete()`.

**Note**: All the `get()` methods have optional parameters `limit` and `offset`.

## Getting all the customers

```python
from effipy import EffiPeople
ef = EffiPeople(token='YOUR_TOKEN')
```

## Getting all the customers

```python
ef.customers().get()
```

## Creating a customer

```python
customer_data = {
    'address': {
        'city': 'Barcelona',
        'cityCode': None,
        'country': None,
        'countryCode': None,
        'parcelNumber': None,
        'postalCode': u'8012',
        'province': None,
        'provinceCode': None,
        'street': 'CL SIRACUSA 17 01 03 08012 (Barcelona)'
    },
 	'email': None,
 	'firstName': ' nom 00004',
 	'firstSurname': 'cognom',
 	'fiscalId': 'DNI00004Z',
 	'id': 'TST0001',
 	'secondSurname': None
}
ef.customers().create(customer_data)
```

## Getting a customer

```python
ef.customer('TST0001').get()
```

## Delete a customer

```python
ef.customer('TST0001').delete()
```
