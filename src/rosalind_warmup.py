# scratch/rosalind_warmup.py

def transcribe_dna(dna: str) -> str:
    """Convierte ADN a ARN reemplazando T por U."""
    return dna.replace("T", "U")

def reverse_complement(dna: str) -> str:
    """Retorna el complemento reverso 5' -> 3'."""
    tabla = str.maketrans("ATCG", "TAGC")
    return dna[::-1].translate(tabla)

def calculate_gc(dna: str) -> float:
    """Calcula el porcentaje de contenido GC."""
    g_count = dna.count("G")
    c_count = dna.count("C")
    return ((g_count + c_count) / len(dna)) * 100

def hamming_distance(s1: str, s2: str) -> int:
    """Calcula la distancia Hamming entre dos secuencias de igual longitud."""
    if len(s1) != len(s2):
        raise ValueError("Las secuencias deben tener la misma longitud")
    return sum(1 for a, b in zip(s1, s2) if a != b)

if __name__ == "__main__":
    # Datos de prueba
    sample_dna = "GATGGAACTTGACTACGTAAATT"
    s1 = "GAGCCTACTAACGGGAT"
    s2 = "CATCGTAATGACGGCCT"
    
    print(f"Original DNA : {sample_dna}")
    print(f"RNA Transcr. : {transcribe_dna(sample_dna)}")
    print(f"Rev Compl.   : {reverse_complement(sample_dna)}")
    print(f"GC Content   : {calculate_gc(sample_dna):.2f}%")
    print(f"Hamming Dist : {hamming_distance(s1, s2)}")

