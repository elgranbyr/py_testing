class Pato:
    def hablar(self):
        return "¡Cuac!"


class Perro:

    def hablar(self):
        return "¡Guau!"


class Gato:
    def hablar(self):
        return "¡Miau!"


class Humano:
    def platicar(self):
        return "Hola Mundo!"


class ProtoCallable:
    def __init__(self):
        self.hablar = lambda : "Hola callable!"

    def __call__(self):
        return self.hablar()


def hacer_hablar(animal):
    print(animal.hablar())


hacer_hablar(Pato())
hacer_hablar(Perro())
hacer_hablar(Gato())
h = Humano()
h.hablar = lambda : h.platicar()
hacer_hablar(h)
