#EXCERCISE 1
#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

def calculate(num1, num2):
    res= int(num1)*int(num2)
    if(res > 1000):
        res = int(num1) + int(num2)
        print('The result is ', res)
    else:
        print('The result is ', res)

#print('********************')
#num1=input('Insert numero 1: ')
#num2=input('Insert numero 2: ')
#calculate(num1, num2)

#------------------*****--------------------*****------------------*****--------------------
#EXCERCISE 2
#Write a script to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

def sum_iteration(i):
    x=0
    for l in range(i):        
        sum=x+l
        print('Current Number', l, 'Previous Number', x, 'sum:', sum)
        x=l

# i=input('Insert numero de iteraciones:')
# sum_iteration(int(i))

#------------------*****--------------------*****------------------*****--------------------
#EXCERCISE 3
#Write a program to accept a string from the user and display characters that are present at an even index number.
def even_characters(word):
    fin=int(len(word))
    for i in range(fin):
        if(i%2 == 0):
            print('Character in position:', word[i])

def even_characters2(word):
    x = list(word)
    for i in x[0::2]:
        print(i)
# palabra=input('Input the word:')
# even_characters2(palabra)

#------------------*****--------------------*****------------------*****--------------------
#EXERCISE 4
#Write a program to remove characters from a string starting from zero up to n and return a new string.
def remove_first_characters(word, num):
    print('The word', word,':', word[num:])

# palabra=input('Input the word:')
# num=int(input('Input the number: '))
# remove_first_characters(palabra,num)

#------------------*****--------------------*****------------------*****--------------------
#EXCERCISE 5
#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

num_x=[30,40,30]
num_y=[45,50,11]
num_z=[45,50,11,213,123,213,123,123,123,12,312,3,123,123,12,31,23,123,1,23,12,45]

def check_first_last(list):
   if(list[0]==list[-1]):
        print('True')
   else:
        print('False')

# check_first_last(num_x)
# check_first_last(num_y)
# check_first_last(num_z)

#EXCERCISE 6
#Write a program to find how many times substring “Emma” appears in the given string.

# string_x='Hola, soy andres y quiero ser andres el resto de andres, no importa cuantas veces diga andres'
# print(string_x.count('andres'))

#------------------*****--------------------*****------------------*****--------------------
#EXCERCISE 7
#Print the following pattern
# 1
# 2 2
# 3 3 3
row = 12

def print_pattern_7(i):
    for j in range(i):
        print(i, end=' ')
    print('')

# for i in range(row):
#     print_pattern_7(i)

#------------------*****--------------------*****------------------*****--------------------
#EXCERCISE 8
#Print the following pattern
# 1
# 1 2
# 1 2 3
def print_pattern(i):
    for j in range(1, i+1):
        print(j, end=' ')
    print('')

# for i in range(1,row + 1):
#     print_pattern(i)

#------------------*****--------------------*****------------------*****--------------------
#EXCERCISE 9
#Write a program to check if the given number is a palindrome number.

# def palindrom(number):
#     if(str(number) == str(number)[::-1]):
#         print('Palindrome')
# number = 744912335533219447
# # print(list(number))
# # print(str(number)[::-1])
# palindrom(number)


#EXCERCISE 10
# Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
list1 = [10, 20, 25, 30, 35,20,15,23,91,34,123]
list2 = [40, 45, 60, 75, 90,100,200]

def new_list(list1, list2):
    new_list = []
    # size = len(list1) + len(list2)
    
    for j in range(len(list1)):
        if(list1[j]%2==1):
            new_list.append(list1[j])
   
    for i in range(len(list2)):
        if(list2[i]%2==0):
            new_list.append(list2[i])
    print(new_list)
# new_list(list1,list2)

#EXCERCISE 10
#Print multiplication table form 1 to 10


def ten_times_table():

    for i in range(1,11):
        print('Number:',i , end=' ')
        for j in range(1,11):
            print(j*i, end=' ')
        print('')
ten_times_table()


