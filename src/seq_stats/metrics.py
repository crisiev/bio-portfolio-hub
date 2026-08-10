"""
Módulo de Métricas Genómicas y Transformaciones de Secuencias.
Proyecto P1 - seq-stats (La Campaña Rango I)
"""

def calculate_gc(sequence: str) -> float:
    """Calcula el porcentaje de contenido GC de una secuencia de ADN/ARN."""
    if not sequence:
        return 0.0
    sequence_upper = sequence.upper()
    g_count = sequence_upper.count('G')
    c_count = sequence_upper.count('C')
    return ((g_count + c_count) / len(sequence_upper)) * 100.0


def reverse_complement(sequence: str) -> str:
    """Retorna el complemento reverso de una cadena de ADN."""
    trans_table = str.maketrans("ATCGatcg", "TAGCtagc")
    return sequence.translate(trans_table)[::-1]


def hamming_distance(seq1: str, seq2: str) -> int:
    """Calcula la distancia Hamming entre dos secuencias de igual longitud."""
    if len(seq1) != len(seq2):
        raise ValueError("Las secuencias deben tener exactamente la misma longitud.")
    return sum(1 for a, b in zip(seq1, seq2) if a != b)

