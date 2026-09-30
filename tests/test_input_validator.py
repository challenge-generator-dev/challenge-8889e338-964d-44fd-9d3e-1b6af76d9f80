import pytest
from src.validators.input_validator import validate_amount, validate_interest_rate, validate_years


class TestInputValidator:
    """Suite de pruebas para validadores de entrada."""

    def test_validate_amount_positive(self):
        """Verifica que montos positivos son aceptados."""
        result = validate_amount(1000.0)
        assert result is True

    def test_validate_amount_zero(self):
        """Verifica que el monto cero es válido."""
        result = validate_amount(0.0)
        assert result is True

    def test_validate_amount_negative(self):
        """Verifica que montos negativos son rechazados."""
        result = validate_amount(-500.0)
        assert result is False

    def test_validate_interest_rate_valid(self):
        """Verifica que tasas entre 0 y 100 son aceptadas."""
        result = validate_interest_rate(5.5)
        assert result is True

    def test_validate_interest_rate_zero(self):
        """Verifica que tasa cero es válida."""
        result = validate_interest_rate(0.0)
        assert result is True

    def test_validate_interest_rate_above_100(self):
        """Verifica que tasas mayores a 100 son rechazadas."""
        result = validate_interest_rate(150.0)
        assert result is False

    def test_validate_interest_rate_negative(self):
        """Verifica que tasas negativas son rechazadas."""
        result = validate_interest_rate(-10.0)
        assert result is False

    def test_validate_years_positive(self):
        """Verifica que años positivos son aceptados."""
        result = validate_years(5)
        assert result is True

    def test_validate_years_zero(self):
        """Verifica que cero años es válido."""
        result = validate_years(0)
        assert result is True

    def test_validate_years_negative(self):
        """Verifica que años negativos son rechazados."""
        result = validate_years(-1)
        assert result is False

    def test_validate_amount_with_string(self):
        """Verifica comportamiento con entrada no numérica."""
        with pytest.raises((TypeError, ValueError)):
            validate_amount("mil")

    def test_validate_interest_rate_with_string(self):
        """Verifica comportamiento con tasa no numérica."""
        with pytest.raises((TypeError, ValueError)):
            validate_interest_rate("cinco")