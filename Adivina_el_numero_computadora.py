import random


print("===========================================================================================")
print("                            ¡Bienvenid(a) al juego! ")
print("===========================================================================================")
print(" Selecciona un rango determinados de números para que la computadora intente adivinarlo")
print(" por ejemplo de 5 a 10, donde el rango menor es 5 y el rango mayor es 10.")
print("===========================================================================================")
print("                                ¡Buena Suerte!")
print("===========================================================================================")

print("-----------------------------------------------------------------------")
limite_minimo = int(input(" Por favor ingresa el número de rango menor: "))
print("---------------------------------------------------------------------")
limite_maximo = int(input("Por favor ingrese el número de rango mayor: "))
print("-----------------------------------------------------------------------")
1

respuesta = ""
while respuesta != "c":

    if limite_minimo != limite_maximo:
        prediccion = random.randint(limite_minimo, limite_maximo)
        
    else:
        prediccion = limite_minimo

    respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta ingresa (A). si es muy baja ingresa (B). Si es correcto ingresa (C): ").lower()
    
    if respuesta == "a":
        limite_maximo = prediccion - 1
    elif respuesta == "b":
        limite_minimo = prediccion + 1

print("===========================================================================================")    
print(          f"Si la computadora adivino tu numero correctamente: {prediccion} ")
print("===========================================================================================")