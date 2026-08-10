"""
Pruebas Unitarias para la librería seq-stats.
Proyecto P1 - La Campaña Rango I
"""

import pytest
from seq_stats import (
    calculate_gc,
    reverse_complement,
    hamming_distance,
    calculate_n50_l50,
)


def test_calculate_gc():
    assert calculate_gc("ATGC") == 50.0
    assert calculate_gc("CCCC") == 100.0
    assert calculate_gc("AAAA") == 0.0
    assert calculate_gc("") == 0.0


def test_reverse_complement():
    assert reverse_complement("GATTACA") == "TGTAATC"
    assert reverse_complement("ATGC") == "GCAT"
    assert reverse_complement("") == ""


def test_hamming_distance():
    # Prueba estándar de distancia Hamming (Rosalind)
    assert hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7
    
    # Debe lanzar ValueError si las secuencias tienen distinta longitud
    with pytest.raises(ValueError):
        hamming_distance("ATGC", "ATG")


def test_calculate_n50_l50():
    # Longitudes de contigs: [2, 3, 4, 5, 6, 7, 8, 9, 10] -> Total = 54 bp. 50% = 27 bp.
    # Orden descendente: 10, 9, 8, 7...
    # Suma acumulada: 10 (1 contig) -> 19 (2 contigs) -> 27 (3 contigs).
    # N50 debe ser 8 bp y L50 debe ser 3 contigs.
    lengths = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    n50, l50 = calculate_n50_l50(lengths)
    assert n50 == 8
    assert l50 == 3
