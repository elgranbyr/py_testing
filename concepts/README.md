#Python core Concepts

## Python es un lenguaje interpretado, lo que significa que el codigo se ejecuta linea por linea(incluye los imports)

    import interpretado
    print("Tercera línea en interpretadoimport.py")

[Ejemplo Interpretado ](./interpretado.py)

[Ejemplo Import ](./interpretadoimport.py)

## Python no es un lenguaje fuertemente tipado, los tipos de datos pueden cambiar dinamicamente. 

    numero = 10
    print(f"\nNúmero inicial: {numero} (tipo: {type(numero)})")
    numero = "string" 
    print(f"\ncadena: {numero} (tipo: {type(numero)})")
    
[Ejemplo Tipado ](./tipado.py)

## Python obedece al paradigma duck typing, lo que significa que el codigo se ejecuta si cumple con la interfaz, no necesariamente el tipo de dato.

[Ejemplo Docktype ](./ducktype.py)

## Python no es un lenguaje puramente orientado a objetos sino mas bien multi-paradigma, sin embargo todo en python es un objeto.
[Ejemplo Docktype ](./objects.py)

 
## Modulos vs Clases:
    los modulos son unidades de codigo independientes que pueden ser importados y utilizados en otros programas.
    las clases son unidades de codigo que definen un tipo de dato y sus propiedades y metodos.
    
    dir()
    globals()
    locals()    

[Ejemplo Scope ](./scope.py)

[Ejemplo Scope Imports ](./scopeimport.py)


## Idempotencia:
Una funcion es idempotente si el resultado de la funcion es el mismo independientemente de cuantas veces se ejecute.

    Ejemplo:
        def suma(a,b):
            return a+b
        print(suma(1,2))
        print(suma(1,2))
        print(suma(1,2))
    
[Ejemplo Idempotencia ](./idempotencia.py)

    
