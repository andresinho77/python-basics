#it is not required to keep the order using "SET" unlike lists

#Sets
frutas={'Perro','Gato','Mosquito','Mate','Pollo'}
numero={1,23,123,4,57,887,877}
print(frutas)

#Add new values 
frutas.add('Burro')
print(frutas)


#Join two Sets
frutas_verdes = {'Peras','Manzanas', 'Platano', 'Cerezas'}
frutas_rojas = {'Fresas', 'Manzanas', 'Cerezas'}


#Using Union
frutas_r = frutas_rojas.union(frutas_verdes)
print('Union',frutas_r)

#Update and 
frutas_verdes.update(frutas_rojas)

print('Verdes',frutas_verdes)

#Remove Elements from Sets (Dictionaries)
frutas_verdes.remove('Fresas')
print(frutas_verdes)

#remove the fisrt element of Set
frutas_verdes.pop()
print(frutas_verdes)

#Clear all the Set makes it empty
frutas_verdes.clear()
print(frutas_verdes)