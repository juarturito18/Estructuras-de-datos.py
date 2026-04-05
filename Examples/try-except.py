class DivisionByTwo(Exception):
    """
    No dividas entre dos
    """

try:
    a = int(input("Insert a number: "))
    b = int(input("Insert a second number: "))
#Se puede usar el exception con el fin de controlar cualquier error, pero tambien se puede especificar el tipo de error
except Exception:
    print("Please enter a number")

if b == 2:
    raise DivisionByTwo("No puedes divir entre dos")

result = None

try:
    result = a / b
    print(f"result: {result}")
#Es una buena practica especificar que el error que puede ocurrir  y de esta forma que sea mas facil de depurar
except ZeroDivisionError as e:
    print(f"Error by: {e}")
#El finally se usa para poder realizar una seccion de codigo independientemente de si existe un error o no
finally:
    print("Thanks for using my code")