def suma(a=10, b=1):
    sum = a + b * 30
    print('La suma es:',sum)

suma()


def add(b, *a):   
    fib = 0  
    for i in a:
        fib = fib + i * b
    print('La suma es: ',fib)

add(100, 2,3,4)

