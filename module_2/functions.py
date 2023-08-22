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
print_name('Gonzalo', 'Gomez')

# Var
#We can pass any number of arguments to this function. Internally all these values are represented in the form of a tuple.
def addition(*nums):
    sum = 0 
    for i in nums:
        if(i>=0):
            print(i, end='\n')
            sum += i
        else:
            sum += i
    print('Suma: ', sum)
    return sum

addition(10,10,12,2131,21312)
addition(10,10,12,2131,21312, 10,10,12,2131,21312,10,10,12,2131,2131210,10,12,2131,2131210,10,12,2131,21312,-3000000)