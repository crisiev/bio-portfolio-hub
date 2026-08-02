# Registro de Campaña — Progreso y XP

> [!IMPORTANT]
> Este archivo registra el progreso real. El inventario, orden de ejecución y horas viven exclusivamente en [`PLAN_MAESTRO.md`](../PLAN_MAESTRO.md); no se duplican aquí para evitar divergencias.

## Estado actual

| Campo | Valor |
|---|---|
| Rango actual | I — Aprendiz de Terminal |
| XP actual | 85 |
| Último ejercicio cerrado | `R1-XUB-005` — Contar lecturas y extraer IDs con grep/awk |
| Próximo ejercicio | `R1-ROSA-01` — Rosalind Warmup: Transcribir ADN a ARN & Complemento Reverso |
| Siguiente bloque | `R1-ROSA-02` (GC & Hamming) + `R1-XUB-010` (Permisos chmod) |

> El orden cronológico lo define el calendario del Plan Maestro, no la numeración del ticket. Por eso el primer ejercicio fue `R1-XUB-002`.

## Tablero de campaña

| Rango | Unidades | XP al cerrar | Estado |
|---|---:|---:|---|
| I — Aprendiz de Terminal | 15 ejercicios + 1 jefe | 600 | En curso (85 / 600 XP) |
| II — Domador de Secuencias | 11 ejercicios + 1 jefe | 650 | Bloqueado hasta Rango I |
| III — Arquitecto de Flujos | 11 ejercicios + 1 jefe | 825 | Bloqueado hasta Rango II |
| IV — Guardián de Datos | 10 ejercicios + 1 jefe | 875 | Bloqueado hasta Rango III |
| V — Cazador de Dragones | 9 ejercicios + 1 jefe | 900 | Bloqueado hasta Rango IV |
| **Total** | **56 ejercicios + 5 jefes** | **3,850** | — |

## Bitácora de progreso

| Código | Fecha de cierre | XP | Evidencia verificable | Cicatriz / aprendizaje |
|---|---|---:|---|---|
| `R1-XUB-002` | 2026-07-31 | 25 | Entorno `bio-env` con Python 3.11, Biopython y pytest creado via `mamba` en AlmaLinux WSL | Canales de bioconda requieren `channel_priority: strict` para evitar conflictos |
| `R1-XUB-003` | 2026-07-31 | 10 | Descargado `data/raw/ecoli_test.fasta` (4.5MB NCBI U00096.3) y verificado con `head` | Uso de `curl -L` para seguir redirecciones de NCBI |
| `R1-XUB-004` | 2026-08-01 | 25 | Archivo `data/raw/ecoli_reads.fastq.gz` e inspección stream con `zcat` y `zless -S` | Detectar magic bytes: archivos sin compresión `.gz` real hacen fallar a `zcat` |
| `R1-XUB-005` | 2026-08-01 | 25 | Extracción de headers `@` (`awk 'NR%4==1'`) y secuencias (`awk 'NR%4==2'`) | Operador modulo `NR%4` en `awk` permite procesar datos FASTQ por ciclos de 4 líneas |

**XP total actual:** 85  
**Rango:** I — Aprendiz de Terminal

Al cerrar cada ejercicio, actualiza esta fila, la sección **Estado Vivo** del Plan Maestro, la bitácora mensual y el commit quirúrgico correspondiente.
