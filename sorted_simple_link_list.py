class Nodo:
    def __init__(self, data):
        self.data = data
        self.link = None

class Sorted_link_list:
    def __init__(self):
        self.head_lista = None
    
    def add_data(self, new_data):
        if self.head_lista is None:
            self.head_lista = Nodo(new_data)
        else:
            new_nodo = Nodo(new_data)
            actual_nodo = self.head_lista
            while actual_nodo.link is not None:
                actual_nodo= actual_nodo.link
            actual_nodo.link = new_nodo

    def sort_data(self):
        if self.head_lista is None or self.head_lista.link is None:
            return "La lista es la misma"
        
        swap = True
        while swap:
            swap = False
            actual_nodo = self.head_lista
            while actual_nodo.link is not None:
                try:
                    if actual_nodo.data > actual_nodo.link.data:
                        actual_nodo.data, actual_nodo.link.data = actual_nodo.link.data, actual_nodo.data
                        swap = True
                except TypeError:
                    print( "Por favor ingresa solo valores de un mismo tipo")
                    return 
                actual_nodo = actual_nodo.link

    def __str__(self):
        result = ""
        nodo_actual = self.head_lista
        while nodo_actual is not None:
            result += str(f"{nodo_actual.data} -> ")
            nodo_actual = nodo_actual.link
        return result + "None"
