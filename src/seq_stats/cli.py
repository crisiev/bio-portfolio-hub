"""
Interfaz de Línea de Comandos (CLI) para seq-stats.
"""

import argparse
import sys
import json
from seq_stats import summarize_fasta, calculate_gc, reverse_complement


def main():
    parser = argparse.ArgumentParser(
        description="seq-stats: Analizador de secuencias FASTA y métricas genómicas."
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Comando a ejecutar")
    
    # Subcomando: fasta
    fasta_parser = subparsers.add_parser("fasta", help="Analizar archivo FASTA (N50, L50, bases)")
    fasta_parser.add_argument("path", type=str, help="Ruta al archivo FASTA")
    fasta_parser.add_argument("--json", action="store_true", help="Salida en formato JSON")

    # Subcomando: gc
    gc_parser = subparsers.add_parser("gc", help="Calcular %GC de una secuencia")
    gc_parser.add_argument("sequence", type=str, help="Cadena de nucleótidos")

    # Subcomando: revcomp
    rev_parser = subparsers.add_parser("revcomp", help="Obtener complemento reverso")
    rev_parser.add_argument("sequence", type=str, help="Cadena de nucleótidos")

    args = parser.parse_args()

    if args.command == "fasta":
        try:
            stats = summarize_fasta(args.path)
            if args.json:
                print(json.dumps(stats, indent=2))
            else:
                print("=== Resumen FASTA ===")
                for key, val in stats.items():
                    print(f"{key:15s}: {val}")
        except Exception as e:
            print(f"Error procesando FASTA: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "gc":
        gc_val = calculate_gc(args.sequence)
        print(f"Contenido GC: {gc_val:.2f}%")

    elif args.command == "revcomp":
        rc_val = reverse_complement(args.sequence)
        print(f"Complemento Reverso: {rc_val}")

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
