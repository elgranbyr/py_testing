def test_sample_data_structure(sample_data):
    """
    Prueba que verifica la estructura del fixture sample_data
    """
    assert isinstance(sample_data, dict)
    assert "name" in sample_data
    assert "value" in sample_data


def test_sample_data_values(sample_data):
    """
    Prueba que verifica los valores del fixture sample_data
    """
    assert sample_data["name"] == 5
    assert sample_data["value"] == 5


def test_sample_data_types(sample_data):
    """
    Prueba que verifica los tipos de datos en sample_data
    """
    assert isinstance(sample_data["name"], int)
    assert isinstance(sample_data["value"], int)


def test_sample_data_modification(sample_data):
    """
    Prueba que verifica que podemos modificar los datos del fixture
    """
    sample_data["name"] = 10
    assert sample_data["name"] == 10
    # El cambio no debe afectar a otras pruebas debido a que pytest
    # crea una nueva instancia del fixture para cada test
