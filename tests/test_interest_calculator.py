import pytest
from src.calculators.interest_calculator import calculate_simple_interest, calculate_total_amount


class TestInterestCalculator:
    """Suite de pruebas para cálculos de interés."""

    def test_calculate_simple_interest_basic(self):
        """Verifica cálculo básico de interés simple."""
        principal = 1000.0
        rate = 5.0
        years = 1
        result = calculate_simple_interest(principal, rate, years)
        assert result == 50.0

    def test_calculate_simple_interest_multiple_years(self):
        """Verifica cálculo con múltiples años."""
        principal = 1000.0
        rate = 10.0
        years = 3
        result = calculate_simple_interest(principal, rate, years)
        assert result == 300.0

    def test_calculate_simple_interest_zero_rate(self):
        """Verifica que tasa cero produce interés cero."""
        principal = 5000.0
        rate = 0.0
        years = 5
        result = calculate_simple_interest(principal, rate, years)
        assert result == 0.0

    def test_calculate_simple_interest_zero_years(self):
        """Verifica que cero años produce interés cero."""
        principal = 2000.0
        rate = 8.0
        years = 0
        result = calculate_simple_interest(principal, rate, years)
        assert result == 0.0

    def test_calculate_simple_interest_large_values(self):
        """Verifica cálculo con valores grandes."""
        principal = 100000.0
        rate = 12.5
        years = 10
        result = calculate_simple_interest(principal, rate, years)
        assert result == 125000.0

    def test_calculate_total_amount_basic(self):
        """Verifica cálculo del monto total."""
        principal = 1000.0
        interest = 50.0
        result = calculate_total_amount(principal, interest)
        assert result == 1050.0

    def test_calculate_total_amount_zero_interest(self):
        """Verifica monto total con interés cero."""
        principal = 1000.0
        interest = 0.0
        result = calculate_total_amount(principal, interest)
        assert result == 1000.0

    def test_calculate_total_amount_large_interest(self):
        """Verifica monto total con interés mayor al principal."""
        principal = 1000.0
        interest = 1500.0
        result = calculate_total_amount(principal, interest)
        assert result == 2500.0

    def test_calculate_simple_interest_with_fractional_rate(self):
        """Verifica cálculo con tasa fraccionaria."""
        principal = 1000.0
        rate = 4.5
        years = 2
        result = calculate_simple_interest(principal, rate, years)
        assert result == 90.0

    def test_calculate_simple_interest_with_fractional_principal(self):
        """Verifica cálculo con principal fraccionario."""
        principal = 1234.56
        rate = 10.0
        years = 1
        result = calculate_simple_interest(principal, rate, years)
        assert result == 123.456