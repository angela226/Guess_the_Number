import random


def adivina_el_mumero(X):
    print("******************************************************************")
    print('========================Bienvenido================================')
    print("******************************************************************")
    print("La meta es Adivinar el numero generado por la computadora")

    numero_aleatorio = random.randint(1, X) #Numero aleatorio entre 1 y X.

    prediccion = 0

    while prediccion != numero_aleatorio:
        #El usuario ingresa un numero
        prediccion = input(f"Adivina el numero entre 1  y {X}: ") # f-string 

        if prediccion < numero_aleatorio:
            print("Primer intento. Es muy pequeño el numero")
        
        elif prediccion > numero_aleatorio:
            print("Segundo ineto. Es muy grande el numero")

    print(f"FELICITACIONES! Lo lograste {numero_aleatorio} correctamente")


adivina_el_mumero(10)