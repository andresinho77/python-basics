# #User adds number into a list
# print('Adding values to the list')
# numero = 1
# lista = []

# num=input('cuantos numeros desea ingresas: ')

# for i in range(int(num)):
#     print('Add the number of the list ',i+1,':')
#     numero=input()
#     lista.append(str(numero))

# print(lista)


# for i in range(10):
#     if i == 5:
#         break
#     else:
#         print(i)
# else:
#     print("Here")

# numbers = range(2, 12)
# new_dict=[]
# {new_dict.append(n//2) for n in numbers if n%3==0}
# print (new_dict)

# sum_1 = lambda a, b: (a**3) // (b**2)
# sum_2 = sum_1(5, 3)
# print(sum_2)

n = 3
print(sum(x*2 for x in range(1, n+1, 2)))