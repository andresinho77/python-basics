def suma(a=10, b=1):
    sum = a + b * 30
    print('La suma es:',sum)

suma()


def add(b, *a):   
    fib = 0  
    for i in a:
        fib = fib + i * b
    print('La suma es: ',fib)

add(100,2,3,4)

def calculateIMC(est, peso):
    imc = peso / (est**2)
    return imc

def estadoPeso (imc):
    
    if (imc < 18.5):
        estadoPeso = "Peso Bajo"
    elif (imc > 18.5 and imc < 29.9):
        estadoPeso = "Peso Normal"
    else:
       estadoPeso = "Sobre peso"
    
    return estadoPeso

print('El IMC es igual a : ',estadoPeso(calculateIMC(1.74, 70)))

