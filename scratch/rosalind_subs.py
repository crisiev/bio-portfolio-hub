"""
Rosalind SUBS: Finding a Motif in DNA
Dominio: D2-Prog (Algoritmos de Secuencias)
Autor: Christian Alcívar
"""

def find_dna_motif(sequence: str, motif: str) -> list[int]:
    """
    Encuentra todas las posiciones (1-indexed, estándar biológico) donde
    ocurre un motivo dentro de una secuencia de ADN, permitiendo solapamiento.
    """
    seq = sequence.strip().upper()
    sub = motif.strip().upper()
    positions: list[int] = []
    
    len_seq = len(seq)
    len_sub = len(sub)
    
    # Recorrer la secuencia permitiendo solapamiento (overlapping)
    for i in range(len_seq - len_sub + 1):
        if seq[i:i+len_sub] == sub:
            # 1-indexed para cumplir el estándar de Rosalind y GenBank
            positions.append(i + 1)
            
    return positions

if __name__ == "__main__":
    # Caso de prueba oficial de Rosalind SUBS
    seq_test = "GATATATGCATATACTT"
    motif_test = "ATAT"
    
    pos = find_dna_motif(seq_test, motif_test)
    print(f"Secuencia: {seq_test}")
    print(f"Motivo   : {motif_test}")
    print("Posiciones encontradas (1-indexed):", " ".join(map(str, pos)))
    
    expected = [2, 4, 10]
    assert pos == expected, f"Error: Se esperaba {expected}, se obtuvo {pos}"
    print("✅ Prueba de Rosalind SUBS SUPERADA EXITOSAMENTE.")
