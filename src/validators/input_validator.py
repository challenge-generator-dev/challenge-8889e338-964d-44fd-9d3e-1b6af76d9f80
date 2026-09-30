"""Módulo de validación de datos de entrada para el cálculo de interés simple.

Este módulo contiene funciones puras que verifican la validez de los
parámetros de entrada: monto del préstamo, tasa de interés y tiempo en años.
"""

from decimal import Decimal, InvalidOperation
from typing import Union


class ValidationError(Exception):
    """Excepción personalizada para errores de validación de entrada."""
    
    def __init__(self, message: str, field: str = "unknown"):
        self.field = field
        super().__init__(message)


def validate_positive_amount(amount: Union[int, float, str, Decimal]) -> Decimal:
    """Valida que el monto del préstamo sea un valor positivo.
    
    Args:
        amount: El monto del préstamo a validar. Puede ser int, float, str o Decimal.
    
    Returns:
        Decimal: El monto validado como Decimal.
    
    Raises:
        ValidationError: Si el monto es negativo, cero o no es numérico.
    """
    try:
        decimal_amount = Decimal(str(amount))
    except (InvalidOperation, ValueError, TypeError) as e:
        raise ValidationError(
            f"El monto debe ser un valor numérico válido. Valor recibido: {amount}",
            field="amount"
        ) from e
    
    if decimal_amount <= 0:
        raise ValidationError(
            f"El monto del préstamo debe ser positivo. Valor recibido: {amount}",
            field="amount"
        )
    
    return decimal_amount


def validate_interest_rate(rate: Union[int, float, str, Decimal]) -> Decimal:
    """Valida que la tasa de interés esté en un rango válido (0-100%).
    
    La tasa debe expresarse como porcentaje (ej. 5 para 5%) y se convierte
    a decimal para cálculos internos.
    
    Args:
        rate: La tasa de interés anual a validar.
    
    Returns:
        Decimal: La tasa validada como Decimal.
    
    Raises:
        ValidationError: Si la tasa es negativa o mayor al 100%.
    """
    try:
        decimal_rate = Decimal(str(rate))
    except (InvalidOperation, ValueError, TypeError) as e:
        raise ValidationError(
            f"La tasa de interés debe ser un valor numérico válido. Valor recibido: {rate}",
            field="interest_rate"
        ) from e
    
    if decimal_rate < 0:
        raise ValidationError(
            f"La tasa de interés no puede ser negativa. Valor recibido: {rate}",
            field="interest_rate"
        )
    
    if decimal_rate > 100:
        raise ValidationError(
            f"La tasa de interés no puede exceder el 100%. Valor recibido: {rate}",
            field="interest_rate"
        )
    
    return decimal_rate


def validate_years(years: Union[int, float, str]) -> int:
    """Valida que el tiempo en años sea un valor entero positivo.
    
    Args:
        years: El tiempo en años a validar.
    
    Returns:
        int: El tiempo validado como entero positivo.
    
    Raises:
        ValidationError: Si el tiempo no es un número positivo o es cero.
    """
    try:
        numeric_years = float(years)
    except (ValueError, TypeError) as e:
        raise ValidationError(
            f"El tiempo en años debe ser un valor numérico válido. Valor recibido: {years}",
            field="years"
        ) from e
    
    if numeric_years <= 0:
        raise ValidationError(
            f"El tiempo en años debe ser positivo. Valor recibido: {years}",
            field="years"
        )
    
    if not numeric_years.is_integer():
        raise ValidationError(
            f"El tiempo en años debe ser un número entero. Valor recibido: {years}",
            field="years"
        )
    
    return int(numeric_years)


def validate_all_inputs(amount, rate, years):
    """Valida todos los parámetros de entrada simultáneamente.
    
    Esta función orchestrar valida cada parámetro y retorna una tupla
    con los valores validados listos para cálculo.
    
    Args:
        amount: Monto del préstamo.
        rate: Tasa de interés anual.
        years: Tiempo en años.
    
    Returns:
        tuple: (amount_decimal, rate_decimal, years_int) validados.
    
    Raises:
        ValidationError: Si cualquier parámetro es inválido.
    """
    validated_amount = validate_positive_amount(amount)
    validated_rate = validate_interest_rate(rate)
    validated_years = validate_years(years)
    
    return validated_amount, validated_rate, validated_years