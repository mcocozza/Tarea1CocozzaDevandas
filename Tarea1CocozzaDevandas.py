import math
# ERR3 -1.5 Repitieron condicion de error


def multiple_op(n):

    # Este método toma el parametro de entrada y determina
    # si el numero es positivo y entero
    # En caso de no cumplirse, devuelve un codigo de error
    # 22.
    # Si es positivo y entero, rellena un array con las
    # siguientes operaciones en orden: X*X, 2^X, X!.

    b = []
    if type(n) == int and n >= 0:  # chequeo de parametros

        X = n  # operaciones para el array
        b.append(X*X)
        b.append(2**X)
        b.append(math.factorial(X))

        return b
    else:
        return 22  # codigo de error argumento invalido


def verify_array_op(n):
    # Este método toma el parametro de entrada y determina
    # si el array de entrada son solamente numeros enteros
    # positivos.
    # En caso de no cumplirse, devuelve un codigo de error
    # 22.
    # Para miembro del array se utiliza el metodo:multiple_op

    a = []
    for i in n:
        if type(i) == int and i >= 0:  # chequeo de parametros

            a.append(multiple_op(i))

        else:
            return 22  # codigo de error argumento invalido

    return a
