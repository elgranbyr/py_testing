from typing import Any, Union, TypeVar, Callable, List, Dict

class c_suma:
    def __init__(self, a: int, b: int) -> int:
        self.a = a
        self.b = b

    def __call__(self) -> int:
        return self.a + self.b 
    
    def __add__(self, other: 'c_suma') -> 'c_suma':
        return c_suma(self.a + other.a, self.b + other.b)   





def suma(a: int, b: int) -> int:
    return a + b

def suma_float(a: float, b: float) -> float:
    return a + b



def suma_class_callable(a: Callable) -> str:
    return a()

def suma_class(a: c_suma) -> str:
    return a()

def suma_classany(a: Any) -> str:
    return a()

def suma_class_varios_tipos(a: Union[any,c_suma]) -> str:
    return a()

T = TypeVar('T')
def suma_typevar(a: T, b: T) -> T:
    return a + b

def suma_list(a: List[int]) -> int:
    return sum(a)

def suma_dict(a: dict) -> int:
    if a is None:
        raise ValueError("El diccionario no puede ser None")
    if not isinstance(a, dict):
        raise TypeError("El argumento debe ser un diccionario")
    if not a:  # si el diccionario está vacío
        raise ValueError("El diccionario no puede estar vacío")
    
    return sum(a.values())  



    
