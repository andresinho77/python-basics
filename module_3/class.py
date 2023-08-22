#Class
class Persona:
    #Constructor
    def __init__(self, peso, estatura, nombre):
        self.nombre = nombre
        self.peso = peso
        self.estatura = estatura

    def calcularIMC(self):
        imc = self.peso / (self.estatura**2)
        return imc

#class inheretance 
class Estado_peso(Persona):
    def estado_peso(self):
        imc = self.calcularIMC()

        if (imc < 18.5):
            estadoPeso = "Peso Bajo"
        elif (imc > 18.5 and imc < 29.9):
            estadoPeso = "Peso Normal"
        else:
            estadoPeso = "Sobre peso"
            
        return estadoPeso        


#Instance of a class (Creating an object)
obj = Estado_peso(70,1.74,'Pepito')
print(obj.nombre)
print(obj.estado_peso())




