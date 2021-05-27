# Módulo calculadora muy básico en Python con TDD

Este módulo Python constituye una calculadora muy básica que realiza las
operaciones de suma, resta, multiplicación, división y raíz cuadrada con
objeto de practicar el desarrollo dirigido por pruebas.

## Requerimientos

- Python 3

## Ejecución de la pruebas

Pueden invocarse las pruebas directamente mediante:

~~~
$ python isa_calculator_test.py
~~~

## Jugar con el módulo

Puede probarse el módulo jugando con él, por ejemplo, desde el modo
interactivo (REPL) proporcionado por Python:

~~~
$ python

Python 3.9.5
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import isa_calculator
>>> isa_calculator.add(2, -3)
-1
>>> isa_calculator.sub(2, 3)
-1
>>> isa_calculator.mul(2, 3)
6
>>> isa_calculator.div(4, 2)
2.0
>>> isa_calculator.sqrt(2)
1.414213562373095
~~~
