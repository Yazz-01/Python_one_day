# A class is like a blueprint for creating objets. An object has properties and methods
#(functions) associated with it. Almost everything in Python is an object.

# Create a class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name= name
        self.email= email
        self.age= age


def greeting(self):
    return f'My name is {self.name} and I am {self.age}'



def has_birthday(self):
   self.age +=1


# Extend Class
class Customer(User):

# Init user object
brad= User('Brad Traversy', 'brada@gmail.com', 37)
brad,has_birthday()
print(brad.greeting())