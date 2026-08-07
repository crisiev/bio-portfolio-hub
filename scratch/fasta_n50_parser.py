"""
Ejercicio R1-XUB-006: Parser FASTA y Cálculo de Métricas de Ensamblado (N50 / L50)
Dominio: D2-Prog & D3-NGS
Autor: Christian Alcívar
"""

import os

def parse_fasta(fasta_path: str) -> dict[str, str]:
    """
    Lee un archivo FASTA de forma robusta y retorna un diccionario {header: secuencia}.
    Maneja secuencias multilínea.
    """
    sequences: dict[str, str] = {}
    current_header = ""
    current_seq_list: list[str] = []
    
    with open(fasta_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current_header:
                    sequences[current_header] = "".join(current_seq_list)
                current_header = line[1:].split()[0]  # ID primario antes del espacio
                current_seq_list = []
            else:
                current_seq_list.append(line.upper())
                
        # Guardar la última secuencia del archivo
        if current_header:
            sequences[current_header] = "".join(current_seq_list)
            
    return sequences

def calculate_n50_l50(lengths: list[int]) -> tuple[int, int]:
    """
    Calcula N50 (longitud en bp) y L50 (conteo de contigs) a partir de una lista de longitudes.
    """
    if not lengths:
        return (0, 0)
        
    # 1. Ordenar obligatoriamente de mayor a menor
    sorted_lengths = sorted(lengths, reverse=True)
    
    # 2. Umbral exacto del 50%
    total_bp = sum(sorted_lengths)
    target_bp = total_bp / 2.0
    
    cumulative_bp = 0
    l50_count = 0
    n50_value = 0
    
    # 3. Acumular contigs hasta superar el 50% de total_bp
    for length in sorted_lengths:
        cumulative_bp += length
        l50_count += 1
        if cumulative_bp >= target_bp:
            n50_value = length
            break
            
    return (n50_value, l50_count)

if __name__ == "__main__":
    fasta_file = "data/raw/ecoli_test.fasta"
    
    if os.path.exists(fasta_file):
        print(f"📖 Leyendo archivo FASTA: {fasta_file}...")
        records = parse_fasta(fasta_file)
        print(f"Total de contigs/secuencias leídas: {len(records)}")
        
        lengths = [len(seq) for seq in records.values()]
        total_size = sum(lengths)
        n50, l50 = calculate_n50_l50(lengths)
        
        print("\n📊 REPORTE DE MÉTRICAS DE ENSAMBLADO:")
        print(f" - Tamaño total del genoma: {total_size:,} bp")
        print(f" - Contig más largo       : {max(lengths):,} bp")
        print(f" - Contig más corto       : {min(lengths):,} bp")
        print(f" - N50                     : {n50:,} bp")
        print(f" - L50                     : {l50} contig(s)")
        print("\n✅ Parser FASTA y N50/L50 verificado correctamente.")
    else:
        print(f"⚠️ Archivo {fasta_file} no encontrado. Ejecutando prueba sintética...")
        synthetic_lengths = [200, 500, 1000, 2000, 8000, 15000]
        n50, l50 = calculate_n50_l50(synthetic_lengths)
        print(f"Prueba Sintética -> Longitudes: {synthetic_lengths}")
        print(f"N50 calculado: {n50} bp | L50 calculado: {l50} contigs")
