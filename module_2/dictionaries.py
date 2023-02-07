person = {'name': 'Pepito', 'lastname':'Perez', 'age':35}

print(person['name'])
print(person.get('name'))

#Add Values:
person['calle']=100

print(person)

#Update Values:
person['calle']='Calle 100'
print(person)
person.update({'calle':100})
print(person)

#Pop (Remove elements using a key)
person.pop('calle')
print(person)

#Copy dictionaries
nuevo = person.copy()
print(nuevo)


