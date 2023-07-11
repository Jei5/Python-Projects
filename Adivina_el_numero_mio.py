import random


def adivina_el_numero(vidas):
    print("=====================================")
    print("=====================================")
    print("     ¡Bienvenido(a) al juego!")
    print("=====================================")
    print("=====================================")
    print("-Tu meta es adivinar el número generado por la computadora, dependiendo del rango de números que elijas.")
    print("-Por ejemplo, adivinar un numero entre 5 y 10")
    print("-Donde el rango menor es 5 y el rango mayor es 10, todo depende del rango que elijas.")
    print("=====================================")
    print("          ¡Buena suerte!")
    print("=====================================")
    jugar_de_nuevo = True
    while jugar_de_nuevo:
        
        while True:
            try:
                x = int(input("Ingresa el rango de número menor: "))
                break
            except:
                print("¡Error! Ingresa un dígito.")

        while True:
            try:
                y = int(input("Ingresa el rango de número mayor: "))
                if x >= y:
                    print("Debe ingresar un valor mayor que el rango anterior.")
                else:
                    break
            except:
                print("¡Error! Ingresa un dígito.")
        
        print(f"El rango de números seleccionados es de {x} a {y}.")
        respuesta = input(f"Está bien el rango de números {x} a {y}?(si/no): ")
        while respuesta.lower() != "si":
            while True:
                respuesta_rango = input("¿Que rango desea modificar el menor o mayor?: ")
                if respuesta_rango.lower() == "menor":
                    while True:
                        try:
                            x = int(input("Ingresa el nuevo rango de número menor: "))
                            if x >= y:
                                print("Debe ingresar un valor menor que el rango mayor.")
                            else:
                                break
                        except:
                            print("¡Error! Ingresa un dígito.")
                    break
                elif respuesta_rango.lower() == "mayor":
                    while True:
                        try:
                            y = int(input("Ingresa el nuevo rango de número mayor: "))
                            if y <= x:
                                print("Debe ingresar un valor mayor que el rango menor.")
                            else:
                                break
                        except:
                            print("¡Error! Ingresa un dígito.")
                    break
                else:
                    print("Respuesta no válida. Por favor ingresa 'menor' o 'mayor'.")
                    continue

                print(f"El nuevo rango de números seleccionado es de {x} a {y}.")
            respuesta = input(f"¿Está bien el rango de números {x} a {y}? (si/no): ")
        
        numero_aleatorio = random.randint(x, y)
        vidas_restantes = vidas
        prediccion = 0
        
        while vidas_restantes > 0:
            try:
                prediccion = int(input(f"Adivina un número entre {x} y {y}: "))
            except:
                print("¡Error! Ingresa un dígito.")
                continue

            if prediccion < numero_aleatorio:
                print("Intenta otra vez. Este número es menor que el de la predicción.")
                vidas_restantes -= 1
                print(f"Te quedan {vidas_restantes} vidas.")
            elif prediccion > numero_aleatorio:
                print("Intenta otra vez. Este número es mayor que el de la predicción.")
                vidas_restantes -= 1
                print(f"Te quedan {vidas_restantes} vidas.")
            else:
                print(f"¡Felicitaciones! Adivinaste. El número de la predicción es {numero_aleatorio}!")
                break

        if vidas_restantes == 0:
            print(f"Se acabaron tus vidas. El número de la predición era {numero_aleatorio}.")

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

adivina_el_numero(3)