class obj:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}                                                                                             , Age: {self.age}"

    def mystaticfunction(namefile):
        pass




    def set_name(self, name):
        self.name = name






    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    # Mal: Este método no usa 'self', debería ser estático
    def sum_numbers(self, x, y):
        return x + y

    # Mal: Este método no usa 'self', debería ser estático
    def multiply_numbers(self, x, y):
        return x * y














