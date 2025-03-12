#Python core Concepts
    Python es un lenguaje interpretado, lo que significa que el codigo se ejecuta linea por linea.
    Python no es un lenguaje fuertemente tipado, los tipos de datos pueden cambiar dinamicamente. 
    Python obedece al paradigma duck typing, lo que significa que el codigo se ejecuta si cumple con la interfaz, no necesariamente el tipo de dato.
    Python no es un lenguaje puramente orientado a objetos sino mas bien multi-paradigma, sin embargo todo en python es un objeto. tales como las funciones de primera clase vrs la definicion estricta de clases
    Modulos vs Clases:
        los modulos son unidades de codigo independientes que pueden ser importados y utilizados en otros programas.
        las clases son unidades de codigo que definen un tipo de dato y sus propiedades y metodos.
    
    dir()
    globals()
    locals()    
    import types
    modules = [name for name in dir() if isinstance(eval(name), types.ModuleType)]
    print(modules)
        
    


    # Variables globales
x = 1
y = 2

def ejemplo():
    # Variables locales
    a = 3
    b = 4
    
    print("Dentro de la función:")
    print("\nlocals():")
    print(locals())  # Muestra solo a y b
    
    print("\nglobals():")
    print(globals())  # Muestra x, y, y la función ejemplo

# En el scope global
print("Fuera de la función:")
print("\nlocals():")
print(locals())  # En el scope global, locals() == globals()

print("\nglobals():")
print(globals())  # Muestra x, y, y la función ejemplo

ejemplo()

    
