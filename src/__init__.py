"""
Paquete principal del código fuente.

Este módulo contiene la lógica central del calculador de interés simple,
organizada en subpaquetes especializados para validación, cálculo y
utilidades comunes.
"""

import os
import sys
from pathlib import Path
from typing import List, Optional

# Definición de la ruta base del proyecto
RUTA_PROYECTO = Path(__file__).parent.parent
RUTA_SRC = Path(__file__).parent
RUTA_TESTS = RUTA_PROYECTO / "tests"

def obtener_ruta_proyecto() -> Path:
    """
    Retorna la ruta raíz del proyecto.
    
    Returns:
        Path: Ruta absoluta del directorio del proyecto
    """
    return RUTA_PROYECTO

def obtener_ruta_src() -> Path:
    """
    Retorna la ruta del directorio src.
    
    Returns:
        Path: Ruta absoluta del directorio src
    """
    return RUTA_SRC

def verificar_estructura_directorios() -> bool:
    """
    Verifica que la estructura de directorios requerida exista.
    
    Returns:
        bool: True si la estructura es válida
    """
    directorios_requeridos = [
        RUTA_SRC / "validators",
        RUTA_SRC / "calculators",
        RUTA_SRC / "utils",
        RUTA_TESTS
    ]
    
    for directorio in directorios_requeridos:
        if not directorio.exists():
            return False
    return True

def crear_directorios_si_no_existen() -> None:
    """
    Crea los directorios necesarios si no existen.
    
    Esta función asegura que la estructura de carpetas
    del proyecto esté disponible para el funcionamiento
    correcto del programa.
    """
    directorios = [
        RUTA_SRC / "validators",
        RUTA_SRC / "calculators",
        RUTA_SRC / "utils",
        RUTA_TESTS
    ]
    
    for directorio in directorios:
        directorio.mkdir(parents=True, exist_ok=True)

def listar_modulos_disponibles() -> List[str]:
    """
    Lista los módulos disponibles en el paquete src.
    
    Returns:
        List[str]: Nombres de los submódulos disponibles
    """
    modulos = []
    
    for item in RUTA_SRC.iterdir():
        if item.is_file() and item.suffix == ".py" and item.name != "__init__.py":
            modulos.append(item.stem)
        elif item.is_dir() and (item / "__init__.py").exists():
            modulos.append(item.name)
    
    return sorted(modulos)

def importar_modulo(nombre_modulo: str):
    """
    Importa un módulo dinámicamente por su nombre.
    
    Args:
        nombre_modulo: Nombre del módulo a importar
    
    Returns:
        Módulo importado
    
    Raises:
        ImportError: Si el módulo no existe
    """
    try:
        return __import__(f"src.{nombre_modulo}", fromlist=["*"])
    except ImportError as e:
        raise ImportError(f"No se pudo importar el módulo '{nombre_modulo}': {e}")

def obtener_ruta_absoluta(relativo: str) -> Path:
    """
    Convierte una ruta relativa a absoluta basada en la raíz del proyecto.
    
    Args:
        relativo: Ruta relativa desde la raíz del proyecto
    
    Returns:
        Path: Ruta absoluta
    """
    return RUTA_PROYECTO / relativo

def verificar_archivo_existe(ruta: str) -> bool:
    """
    Verifica si un archivo existe en el proyecto.
    
    Args:
        ruta: Ruta del archivo a verificar
    
    Returns:
        bool: True si el archivo existe
    """
    return (RUTA_PROYECTO / ruta).exists()

def obtener_configuracion_ejecucion() -> dict:
    """
    Retorna la configuración de ejecución del programa.
    
    Returns:
        dict: Diccionario con configuración
    """
    return {
        "ruta_proyecto": str(RUTA_PROYECTO),
        "ruta_src": str(RUTA_SRC),
        "ruta_tests": str(RUTA_TESTS),
        "python_version": f"{sys.version_info.major}.{sys.version_info.minor}",
        "plataforma": sys.platform
    }

def mostrar_info_configuracion() -> None:
    """
    Imprime información de configuración del entorno.
    
    Útil para depuración y para verificar que el
    entorno está correctamente configurado.
    """
    config = obtener_configuracion_ejecucion()
    
    print("Configuración del entorno de ejecución:")
    print(f"  Ruta del proyecto: {config['ruta_proyecto']}")
    print(f"  Ruta src: {config['ruta_src']}")
    print(f"  Ruta tests: {config['ruta_tests']}")
    print(f"  Python: {config['python_version']}")
    print(f"  Plataforma: {config['plataforma']}")
    print()
    print("Módulos disponibles:")
    for modulo in listar_modulos_disponibles():
        print(f"  - {modulo}")

def validar_ambiente() -> bool:
    """
    Valida que el ambiente esté correctamente configurado.
    
    Returns:
        bool: True si el ambiente es válido
    """
    if sys.version_info < (3, 8):
        print("Error: Se requiere Python 3.8 o superior")
        return False
    
    if not verificar_estructura_directorios():
        print("Advertencia: Estructura de directorios incompleta. Intentando crear...")
        crear_directorios_si_no_existen()
    
    return True

def iniciar_aplicacion() -> None:
    """
    Inicia la aplicación verificando el entorno.
    
    Esta función prepara todo lo necesario para
    que el programa pueda ejecutarse correctamente.
    """
    if not validar_ambiente():
        sys.exit(1)
    
    print("Entorno validado correctamente.")
    print()