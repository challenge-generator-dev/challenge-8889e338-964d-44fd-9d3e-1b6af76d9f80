"""Módulo de mensajes de error predefinidos para validación y cálculos.

Contiene constantes con mensajes de error organizados por categoría
para mantener coherencia en los mensajes mostrados al usuario.
"""


class ErrorMessages:
    """Clase de contenedor para mensajes de error预definidos."""
    
    # Errores de validación de monto
    AMOUNT_INVALID_TYPE = "El monto debe ser un valor numérico válido"
    AMOUNT_NEGATIVE = "El monto del préstamo debe ser un valor positivo"
    AMOUNT_ZERO = "El monto del préstamo no puede ser cero"
    AMOUNT_TOO_LARGE = "El monto del préstamo excede el límite permitido"
    
    # Errores de validación de tasa de interés
    RATE_INVALID_TYPE = "La tasa de interés debe ser un valor numérico válido"
    RATE_NEGATIVE = "La tasa de interés no puede ser negativa"
    RATE_EXCEEDS_100 = "La tasa de interés no puede exceder el 100%"
    RATE_INVALID_FORMAT = "El formato de la tasa de interés es inválido"
    
    # Errores de validación de tiempo
    YEARS_INVALID_TYPE = "El tiempo en años debe ser un valor numérico válido"
    YEARS_NEGATIVE = "El tiempo en años debe ser positivo"
    YEARS_ZERO = "El tiempo en años no puede ser cero"
    YEARS_NOT_INTEGER = "El tiempo en años debe ser un número entero"
    YEARS_TOO_LARGE = "El tiempo en años excede el límite permitido"
    
    # Errores de cálculo
    CALCULATION_OVERFLOW = "El resultado del cálculo excede los límites numéricos"
    CALCULATION_UNDERFLOW = "El resultado del cálculo es demasiado pequeño"
    CALCULATION_PRECISION = "Error de precisión en los cálculos"
    
    # Errores generales
    INVALID_INPUT = "Los datos de entrada no son válidos"
    MISSING_INPUT = "Faltan datos requeridos para el cálculo"
    UNEXPECTED_ERROR = "Ha ocurrido un error inesperado"


def get_amount_error_message(value, error_type="invalid"):
    """Genera un mensaje de error específico para errores de monto.
    
    Args:
        value: El valor que causó el error.
        error_type: Tipo de error ('invalid', 'negative', 'zero', 'large').
    
    Returns:
        str: Mensaje de error formateado.
    """
    messages = {
        "invalid": f"{ErrorMessages.AMOUNT_INVALID_TYPE}. Valor recibido: {value}",
        "negative": f"{ErrorMessages.AMOUNT_NEGATIVE}. Valor recibido: {value}",
        "zero": f"{ErrorMessages.AMOUNT_ZERO}. Valor recibido: {value}",
        "large": f"{ErrorMessages.AMOUNT_TOO_LARGE}. Valor recibido: {value}",
    }
    return messages.get(error_type, ErrorMessages.AMOUNT_INVALID_TYPE)


def get_rate_error_message(value, error_type="invalid"):
    """Genera un mensaje de error específico para errores de tasa de interés.
    
    Args:
        value: El valor que causó el error.
        error_type: Tipo de error ('invalid', 'negative', 'exceeds').
    
    Returns:
        str: Mensaje de error formateado.
    """
    messages = {
        "invalid": f"{ErrorMessages.RATE_INVALID_TYPE}. Valor recibido: {value}",
        "negative": f"{ErrorMessages.RATE_NEGATIVE}. Valor recibido: {value}",
        "exceeds": f"{ErrorMessages.RATE_EXCEEDS_100}. Valor recibido: {value}",
    }
    return messages.get(error_type, ErrorMessages.RATE_INVALID_TYPE)


def get_years_error_message(value, error_type="invalid"):
    """Genera un mensaje de error específico para errores de tiempo.
    
    Args:
        value: El valor que causó el error.
        error_type: Tipo de error ('invalid', 'negative', 'zero', 'not_integer', 'large').
    
    Returns:
        str: Mensaje de error formateado.
    """
    messages = {
        "invalid": f"{ErrorMessages.YEARS_INVALID_TYPE}. Valor recibido: {value}",
        "negative": f"{ErrorMessages.YEARS_NEGATIVE}. Valor recibido: {value}",
        "zero": f"{ErrorMessages.YEARS_ZERO}. Valor recibido: {value}",
        "not_integer": f"{ErrorMessages.YEARS_NOT_INTEGER}. Valor recibido: {value}",
        "large": f"{ErrorMessages.YEARS_TOO_LARGE}. Valor recibido: {value}",
    }
    return messages.get(error_type, ErrorMessages.YEARS_INVALID_TYPE)


def format_error_for_user(field_name: str, message: str) -> str:
    """Formatea un mensaje de error para mostrar al usuario final.
    
    Args:
        field_name: Nombre del campo que falló la validación.
        message: Mensaje de error técnico.
    
    Returns:
        str: Mensaje formateado para usuario.
    """
    return f"Error en '{field_name}': {message}"