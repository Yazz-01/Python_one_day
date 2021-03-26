# If / Else conditions are used to decide to do something based on something being true or false
x=13
y=13


# Simple if
# Comparison Operators (==, !=, >, <, >=, <=) Used to compare values
# if x>y:
#     print(f'{x} is greater than {y}')

# # if/Else
# if x>y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{y} is greater than {x}')

# elif
if x>y:
    print(f'{x} is greater than {y}')

elif x==y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')



# Nested if 
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 less than or equeal to 10')


# Logical operators (and, or, not) Used to combine conditional statements

# and
# if x  > 2 and x<=10: 
#     print(f'{x} is greater than 2 less than or equeal to 10')
# # or
# if x  > 2 or x<=10: 
#     print(f'{x} is greater than 2 less than or equeal to 10')

# # not
# if not(x==y): 
#     print(f'{x} is not equeal to 10')

# Membership Operators (not, not in) Membership operators are used to test if a sequence is present 
# in an object 
numbers=[1,2,3,4,5]
# in
if x in numbers:
    print(x in numbers)

# not in
if x not in numbers:
    print(x not in numbers)


# Identity Opertors (is,is not) COmpare the objects, not if they are equal, bt if they
# are actually the same object, with the same memory location:

#is 
if x is y:
    print(x is y)

    #is 
if x is y:
    print(x is y)