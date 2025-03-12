# Virtual Environment Setup
La importancia de tener un entorno virtual para el desarrollo de software es fundamental, para evitar problemas de compatibilidad entre versiones de python y paquetes. adicionalmente, permite aislar el proyecto de dependencias externas y tener un ambiente controlado y reproducible entre programadores y los entornos de desarrollo,staging y producción.

Los scripts de setup estan pensados para ser ejecutados en un sistema linux o windows, ya sea en una maquina local o en un servidor de desarrollo.
tomar encueta que el entorno de staging, y producciòn puede ser generado usando hermientas tales como docker, kubernetes, etc.

para generar estos ambientes es recomendado tener conceptos solidos de CI/CD y  utilizar herramientas github actions, gitlab ci, etc. o herramientas de orquestacion de contenedores como docker, kubernetes, etc.


## Linux

```bash
./scripts/venv_base/linux_setup.sh
```

## Windows

```batch
./scripts/venv/win_setup.bat
```
