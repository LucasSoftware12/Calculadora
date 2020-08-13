inicio = True


def ingreso():
    global a, b
    a = int(input("Ingrese el primer numero \n"))
    b = int(input("Ingrese el segundo numero \n"))


def suma():
    print(f"El resultado de la suma es: ", a+b)


def resta():
    print(f"El resultado de la resta es: ", a-b)


def multiplicacion():
    print(f"El resultado de la multiplicacion es: ", a*b)


def division():

    if (b == 0):
        print("No se puede dividir en 0")

    else:
        print("El resultado de la division es: ", a/b)


while inicio:
    print("\nCalculadora"
          "\n1 Suma"
          "\n2 Resta"
          "\n3 Multiplicacion"
          "\n4 Division"
          "\n")

    opcion = int(input("Ingrese opcion\n"))
    if opcion == 1:
        ingreso()
        suma()

    if opcion == 2:
        ingreso()
        resta()

    if opcion == 3:
        ingreso()
        multiplicacion()

    if opcion == 4:
        ingreso()
        division()
    seguimos = int(input('\nSeguimos''\n1= Si''\n0= No''\n'))
    if seguimos == 0:
        inicio = False
