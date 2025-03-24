
# Variables globales
x = 1
y = 2

print("****Fuera de la función:*****")
print("\nlocals():")
print(locals())  # En el scope global, locals() == globals()

print("\nglobals():")
print(globals())  # Muestra x, y, y la función ejemplo


def ejemplo():
    # Variables locales
    a = 3
    b = 4
    print("***** Dentro de la función:**********")
    print("\nlocals():")
    print(locals())  # Muestra solo a y b

    print("\nglobals():")
    print(globals())  # Muestra x, y, y la función ejemplo

    # En el scope global


ejemplo()


print("***** despues de la funcion:**********")

print("\nlocals() <-> Global():")
print(locals())  # Muestra x, y, y la función ejemplo
print(globals())  # Muestra x, y, y la función ejemplo
