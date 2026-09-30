"""
Módulo principal del Calculador de Interés Simple.

Este paquete proporciona funcionalidades para calcular el interés simple
de préstamos financieros, con validación robusta de entradas y manejo
de errores descriptivo.

Paquetes incluidos:
    - src.validators: Validación de entradas del usuario
    - src.calculators: Cálculo de interés simple
    - src.utils: Utilidades y manejo de errores
"""

import sys
from typing import Optional, Tuple
from decimal import Decimal

# Constantes de configuración global del módulo
VERSION = "1.0.0"
NOMBRE_PROGRAMA = "Calculador de Interés Simple"
DESCRIPCION_PROGRAMA = "Herramienta para calcular el interés simple de préstamos financieros"

# Valores por defecto para cálculos
TASA_MINIMA = Decimal("0.0")
TASA_MAXIMA = Decimal("100.0")
MONTO_MINIMO = Decimal("0.01")
TIEMPO_MINIMO = Decimal("0.0")
TIEMPO_MAXIMO = Decimal("50.0")

# Formato de salida
FORMATO_DECIMAL = "{:.2f}"
MENSAJE_BIENVENIDA = """
========================================
{} - v{}
{}
========================================
""".format(NOMBRE_PROGRAMA, VERSION, DESCRIPCION_PROGRAMA)

# Códigos de salida del programa
EXIT_SUCCESS = 0
EXIT_ERROR_INPUT = 1
EXIT_ERROR_CALCULO = 2
EXIT_ERROR_DESCONOCIDO = 3

def obtener_version() -> str:
    """
    Retorna la versión actual del programa.
    
    Returns:
        str: Versión del programa en formato semántico
    """
    return VERSION

def obtener_info_programa() -> Tuple[str, str, str]:
    """
    Retorna información básica del programa.
    
    Returns:
        Tuple[str, str, str]: Tupla con (nombre, versión, descripción)
    """
    return (NOMBRE_PROGRAMA, VERSION, DESCRIPCION_PROGRAMA)

def mostrar_bienvenida() -> None:
    """Imprime el mensaje de bienvenida del programa."""
    print(MENSAJE_BIENVENIDA)

def obtener_codigo_salida(tipo_error: str) -> int:
    """
    Retorna el código de salida apropiado según el tipo de error.
    
    Args:
        tipo_error: Tipo de error ocurrido ('input', 'calculo', 'desconocido')
    
    Returns:
        int: Código de salida del sistema
    """
    codigos = {
        "input": EXIT_ERROR_INPUT,
        "calculo": EXIT_ERROR_CALCULO,
        "desconocido": EXIT_ERROR_DESCONOCIDO
    }
    return codigos.get(tipo_error, EXIT_ERROR_DESCONOCIDO)

def configurarLocale() -> None:
    """
    Configura el locale para formateo de números.
    
    Asegura que el separador decimal sea el punto para
    compatibilidad con los cálculos.
    """
    import locale
    try:
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    except locale.Error:
        pass

def inicializar_modulo() -> None:
    """
    Inicializa el módulo configurando el entorno.
    
    Esta función debe llamarse al inicio del programa
    para asegurar que todos los componentes estén
    correctamente configurados.
    """
    configurarLocale()
    mostrar_bienvenida()

def validar_rango_tasa(tasa: Decimal) -> bool:
    """
    Valida que la tasa de interés esté en el rango permitido.
    
    Args:
        tasa: Tasa de interés a validar
    
    Returns:
        bool: True si la tasa es válida
    """
    return TASA_MINIMA <= tasa <= TASA_MAXIMA

def validar_rango_monto(monto: Decimal) -> bool:
    """
    Valida que el monto del préstamo sea válido.
    
    Args:
        monto: Monto del préstamo a validar
    
    Returns:
        bool: True si el monto es válido
    """
    return monto >= MONTO_MINIMO

def validar_rango_tiempo(tiempo: Decimal) -> bool:
    """
    Valida que el tiempo en años esté en el rango permitido.
    
    Args:
        tiempo: Tiempo en años a validar
    
    Returns:
        bool: True si el tiempo es válido
    """
    return TIEMPO_MINIMO <= tiempo <= TIEMPO_MAXIMO

def formatear_moneda(valor: Decimal) -> str:
    """
    Formatea un valor decimal como moneda.
    
    Args:
        valor: Valor a formatear
    
    Returns:
        str: Valor formateado con símbolo de moneda
    """
    return f"${FORMATO_DECIMAL.format(valor)}"

def formatear_porcentaje(valor: Decimal) -> str:
    """
    Formatea un valor decimal como porcentaje.
    
    Args:
        valor: Valor a formatear (ej: 0.05 para 5%)
    
    Returns:
        str: Porcentaje formateado
    """
    return f"{FORMATO_DECIMAL.format(valor * 100)}%"

def obtener_limites() -> dict:
    """
    Retorna un diccionario con los límites de validación.
    
    Returns:
        dict: Diccionario con límites de tasa, monto y tiempo
    """
    return {
        "tasa_minima": TASA_MINIMA,
        "tasa_maxima": TASA_MAXIMA,
        "monto_minimo": MONTO_MINIMO,
        "tiempo_minimo": TIEMPO_MINIMO,
        "tiempo_maximo": TIEMPO_MAXIMO
    }

def verificar_entorno() -> bool:
    """
    Verifica que el entorno de ejecución sea el adecuado.
    
    Returns:
        bool: True si el entorno es válido
    """
    return sys.version_info >= (3, 8)

def obtener_info_python() -> str:
    """
    Retorna información sobre la versión de Python.
    
    Returns:
        str: Información de versión
    """
    return f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

def ejecutar_inicio() -> None:
    """
    Ejecuta la secuencia de inicio del programa.
    
    Verifica el entorno, muestra la bienvenida e informa
    sobre la versión de Python en uso.
    """
    if not verificar_entorno():
        print("Advertencia: Se recomienda Python 3.8 o superior")
    
    inicializar_modulo()
    print(f"Entorno: {obtener_info_python()}")
    print()