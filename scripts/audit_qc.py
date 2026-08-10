"""
Auditor Automatizado de Métricas de Calidad (MultiQC JSON Parser)
Proyecto P1 - La Campaña Rango I (Ejercicio R1-XUB-011)
"""

import sys
import json
from pathlib import Path


def audit_multiqc_json(json_path: str) -> bool:
    """Parsea multiqc_data.json y emite un dictamen de calidad para cada muestra."""
    path = Path(json_path)
    if not path.exists():
        print(f"Error: El archivo '{json_path}' no existe.", file=sys.stderr)
        return False

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # MultiQC 1.35: report_general_stats_data es un dict -> modulo (ej. 'fastqc') -> muestra -> métricas
    gen_stats = data.get("report_general_stats_data", {})

    print("\n" + "=" * 60)
    print("📊 DICTAMEN AUTOMATIZADO DE CALIDAD BIOINFORMÁTICA")
    print("=" * 60)

    all_passed = True

    if isinstance(gen_stats, dict):
        for module_name, samples_dict in gen_stats.items():
            if isinstance(samples_dict, dict):
                for sample_name, metrics in samples_dict.items():
                    gc_content = metrics.get("percent_gc", 0.0)
                    dup_rate = metrics.get("percent_duplicates", 0.0)
                    total_sequences = metrics.get("total_sequences", 0)

                    print(f"Muestra: {sample_name} (Módulo: {module_name})")
                    print(f"  └─ Lecturas Totales:  {int(total_sequences):,}")
                    print(f"  └─ Contenido %GC:     {gc_content:.2f}%")
                    print(f"  └─ % Duplicación:     {dup_rate:.2f}%")

                    if gc_content < 30.0 or gc_content > 70.0:
                        print(f"  └─ ⚠️ ALERTA: Sesgo anómalo de %GC ({gc_content:.1f}%)")
                        all_passed = False
                    else:
                        print("  └─ 🟢 Estado %GC:       PASS (Óptimo)")
                    print("-" * 60)

    if all_passed:
        print("🏆 RESULTADO FINAL: TODAS LAS MUESTRAS SUPERAN EL CONTROL DE CALIDAD.")
    else:
        print("⚠️ RESULTADO FINAL: ALGUNAS MUESTRAS REQUIEREN REVISIÓN MANUAL O TRIMMING.")

    return all_passed


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 audit_qc.py <ruta_a_multiqc_data.json>")
        sys.exit(1)

    success = audit_multiqc_json(sys.argv[1])
    sys.exit(0 if success else 1)
