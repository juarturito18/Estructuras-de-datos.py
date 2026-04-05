"""Typing con python"""

variable = 42 #Int
print(f"Variable {variable}, del tipo {type(variable)}")

variable = "Texto de prueba" #Int
print(f"Variable {variable}, del tipo {type(variable)}")

#De esta forma se tipa una variable para que dentro del editor lo use de forma se va a usar 
user_id : int = 0
print(type(user_id))

#De esta forma se estamos tipando la funcion '->' y diciendo cula va a ser el posibel resultado 
def suma_clara(a:int,b:int) -> int:
    return a + b

#De esta forma estamos tipando valores que esten aniados como listas en diccionarios o int en tuplas
Articles: list [dict] = [{"Tittle 1":"Example 1"},{"Tittle 2":"Example 2"}]