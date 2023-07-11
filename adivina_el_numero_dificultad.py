import random

print("=====================================")
print("=====================================")
print("     ¡Bienvenido(a) al juego!")
print("=====================================")
print("=====================================")
print("-Tu meta es adivinar el número generado por la computadora, dependiendo de la dificultad que eligas.")
print("-Por ejemplo, adivinar un numero entre 1 y 10")
print("-Donde dentro de ese rango se generara un numero aleatorio el cual tendras que adivinar, pero todo depende de la dificultad que eligas")
print("=====================================")
print("          ¡Buena suerte!")
print("=====================================")
    
rango_menor = 0
rango_mayor = 0
prediccion = 0
    

jugar_de_nuevo = True
while jugar_de_nuevo:
    nivel_valido = False
    while not nivel_valido:
            print("==================================================")
            print("Selecciona un nivel de dificultad a continuacion: ")
            print("==================================================")
            print("------------------------------------")
            print("facil: 3 vidas, rango de 1 a 10.")
            print("------------------------------------")
            print("Medio: 3 vidas, rango de 1 a 25.")
            print("------------------------------------")
            print("Dificil: 4 vidas, rango de 1 a 50.")
            print("==================================================")
            print("==================================================")
            nivel = input("¿Que dificultad eliges?: ")
            print("==================================================")
            
            if nivel.lower() == "facil":
                    vidas = 3
                    rango_menor = 1
                    rango_mayor = 10
                    nivel_valido = True
            elif nivel.lower() == "medio":
                    vidas = 3
                    rango_menor = 1
                    rango_mayor = 25
                    nivel_valido = True
            elif nivel.lower() == "dificil":
                    vidas = 4
                    rango_menor = 1
                    rango_mayor = 50
                    nivel_valido = True

            else:
                    print("=================================")
                    print("No seleccionaste un nivel válido.")
                    print("=================================")
                    continue
                    
            
    numero_aleatorio = random.randint(rango_menor, rango_mayor)
    vidas_restantes = vidas

    while vidas_restantes > 0:
        try:
            prediccion = int(input(f"Adivina un número entre {rango_menor} y {rango_mayor}: "))
        except:
            print("==========================")
            print("¡Error! Ingresa un dígito.")
            print("==========================")
            continue

        if prediccion < numero_aleatorio:
            print("================================================================")
            print("Intenta otra vez. Este número es menor que el de la predicción.")
            print("================================================================")
            vidas_restantes -= 1
            print("------------------------------------")
            print(f"Te quedan {vidas_restantes} vidas.")
            print("------------------------------------")

        elif prediccion > numero_aleatorio:
            print("================================================================")
            print("Intenta otra vez. Este número es mayor que el de la predicción.")
            print("================================================================")
            vidas_restantes -= 1

            print("------------------------------------")
            print(f"Te quedan {vidas_restantes} vidas.")
            print("------------------------------------")
        else:
            print("================================================================================")
            print(f"¡Felicitaciones! Adivinaste. El número de la predicción es {numero_aleatorio}!")
            print("================================================================================")
            break

    if vidas_restantes == 0:
        print("=========================================================================")
        print(f"Se acabaron tus vidas. El número de la predición era {numero_aleatorio}.")
        print("=========================================================================")
    while True:
        respuesta = input("¿Deseas jugar de nuevo? (si/no): ")
        if respuesta.lower() == "si":
            vidas_restantes = vidas
            break
        elif respuesta.lower() == "no":
            jugar_de_nuevo = False
            print("=====================================")
            print("=====================================")
            print("      Gracias por jugar.")
            print("=====================================")
            print("=====================================")
            print("      ¡Hasta la próxima!")
            print("=====================================")
            print("=====================================")
            break
        else:
            print("Respuesta no válida. Por favor ingresa 'si' o 'no'.")
            continue
