# dictionaries

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer['name'])

print(customer.get('birthdate', 'Jan 1 1980'))  # second argument is default if there isn't value

print(customer.get('age'))





