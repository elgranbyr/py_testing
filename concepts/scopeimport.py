x = 1
y = 2


def ejemplo():
    pass


print("****Fuera de la función:*****")
print("\ndir():")
print(dir())  # En el scope global, locals() == globals()


print("\nlocals():")
print(locals())  # En el scope global, locals() == globals()

print("\nglobals():")
print(globals())  # Muestra x, y, y la función ejemplo
