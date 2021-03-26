# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members

# Create a Dioctionary
person={
    'first_name':'John',
    'last_name':'Doe',
    'age':30
}
print(person, type(person))

# Use a constructor
#person2=dict(first_name='Sara',last_name='Williams')
#print(person2)


# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key value
person['phone']= '555-55-5555'

 # Get Dictionary keys
print(person.keys())

# Get Dictionary values
print(person.values())

# Get Dictionary items
print(person.items())


# Copy dict
person2= person.copy()
person2['city']='Boston'
print(person2)

# Removedict
del (person['age'])
person.pop('phone')
print(person)



# Clear
person.clear()

# Get Lenght
print(len(person2))

# List of dictionaries
people=[
    {'name':'Marha', 'age':30},
    {'name':'Kevin', 'age':25},
]

print(people[0]['age'])