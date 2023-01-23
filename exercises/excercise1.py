#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

def calculate(num1, num2):
    res= int(num1)*int(num2)
    if(res > 1000):
        res = int(num1) + int(num2)
        print('The result is ', res)
    else:
        print('The result is ', res)

#Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

def sum_iteration(i):
    x=0
    for l in range(i):        
        sum=x+l
        print('Current Number', l, 'Previous Number', x, 'sum:', sum)
        x=l

#print('********************')
#num1=input('Insert numero 1: ')
#num2=input('Insert numero 2: ')
#calculate(num1, num2)

i=input('Insert numero de iteraciones:')
sum_iteration(int(i))


