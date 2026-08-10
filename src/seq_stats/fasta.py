"""
Módulo de Procesamiento de FASTA y Estadísticas de Ensamblaje.
Proyecto P1 - seq-stats (La Campaña Rango I)
"""

from typing import List, Tuple, Dict, Any
from Bio import SeqIO


def parse_fasta_lengths(fasta_path: str) -> List[int]:
    """Lee un archivo FASTA y retorna la lista de longitudes de sus secuencias."""
    lengths = [len(record.seq) for record in SeqIO.parse(fasta_path, "fasta")]
    if not lengths:
        raise ValueError(f"El archivo '{fasta_path}' está vacío o no es un FASTA válido.")
    return lengths


def calculate_n50_l50(lengths: List[int]) -> Tuple[int, int]:
    """
    Calcula el N50 (longitud en bp) y L50 (conteo de contigs) de una lista de longitudes.
    """
    if not lengths:
        return 0, 0

    sorted_lengths = sorted(lengths, reverse=True)
    total_length = sum(sorted_lengths)
    target = total_length / 2.0

    cumulative_sum = 0
    for l50, length in enumerate(sorted_lengths, start=1):
        cumulative_sum += length
        if cumulative_sum >= target:
            return length, l50

    return sorted_lengths[-1], len(sorted_lengths)


def summarize_fasta(fasta_path: str) -> Dict[str, Any]:
    """Genera un resumen estadístico completo de un archivo FASTA."""
    lengths = parse_fasta_lengths(fasta_path)
    n50, l50 = calculate_n50_l50(lengths)

    return {
        "num_sequences": len(lengths),
        "total_bases": sum(lengths),
        "min_length": min(lengths),
        "max_length": max(lengths),
        "n50": n50,
        "l50": l50
    }
