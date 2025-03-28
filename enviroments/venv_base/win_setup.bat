@echo off
setlocal

:: Obtener el directorio actual y el directorio raíz del repositorio
set "CURR_DIR=%~dp0"
set "REPO_ROOT=%CURR_DIR%.."
set "VENV_DIR=%REPO_ROOT%\venv"

:: Eliminar el entorno virtual si existe
if exist "%VENV_DIR%" (
    rmdir /s /q "%VENV_DIR%"
)

:: Crear nuevo entorno virtual
echo Creating virtual environment in %VENV_DIR%
python -m venv "%VENV_DIR%"

:: Activar el entorno virtual y instalar el paquete
call "%VENV_DIR%\Scripts\activate.bat"


endlocal
