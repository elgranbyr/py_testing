from pathlib import Path

from setuptools import find_packages, setup

# Lee el contenido del README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Obtiene la versión del paquete
VERSION = "0.1.0"

# Dependencias requeridas
INSTALL_REQUIRES = [
    "requests>=2.28.0",
    "pandas>=1.5.0",
    "numpy>=1.23.0",
]

# Dependencias opcionales para desarrollo
EXTRAS_REQUIRE = {
    "dev": [
        "pytest>=7.0.0",
        "pytest-cov>=3.0.0",
        "black>=22.0.0",
        "isort>=5.10.0",
        "flake8>=4.0.0",
        "mypy>=0.950",
    ],
    "docs": [
        "sphinx>=4.5.0",
        "sphinx-rtd-theme>=1.0.0",
    ],
}

setup(
    # Información básica del paquete
    name="your-package-name",
    version=VERSION,
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # URLs importantes
    url="https://github.com/username/repository",
    project_urls={
        "Bug Tracker": "https://github.com/username/repository/issues",
        "Documentation": "https://your-package.readthedocs.io/",
        "Source Code": "https://github.com/username/repository",
    },
    # Configuración del paquete
    packages=find_packages(exclude=["tests*", "docs*"]),
    include_package_data=True,
    package_data={
        "": ["*.json", "*.yaml", "*.yml"],  # Archivos adicionales a incluir
    },
    # Dependencias
    python_requires=">=3.8",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    # Entradas de consola (CLI)
    entry_points={
        "console_scripts": [
            "your-command=your_package.cli:main",
        ],
    },
    # Clasificadores
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    # Metadatos adicionales
    keywords="keywords, for, your, package",
    license="MIT",
    platforms=["any"],
    zip_safe=False,
)
