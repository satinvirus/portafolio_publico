import time


#calculadora con opciones

def suma(x,y):
    return x+y

def resta(x,y):
    return x - y

def divicion(x,y):
    return x / y

def multiplicacion(x,y):
    return x * y

def operacion():
    print("Elije una operacion: ")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - divicion")
    print("4 - multiplicacion")

    elecion = input("Elije una opcion:")

    num1 = int(input("Primer numero a ingresar:"))
    num2 = int(input("Segundo numero a ingresar:"))


    if elecion == '1':
        print(num1," + ",num2, "=", suma(num1,num2))

    elif elecion == '2':
        print(num1, "-", num2, "=", resta(num1,num2))

    elif elecion == '3':
        print(num1, "/", num2, "=", divicion(num1,num2))

    elif elecion == '4':
        print(num1, "x", num2, "=", multiplicacion(num1,num2))

    elif elecion == '0':
        print("Hasta luego")


    else:
        print("Eleccion no valida")

################################################################################################


def operacion_auto():

    for i in range(1,6):

        print("Elije una operacion: ")
        print("1 - Suma")
        print("2 - Resta")
        print("3 - divicion")
        print("4 - multiplicacion")
        print("5 - Salir")


        elecion = int(input("Elije una opcion: "))
        print(" ")


        if elecion == 1:
            num1 = int(input("Primer numero a ingresar:"))
            num2 = int(input("Segundo numero a ingresar:"))
            print(" ")
            print(num1, " + ", num2, "=", suma(num1, num2))
            print(" ")

        elif elecion == 2:
            num1 = int(input("Primer numero a ingresar:"))
            num2 = int(input("Segundo numero a ingresar:"))
            print(" ")
            print(num1, "-", num2, "=", resta(num1, num2))
            print(" ")
        elif elecion == 3:
            num1 = int(input("Primer numero a ingresar:"))
            num2 = int(input("Segundo numero a ingresar:"))
            print(" ")
            print(num1, "/", num2, "=", divicion(num1, num2))
            print(" ")
        elif elecion == 4:
            num1 = int(input("Primer numero a ingresar:"))
            num2 = int(input("Segundo numero a ingresar:"))
            print(" ")
            print(num1, "x", num2, "=", multiplicacion(num1, num2))
            print(" ")
        elif elecion == 5:

            print(" ")
            print("!!Hasta luego!!")
            print(" ")
            break
        else:
            print(" ")
            print("Opcion no valida, vuelva a ingresar alguna opcion mostrada ")
            print(" ")

###############################################################################################

def guesshenumber():

    import random #se importa el modulo de random
    v = random.randint(1,3) # con esto podemos asignar los valores inferior y superior que se sin antes hacerlo entero

    print("Adivina el valor de la computadora")
    valor =int(input("Que numero esta pensando del 1 al 10: "))

    if v == valor:
        print("!!Felicidades tu y la computadora piensan igual!!!")
    else:
        print("Lo siento ese no era el valor el valor es: ", v ," a intentarlo")


#####################################################################################################################


def guesshenumber_auto():


    import random  # se importa el modulo de random
    v = random.randint(1, 10)  # con esto podemos asignar los valores inferior y superior que se sin antes hacerlo entero

    print("Adivina el valor de la computadora tienes 3 intentos")

    x = 3 #este indica cuantos intentos tienes

    while x > 0 : #este ciclo while va indicar si es que llega a 0 o menos para el ciclo

        x-=1 #este indicara una reduccion de 1 en 1 hasta que el ciclo while se termine


        valor = int(input("Que numero esta pensando del 1 al 10: "))

        if v == valor:
            print("!!Felicidades tu y la computadora piensan igual!!! Hasta luego :D")
            time.sleep(1)
            break
        else:
            print("Lo siento ese no era el valor el valor es: ", v, " a intentarlo")
    else:
        print("Tus intentos han finalizado")

###################################################################################################################

#operacion()

#operacion_auto()

#guesshenumber()

guesshenumber_auto()