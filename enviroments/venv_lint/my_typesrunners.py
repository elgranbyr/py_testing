from my_types import *

print("suma(1, 2): ",suma(1, 2))
print("suma_float(1.2, 25): ",suma_float(1.2, 25))
print("suma_class(c_suma(1, 2)): ",suma_class_callable(c_suma(1, 2)))
print("suma_class_callable(c_suma(1, 2)): ",suma_class_callable(c_suma(1, 2)))
print("suma_classany(c_suma(5, 7)): ",suma_classany(c_suma(5, 7)))
print("suma_class_varios_tipos(c_suma(8, 7)): ",suma_class_varios_tipos(c_suma(8, 7)))
print("suma_typevar(1, 2): ",suma_typevar(1, 2))
print("suma_typevar(1.2, 25): ",suma_typevar(1.2, 25))
print("suma_typevar(c_suma(1, 2), c_suma(3, 4)): ",suma_typevar(c_suma(1, 2), c_suma(3, 4)))
print("suma_list([1, 2, 3, 4, 5]): ",suma_list([1, 2, 3, 4, 5]))
print("suma_dict({'a': 1, 'b': 2, 'c': 3}): ",suma_dict({'a': 1, 'b': 2, 'c': 3}))