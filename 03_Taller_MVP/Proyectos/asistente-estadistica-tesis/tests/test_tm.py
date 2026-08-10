import pytest
from src.services.tm_calculator import calculate_tm

def test_calculate_tm_wallace():
    """
    Prueba el cálculo de Tm usando la regla de Wallace (básica).
    Secuencia: ATGC (1A, 1T, 1G, 1C)
    Fórmula Wallace: 2 * (A+T) + 4 * (G+C)
    Tm = 2*(2) + 4*(2) = 4 + 8 = 12.0 °C
    """
    secuencia = "ATGC"
    resultado = calculate_tm(secuencia)
    
    assert resultado == 12.0
    assert isinstance(resultado, float)
