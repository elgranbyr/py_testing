import unittest
import pytest
from enviroments.venv_lint.my_types import suma_dict,suma_float

class TestExample(unittest.TestCase):
    def setUp(self):
        """
        Este método se ejecuta antes de cada test
        """
        self.test_data = {
            "name": 15,
            "value": 42
        }

    def test_suma(self):
        result = suma_dict(self.test_data)
        self.assertEqual(result, 57)

    def test_raises(self):
        with pytest.raises(ValueError, match="El diccionario no puede ser None"):
            suma_dict(None)


    def test_type(self):
        with pytest.raises(TypeError, match="El argumento debe ser un diccionario"):
            suma_dict(1)

    def test_empty(self):
        with pytest.raises(ValueError, match="El diccionario no puede estar vacío"):
            suma_dict({})

    def test_cualquier_exception(self):
        with pytest.raises(Exception):
            suma_dict(None)

    @unittest.skip("Test temporal deshabilitado")
    def test_future_feature(self):
        """
        Test para una función que aún no está implementada
        """
        pass

if __name__ == '__main__':
    unittest.main() 