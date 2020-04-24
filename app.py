# dictionaries

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer['name'])

print(customer.get('birthdate', 'Jan 1 1980'))  # second argument is default if there isn't value

print(customer.get('age'))

phone = input('Phone: ')

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = ''

for number in phone:
    output += digits_mapping.get(number, "!") + ' '

print(output)






