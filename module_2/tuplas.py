#Tuple 
#Tuple cannot be modified (readonly)
lista= ['Perro','Gato','Mosquito','Mate','Pollo']
tupla=('Nala','Perro',2123)
h=tuple(lista)
print(h)
print(tupla)

#Read Tuples
print(lista[2])
print(tupla[1])


# Asign values
(nala,perro,numero)=tupla
print(nala)
print(numero)

#Asing leftovers to latest variable.
tupla_2=('Nala','Perro','400',9000)
(nala,perro,*numero)=tupla_2
print(nala)
print(numero)

#Sum Tuples
print(tupla + tupla_2)

#Multiplicar Datos de una tupla, Numero de incrementos de la tupla 
new_tupla=tupla_2*3
print(new_tupla)