#Functions

#Return multiples variables
def arithmetic(a , b):

    add= a + b
    sub= a - b
    multiply= a * b
    division=a/b
    
    return add, sub, multiply, division

#red four return values in four variables
a, b, c, d = arithmetic(11,3)
print(a)
print(b)
print(c)
print(d)

#Default Arguments 
def print_name(name='Pepito', last_name='Perez'):
    print('Hola',name, last_name)

print_name()
print_name('Pepito', 'Perez')

