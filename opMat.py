""" 
un programa con las operaciones basicas y complejas de aritmetica
// hay tipos de datos int para numero enteros y float para decimales
"""
# Definir las variables 
num1 = float( input("Ingrese un numero: "))
num2 = float (input ("Ingrese el otro numero: "))

#sumar

suma = num1 + num2

# resta
resta = num1 - num2

# multiplicacion
multiplicacion = num1 * num2

# division

if num2 != 0:
    division = num1 / num2
    divisionModular = num1 % num2
    print(f"el resulltado de la division es: '{division}'")
    print(f"el resultado de la divison modular es: '{divisionModular}'")

else:
    print("ERROR! No se puede dividir entre cero")
    print("ERROR! No hay modulo si se divide por cero ")
#potencia
potencia = num1 ** num2 #com validar cuado la base o el exponente es cero
if num1 == 0 :
    potencia = 0
else:
    potencia = num1 ** num2
    print(f"el resulltado de la potencia es: '{potencia}'")

# radicacion
if num2 == 0:
    radicacion = 1
    print(f"el resulltado de la radicacion es: '{radicacion}'")
elif num2 > 0:
    radicacion = num1 ** (1/num2)
    print(f"el resulltado de la radicacion es: '{round(radicacion, 2)}'")
else:
    print("no existe resultado de radicacion con elevacion de numero negativo")
    
#print("el resultado de la suma ", suma)
print(f"el resulltado de la suma es: '{suma}'")
print(f"el resulltado de la resta es: '{resta}'")
print(f"el resulltado de la multiplicacion es: '{multiplicacion}'")

 #investigar como formatear decimales

