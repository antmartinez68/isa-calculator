"""Módulo calculadora muy básico"""


def add(a, b):
    """Sumar dos valores"""
    return a + b


def sub(a, b):
    """Restar a un valor otro"""
    return a - b


def mul(a, b):
    """Multiplicar dos valores"""
    return a * b


def div(a, b):
    """Dividir un valor entre otro"""
    return a / b


def sqrt(a):
    """Obtener raiz cuadrada de un valor por el método babilónico"""
    if a < 0:
        raise ArithmeticError(f"No hay solución real para la raíz cuadrada de {a}")
    x = div(a, 2)
    # Iterar hasta conseguir la máxima precisión permitida
    # por el tipo float de python
    while True:
        if mul(x, x) == a:
            return x
        else:
            last_x = x
            x = div(add(x, div(a, x)), 2)  # Más claro: (x + (a / x)) / 2
            if x == last_x:
                # Se detecta que se ha alcanzado la máxima precisión que
                # podemos conseguir cuando el resultado en dos
                # interaciones consecutivas es el mismo
                break
    return x
