"""
Programa para calcular el interés simple de un préstamo.
Solicita al usuario el monto del préstamo, la tasa de interés anual y el tiempo en años,
valida las entradas y calcula el interés ganado y el monto total a pagar.
"""

import sys
from validators.input_validator import validate_loan_inputs
from calculators.interest_calculator import calculate_simple_interest
from utils.error_messages import INPUT_ERROR_MESSAGE

def main():
    """Función principal que coordina la entrada, validación y cálculo."""
    print("=== Calculadora de Interés Simple ===")
    
    try:
        # Solicitar datos al usuario
        principal = float(input("Ingrese el monto del préstamo: $"))
        rate = float(input("Ingrese la tasa de interés anual (%): "))
        time = float(input("Ingrese el tiempo en años: "))
        
        # Validar entradas
        validate_loan_inputs(principal, rate, time)
        
        # Calcular interés y monto total
        interest, total_amount = calculate_simple_interest(principal, rate, time)
        
        # Mostrar resultados
        print(f"\nInterés ganado: ${interest:.2f}")
        print(f"Monto total a pagar: ${total_amount:.2f}")
        
    except ValueError as ve:
        print(f"\nError: {ve}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nError inesperado: {INPUT_ERROR_MESSAGE}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()