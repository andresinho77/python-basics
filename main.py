#User adds number into a list
print('Adding values to the list')
numero = 1
lista = []

num=input('cuantos numeros desea ingresas: ')

for i in range(int(num)):
    print('Add the number of the list ',i+1,':')
    numero=input()
    lista.append(str(numero))

print(lista)