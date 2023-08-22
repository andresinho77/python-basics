#Using If-statement

print('Please indicate your number A: ')
a=input()
print('Please indicate your number B: ')
b=input()

if(int(a) > int(b)):
    print('A es mayor que B')
else:
    print('B es mayor o igual A')   

#Using elseif
c=3
v=31

if(c>v):
    print('C es mayor que V')
elif c==v:
    print('c es igual a V')
else:
    print('v es mayor que c')

#Shor if
print('Andres:') if c > v else print ('Sandra')

#Using while:

num = 10
while(num > 0):
    print('Cuenta regresiva es: ',num)
    num-=1


#Printing even/odd numbers
n=1
while(n<=10):
    if(n%2)==0:
        print('El numero:',n,'es par')
    else:
        print('El numero:',n,'es impar')
    n+=1
else: 
    print('El while se termino')


#Using for in.
nombres=['andres','felipe','lara','buendia']

for nombre in nombres:
    print(nombre)

letras='pepito perez pererida'

for p in letras:
    print(p)


for numero in range(10):
    print(numero)


for numero in range(9,10):
    print(numero)


for lect in range(5,10):
    print(lect)
else:
    print('FOR has ended')