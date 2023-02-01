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
lista_resul = frutas + frutas_2
print(frutas)
print('***********+',lista_resul)

#Remove elements within the list
frutas.remove('Banana')
print(frutas)

frutas.pop(1)
print(frutas)

#Delete remove
del frutas[1]
print(frutas)

#Clear the List
brands=['Mazda','Ford','Tesla','BWM','Mercedes','Chevrolet']
numbers= [1,32,43,5,6,7,23,2,34,5,432,2,3,4,223,6]
print(brands)
# brands.clear()
# print(brands)
# brands.append('Nala')
# print(brands)

#Sort the list
brands.sort()
print(brands)

#Sort the other way around
brands.sort(reverse=True)
print(brands)
brands.reverse()
print(brands)

numbers.sort()
print(numbers)

#Note: You CANNOT sort Mix List (int and String)

#Copy lists 
brand_new=brands.copy()
brand_new.append('Ferrari')
print(brand_new)

brand_new_list=list(brand_new)
print(brand_new_list)

# Exercise to reverse each word  of a string
def reverse_words(Sentence):
    # Split string on whitespace
    words = Sentence.split(" ")
    # iterate list and reverse each word using ::-1
    new_word_list = [word[::-1] for word in words]
    # Joining the new list of words
    res_str = " ".join(new_word_list)
    return res_str

# Given String
str1 = "Hola Andres"
print(reverse_words(str1))