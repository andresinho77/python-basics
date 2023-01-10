#Calculate IMC 
weight = int(input('How much do you weight: '))
height = float(input('what is your height: '))

def calculate_bmi(w , h):
    return w/(h*h)

print('Your BMI is: ',calculate_bmi(weight, height))


