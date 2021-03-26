# A list is a collection which is ordered and changable. Allows duplicate members

# Create a list
numbers=[1,2,3,4,5]
fruits=['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
#numbers2= list((1,2,3))

# Get a value
print(fruits[1])

# Get a lenght
print(len(fruits))

# Append to list
fruits.append('Mangos')
print(fruits)
 
 # Remove from a list
fruits.remove('Grapes')
print(fruits)
 
  # Insert into position 
fruits.insert(2,'Strawberries')
print(fruits) 

 # Change value
fruits[0]='Blueberries'
print(fruits) 

 # Remove position 
fruits.pop(2)
print(fruits) 

 # Reverse 
fruits.reverse()
print(fruits) 

# Sort list
fruits.sort()
print(fruits) 

# Reverse sort
fruits.sort(reverse=True)
print(fruits) 