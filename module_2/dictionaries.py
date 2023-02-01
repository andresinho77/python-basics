person = {'name': 'Pepito', 'lastname':'Perez', 'age':35}

print(person['name'])
print(person.get('name'))

#Add Values:
person['calle']=100

print(person)

#Update Values:
person['calle']='Calle 100'
print(person)