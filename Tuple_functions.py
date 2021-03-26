# A Tuple is a collection which is ordered and unchangable. Allows duplicate members.

# Create a Tuple
fruits= ('Apples','Grapes','Oranges')

# Create a Tuple using a construtor
#fruits2= tuple(('Apples','Grapes','Oranges'))

# Single value need a trailing comma
fruits2=('Apples',)


#Get Value
print(fruits2, type(fruits2))

# Can't change the value
#fruits[0]='Pears'

# Delete tuple
del fruits2

#print(fruits2)


# Get Lenght
print(len(fruits))


# A set is a collection which is unordered and unindexed. No duplicate members.

# Create a set
fruits_set= {'Apples', 'Oranges','Mango'}

# Check if is in set
print('Apples' in fruits_set)


# Add to set
fruits_set.add('Grape')
print(fruits_set)

# Remove from set
fruits_set.remove('Grape')
print(fruits_set)

# Clear set
fruits_set.clear()
print(fruits_set)

# Delete set
del fruits_set
print(fruits_set)