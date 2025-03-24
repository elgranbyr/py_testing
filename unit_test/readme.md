# Existen tres tipos de tests:

- Unit tests: Prueban una unidad del código por sí sola.
- Integration tests: Prueban la interacción entre compoentes.
- End-to-end tests (o tests funcionales): Prueban la interacción entre múltiples unidades y el funcionamiento completo del sistema desde la perspectiva del usuario final.

## Core Concepts de Pytest

Pytest es un framework de testing para Python que se basa en los siguientes conceptos fundamentales:

1. **Assertions simples**: Utiliza el statement `assert` de Python para realizar verificaciones, sin necesidad de recordar métodos específicos de testing.


2. **Fixtures**: Mecanismo para proporcionar datos o estados base que tus tests necesitan. Las fixtures pueden ser reutilizadas entre tests y se definen usando el decorador `@pytest.fixture`.

3. **Marcadores (Markers)**: Permiten categorizar tests y ejecutarlos selectivamente. Por ejemplo: `@pytest.mark.slow` para tests lentos.

4. **Parametrización**: Permite ejecutar el mismo test con diferentes conjuntos de datos usando `@pytest.mark.parametrize`.



### Assertions en Pytest

Pytest proporciona múltiples formas de realizar assertions:

1. **Assertions básicas**:
   - `assert x == y`: Verifica igualdad
   - `assert x != y`: Verifica desigualdad
   - `assert x`: Verifica que x es True
   - `assert not x`: Verifica que x es False

2. **Comparaciones**:
   - `assert x > y`: Mayor que
   - `assert x >= y`: Mayor o igual que
   - `assert x < y`: Menor que
   - `assert x <= y`: Menor o igual que

3. **Colecciones**:
   - `assert x in y`: Verifica que x está en y
   - `assert x not in y`: Verifica que x no está en y
   - `assert len(x) == y`: Verifica longitud

4. **Excepciones**:
   ```python
   with pytest.raises(Exception):
       # Código que debería lanzar una excepción
   ```

5. **Aproximaciones** (útil para números flotantes):
   ```python
   assert pytest.approx(0.1 + 0.2) == 0.3
   ```

6. **Coincidencia de patrones**:
   - `assert str(excinfo.value).startswith("mensaje")`
   - `assert re.match(pattern, string)`



### Fixtures en Pytest

Las fixtures son una de las características personalizadas de pytest. Basicamente son funciones que proporcionan datos o estado inicial para tus tests.



1. **Definición básica**:
   ```python
   import pytest

   @pytest.fixture
   def mi_fixture():
       return "datos de prueba"

   def test_ejemplo(mi_fixture):
       assert mi_fixture == "datos de prueba"
   ```

2. **Alcance (Scope)**:
   Las fixtures pueden tener diferentes alcances usando el parámetro `scope`:
   ```python
   @pytest.fixture(scope="function")  # Por defecto, se ejecuta para cada test
   @pytest.fixture(scope="class")     # Una vez por clase
   @pytest.fixture(scope="module")    # Una vez por módulo
   @pytest.fixture(scope="session")   # Una vez por sesión de testing
   ```

3. **Fixtures con setup y teardown**:

El **teardown** es la fase de limpieza que se ejecuta después de que un test ha finalizado. Es crucial para:
- Limpiar datos temporales
- Cerrar conexiones
- Liberar recursos
- Restaurar el estado inicial del sistema etc

   ```python
   @pytest.fixture
   def conexion_db():
       # Setup
       db = crear_conexion()
       yield db  # Proporciona la conexión al test
       # Teardown
       db.cerrar()
   ```

4. **Fixtures parametrizadas**:
   ```python
   @pytest.fixture(params=['mysql', 'postgresql', 'sqlite'])
   def base_datos(request):
       return request.param
   ```

5. **Fixtures anidadas**:
   ```python
   @pytest.fixture
   def usuario(conexion_db):
       return conexion_db.crear_usuario()
   ```
#instalación de pytest

```bash
# Instalación básica de pytest
pip install pytest

# Para verificar la instalación y versión
pytest --version
```

### Paquetes Adicionales Recomendados
```bash
# Para generar reportes HTML
pip install pytest-html

# Para ejecutar tests en paralelo
pip install pytest-xdist

# Para medir cobertura de código
pip install pytest-cov

# Para tests asíncronos
pip install pytest-asyncio

# Para mock de objetos
pip install pytest-mock
```

### Estructura Recomendada de Proyecto
```
mi_proyecto/
│
├── src/
│   └── mi_codigo.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Fixtures compartidas
│   ├── test_feature1.py
│   └── test_feature2.py
│
└── pytest.ini              # Configuración de pytest
```