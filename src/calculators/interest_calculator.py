"""Módulo de cálculo de interés simple para préstamos financieros.

Implementa la fórmula estándar del interés simple: I = P * r * t
donde:
    I = Interés generado
    P = Principal (monto del préstamo)
    r = Tasa de interés anual (en formato decimal)
    t = Tiempo en años

Este módulo utiliza Decimal para evitar errores de precisión con números flotantes.
"""

from decimal import Decimal, ROUND_HALF_UP
from typing import Union


class CalculationError(Exception):
    """Excepción personalizada para errores en cálculos financieros."""
    
    def __init__(self, message: str):
        super().__init__(message)


def convert_rate_to_decimal(rate_percent: Union[int, float, str, Decimal]) -> Decimal:
    """Convierte la tasa de interés de porcentaje a formato decimal.
    
    La tasa se ingresa como porcentaje (ej. 5 para 5%) y se convierte
    a decimal (0.05) para usar en la fórmula del interés.
    
    Args:
        rate_percent: Tasa de interés en formato porcentaje.
    
    Returns:
        Decimal: La tasa en formato decimal para cálculos.
    """
    rate_str = str(rate_percent)
    decimal_rate = Decimal(rate_str)
    
    return decimal_rate / Decimal('100')


def calculate_simple_interest(
    principal: Decimal,
    rate_percent: Decimal,
    years: int
) -> Decimal:
    """Calcula el interés simple generado por un préstamo.
    
    Fórmula: I = P * r * t
    
    Args:
        principal: Monto principal del préstamo (Decimal).
        rate_percent: Tasa de interés anual en porcentaje (Decimal).
        years: Tiempo en años (int).
    
    Returns:
        Decimal: El interés simple calculado, redondeado a 2 decimales.
    """
    if not isinstance(principal, Decimal):
        principal = Decimal(str(principal))
    
    if not isinstance(rate_percent, Decimal):
        rate_percent = Decimal(str(rate_percent))
    
    rate_decimal = convert_rate_to_decimal(rate_percent)
    
    interest = principal * rate_decimal * Decimal(str(years))
    
    return interest.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def calculate_total_amount(
    principal: Decimal,
    rate_percent: Decimal,
    years: int
) -> Decimal:
    """Calcula el monto total a pagar incluyendo principal más interés.
    
    Fórmula: Total = P + I = P + (P * r * t)
    
    Args:
        principal: Monto principal del préstamo (Decimal).
        rate_percent: Tasa de interés anual en porcentaje (Decimal).
        years: Tiempo en años (int).
    
    Returns:
        Decimal: El monto total a pagar, redondeado a 2 decimales.
    """
    interest = calculate_simple_interest(principal, rate_percent, years)
    
    total = principal + interest
    
    return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def calculate_loan_details(
    principal: Union[int, float, str, Decimal],
    rate_percent: Union[int, float, str, Decimal],
    years: Union[int, float, str]
) -> dict:
    """Calcula todos los detalles del préstamo en una sola llamada.
    
    Esta función convenience retorna un diccionario con el principal,
    la tasa, el tiempo, el interés calculado y el monto total.
    
    Args:
        principal: Monto del préstamo.
        rate_percent: Tasa de interés anual en porcentaje.
        years: Tiempo en años.
    
    Returns:
        dict: Diccionario con 'principal', 'rate', 'years', 'interest' y 'total'.
    """
    principal_dec = Decimal(str(principal))
    rate_dec = Decimal(str(rate_percent))
    years_int = int(years)
    
    interest = calculate_simple_interest(principal_dec, rate_dec, years_int)
    total = calculate_total_amount(principal_dec, rate_dec, years_int)
    
    return {
        'principal': principal_dec,
        'rate': rate_dec,
        'years': years_int,
        'interest': interest,
        'total': total
    }