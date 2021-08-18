import math
import random
# ERR8 -5
# ERR1x2 -3 Los casos negativos deben de pasar, no se esperaba test fallando
# ERR2x2 -5 Los casos positivos tenian que probar la respuesta no solo el
# codigo de error


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


def test_multiple_op_pos():

    # CASO POSITIVO
    # Prueba multiple_op con numeros enteros positivos
    # al azar
    # El assert espera que no haya error ya que se asume
    # que todos estos caracteres son numeros enteros
    # positivos.

    assert multiple_op(random.randint(0, 100)) != 22


def test_verify_array_op_pos():

    # CASO POSITIVO
    # Prueba verify_array_op con array de entrada de
    # tamaño fijo, con miembros aleatorios que sean
    # numeros enteros positivos.
    # El assert espera que no haya error ya que se asume
    # que todos estos caracteres son numeros enteros
    # positivos.

    g = []
    for i in range(0, 5):

        g.append(random.randint(0, 100))

    assert verify_array_op(g) != 22


def test_multiple_op_neg():

    # CASO NEGATIVO
    # Prueba multiple_op se verifica que al ingresar
    # un caracter inválido al azar, dé el error 22.
    # assert espera que no haya error

    g = [-1, "hola mundo", 2.5]

    assert multiple_op(g[random.randint(0, 2)]) != 22


def test_verify_array_op_neg():

    # CASO NEGATIVO
    # Prueba verify_array_op se verifica que al ingresar un
    # array con caracter inválido al azar, dé el error 22.
    # assert espera que no haya error

    g = [1, "hola mundo", 5]

    assert multiple_op(g) != 22
