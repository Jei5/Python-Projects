import random

num1=random.randint(99, 999)
num2=random.randint(99, 999)
num3=(num1+num2)

print(num1)
print("+")
print(num2)
print("____")

while True:
    try:
        respuesta=int(input("¿cuanto da esta suma?: "))
        break
    except:
        print("Error ingrese un digito")
if respuesta==num3:
    print("¡Felicitaciones es correcto!")
elif respuesta!=num3:
    print("¡incorrecto!, la respuesta es:",num3)
print("fin del programa")

    