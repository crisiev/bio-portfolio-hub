"""
Rosalind PROT: Translating RNA into Protein
Dominio: D2-Prog (Algoritmos de Secuencias & Biopython)
Autor: Christian Alcívar
"""

# Tabla del Código Genético Estándar
# Los codones de parada (UAA, UAG, UGA) se definen explícitamente como None
CODON_TABLE: dict[str, str | None] = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y", "UAA": None, "UAG": None,
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "UGU": "C", "UGC": "C", "UGA": None, "UGG": "W",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

def translate_rna(rna_sequence: str) -> str:
    """
    Traduce una secuencia de ARN a una cadena de aminoácidos.
    Se detiene al encontrar el primer codón de parada.
    """
    clean_rna = rna_sequence.strip().upper()
    amino_acids: list[str] = []
    
    # Limite asegurando múltiplos de 3
    limit = len(clean_rna) - (len(clean_rna) % 3)
    
    for i in range(0, limit, 3):
        codon = clean_rna[i:i+3]
        
        if codon not in CODON_TABLE:
            raise ValueError(f"Error Genómico: Codón inválido detectado '{codon}' en posición {i}.")
        
        amino_acid = CODON_TABLE[codon]
        
        # Si encontramos un codón de parada (None), terminamos la traducción
        if amino_acid is None:
            break
            
        amino_acids.append(amino_acid)
        
    return "".join(amino_acids)

if __name__ == "__main__":
    test_rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    result = translate_rna(test_rna)
    print(f"ARN Entrada : {test_rna}")
    print(f"Proteína    : {result}")
    
    expected = "MAMAPRTEINSTRING"
    assert result == expected, f"Error: Se esperaba '{expected}', pero se obtuvo '{result}'"
    print("✅ Prueba de Rosalind PROT SUPERADA EXITOSAMENTE.")
