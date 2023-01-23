#Lists 
frutas = ['Apple', 'Banana', 'Tomatoes', 'Banana']
datos=[1,'a',1232312,'31231',7]
numeros=[1,2,43,543,2342,231,13,87,67]

#Count List elements 
print(len(datos))


#Type of 
print(type(frutas))
if(type(frutas)==list):
    print('Hello')

#First element matched
print(frutas.index('Banana'))
#Count elements within the list
print(frutas.count('Apple'))

#Max List elements
print(max(numeros))
print(min(numeros))

#Access index values 
print(frutas[-2])
print(frutas[1])

#other way around
print(frutas[::-1])
 
frutas[1:3]=['Perro','Mora','Mango','Cebolla']
print(frutas)

#Insert new values into the List
frutas.insert(2,'Elemento')
print(frutas)

#Insert last position 
frutas.append('Gato')
print(frutas)


#Join to Lists 
frutas_2 = ['Peras','Fresas','Banana']

frutas.extend(frutas_2)
print(frutas)

#Remove elements within the list
frutas.remove('Banana')
print(frutas)

frutas.pop(1)
print(frutas)







