#Manage String Variables

a="""This message contains information: Andres Lara"""

b="Hola, Andres"

print(b[0:5])
print(b[5:10])
print(b[2:10])
#sort the string backwards
print(b[::-1])

#Covert to lower
print(b.lower())
#Remove the white space at the start and at end of the string
print(b.strip())


#Separate the string
print(b.split(","))

#replace a Letter with Other
b=b.replace("Hola", "hey")
print(b)

a="Holi"
c="Devep"
s=","

#Joint strings
t=a+s+c
print(t)

#Printing using sorting variables
quatity=1
num=30
price=3450

salida = 'El valor {} y la cantidad {} y el id {}'
print(salida.format(price,quatity,num))

salida = 'El valor {1} y la cantidad {2} y el id {0}'
print(salida.format(num,price,quatity))

# Using len
#Count a string characters
print('Write your frase')
f=input()

print('The number of charaters for the string is:')
print(len(f))