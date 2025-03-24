# Virtual Environment + Lint Setup
La importancia de tener un entorno virtual para el desarrollo de software es fundamental, para evitar problemas de compatibilidad entre versiones de python y paquetes. adicionalmente, permite aislar el proyecto de dependencias externas y tener un ambiente controlado y reproducible entre programadores y los entornos de desarrollo,staging y producción.

Los scripts de setup estan pensados para ser ejecutados en un sistema linux o windows, ya sea en una maquina local o en un servidor de desarrollo.
tomar encueta que el entorno de staging, y producciòn puede ser generado usando hermientas tales como docker, kubernetes, etc.

para generar estos ambientes es recomendado tener conceptos solidos de CI/CD y  utilizar herramientas github actions, gitlab ci, etc. o herramientas de orquestacion de contenedores como docker, kubernetes, etc.

## linter


Un linter es una herramienta que analiza el codigo fuente de un programa para detectar errores y posibles mejoras. entre funciones, un linter puede identificar:

- Errores de sintaxis
- Errores de estilo
- Errores de seguridad
- Errores de rendimiento
- Errores de diseño

entre los linter mas populares se encuentran:

- pylint (https://www.pylint.org/)
- flake8 (https://flake8.pycqa.org/)
- black (https://black.readthedocs.io/en/stable/)

Por ejemplo, en nuestro programa queremos no limitar la longitud de las lineas de codigo, para ello podemos en flake8, la siguiente configuracion:
esta configuración se puede agregar al archivo .flake8 en el root del proyecto.

```python
flake8:
    max-line-length: 120
```
para el caso de black, se puede agregar la siguiente configuracion al archivo pyproject.toml en el root del proyecto.

```python
[tool.black]
line-length = 120
```

# ./Enviroments
En este folder encontrara 3 folder conrespondientes a la configuracion de entornos virtuales

En cada folder encontrará el setup con archivos BAT o SH a utilizar para crear el entorno virtual tomar encuenta que estos folders contiene archivos de setup.py y tox.ini que deben colocarse en el root   
```python
./venv_base
./venv_lint
./venv_lint_precommit
```
 

#lint
Tomar encuenta que en setup.py se estan instalando las dependencias de flake8, a continuacion encontrar un listado de posibles
plugins con los que puede agregar al proceso de linter
``` 
pip install flake8-docstrings
pip install flake8-annotations 


[mypy]
strict = True
disallow_untyped_defs = True
check_untyped_defs = True
```

Para typing es necesario agregar las librerias adicionales y sus validadores , a continaure encontrara los pip install asociacdos y un config de ejemplo
```
pip install mypy 
pip install pytype
```

setup.cfg
```
[flake8]
max-line-length = 88
extend-ignore = E203
select = ANN  # Habilitar checks de anotaciones

[mypy]
strict = True
disallow_untyped_defs = True
check_untyped_defs = True

[pytype]
inputs = src/
python_version = 3.9
```

## Linux

```bash
./enviroments/venv_base/linux_setup.sh
./enviroments/venv_lint/linux_setup.sh
./enviroments/venv_lint_precommit/linux_setup.sh
```

## Windows

```batch
./enviroments/venv_base/win_setup.bat
./enviroments/venv_lint/win_setup.bat
./enviroments/venv_lint_precommit/win_setup.bat
```

Nota: cada setup executa la instrucción de instalación dependiendo de su entorno
por ejemplo:
```
pip install -e ".[dev,lint,test]"
```
