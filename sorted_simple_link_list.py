class Nodo:
    def __init__(self, data):
        self.data = data
        self.link = None

class Sorted_link_list:
    head_lista = None
    
    @classmethod
    def add_data(cls, new_data):
        if cls.head_lista is None:
            cls.head_lista = Nodo(new_data)
        else:
            new_nodo = Nodo(new_data)
            actual_nodo = cls.head_lista
            while actual_nodo.link is not None:
                actual_nodo= actual_nodo.link
            actual_nodo.link = new_nodo
    
    @classmethod
    def __str__(cls):
        result = ""
        nodo_actual = cls.head_lista
        while nodo_actual is not None:
            result += str(f"{nodo_actual.data} -> ")
            nodo_actual = nodo_actual.link
        return result + "None"
