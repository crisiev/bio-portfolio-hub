#!/usr/bin/env bash
# ==============================================================================
# Script: auto_qc.sh
# Descripción: Automatización de Control de Calidad FASTQ (FastQC + MultiQC + Audit)
# Proyecto: La Campaña Rango I (Ejercicio R1-XUB-011)
# ==============================================================================

set -euo pipefail

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

if [ "$#" -ne 2 ]; then
    echo -e "${RED}[ERROR] Uso incorrecto del script.${NC}"
    echo -e "Uso: $0 <directorio_fastq_entrada> <directorio_reportes_salida>"
    exit 1
fi

INPUT_DIR="$1"
OUTPUT_DIR="$2"

if [ ! -d "$INPUT_DIR" ]; then
    echo -e "${RED}[ERROR] El directorio de entrada '$INPUT_DIR' no existe.${NC}"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

echo -e "${YELLOW}====================================================${NC}"
echo -e "${YELLOW}🚀 Iniciando Pipeline Automatizado de QC (FastQC + MultiQC + Auditoría)${NC}"
echo -e "${YELLOW}====================================================${NC}"
echo -e "Directorio de Entrada: $INPUT_DIR"
echo -e "Directorio de Salida:  $OUTPUT_DIR"
echo -e ""

echo -e "${GREEN}[1/3] Ejecutando FastQC en archivos FASTQ...${NC}"
fastqc "$INPUT_DIR"/*.fastq* -o "$OUTPUT_DIR"

echo -e "${GREEN}[2/3] Compilando reporte consolidado con MultiQC...${NC}"
multiqc "$OUTPUT_DIR" -o "$OUTPUT_DIR" --force

echo -e "${GREEN}[3/3] Ejecutando Auditoría Automática con Python...${NC}"
python3 scripts/audit_qc.py "$OUTPUT_DIR/multiqc_data/multiqc_data.json"

echo -e ""
echo -e "${GREEN}====================================================${NC}"
echo -e "${GREEN}✅ Pipeline de QC y Auditoría completado con éxito.${NC}"
echo -e "${GREEN}Reporte HTML: $OUTPUT_DIR/multiqc_report.html${NC}"
echo -e "${GREEN}====================================================${NC}"
