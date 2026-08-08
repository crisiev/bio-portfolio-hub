# Registro de Campaña — Progreso y XP

> [!IMPORTANT]
> Este archivo registra el progreso real. El inventario, orden de ejecución y horas viven exclusivamente en [`PLAN_MAESTRO.md`](../PLAN_MAESTRO.md); no se duplican aquí para evitar divergencias.

## Estado actual

| Campo | Valor |
|---|---|
| Rango actual | I — Aprendiz de Terminal |
| XP actual | 320 |
| Último ejercicio cerrado | `R1-XUB-008` — Inicializar Git, commits limpios y SSH keys en WSL |
| Próximo ejercicio | `R1-XUB-009` — Publicar repo en GitHub con README profesional |
| Siguiente bloque | `R1-XUB-012` (GitHub Profile README crisiev/crisiev) |

> El orden cronológico lo define el calendario del Plan Maestro, no la numeración del ticket. Por eso el primer ejercicio fue `R1-XUB-002`.

## Tablero de campaña

| Rango | Unidades | XP al cerrar | Estado |
|---|---:|---:|---|
| I — Aprendiz de Terminal | 15 ejercicios + 1 jefe | 600 | En curso (320 / 600 XP) |
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
| `R1-ROSA-01` | 2026-08-04 | 10 | Script `scratch/rosalind_warmup.py`: `transcribe_dna` y `reverse_complement` con `maketrans` y `[::-1]` | Inversión de secuencia por slicing `[::-1]` combinada con mapa de substitución |
| `R1-ROSA-02` | 2026-08-04 | 25 | Script `scratch/rosalind_warmup.py`: `calculate_gc` y `hamming_distance` con `zip` | %GC define estabilidad de primers y GC-bias; distancia Hamming cuenta SNPs |
| `R1-XUB-010` | 2026-08-04 | 25 | Protección contra escritura con `chmod -R a-w data/raw/` verificada (`Permission denied`) | Quitar permiso `-w` en datasets crudos previene pérdida accidental de datos en pipelines |
| `R1-ROSA-03` | 2026-08-06 | 25 | Traducción ARN a Proteína con tabla de codones y búsqueda de motivos `find_motif` | Manejo de codón de parada (Stop '*') y offsets de posición 1-indexed vs 0-indexed |
| `R1-XUB-006` | 2026-08-06 | 25 | Script Python `fasta_n50.py`: parsear FASTA, acumular sumas y calcular N50/L50 | N50 es la longitud de contig donde el 50% del ensamblaje está contenido; L50 es el conteo mínimo de contigs |
| `R1-XUB-001` | 2026-08-07 | 50 | FastQC/MultiQC en `scratch/qc_test` y dictamen bioinformáticos sobre Phred Q30 | Distinguir artefactos de %GC/primers vs fallos reales de la celdilla de flujo Illumina |
| `R1-XUB-007` | 2026-08-07 | 50 | Script `clean_metadata.py`: estandarización `.str.lower()`, filtrado `dropna` y `groupby` | Preparación de samplesheets sin nulos ni incoherencias de texto para pipelines NGS |
| `R1-XUB-008` | 2026-08-07 | 25 | Claves SSH `WSL-AlmaLinux` y `PowerShell-Windows11` vinculadas en GitHub | Autenticación criptográfica ed25519 activa para push directo sin passwords |

**XP total actual:** 320  
**Rango:** I — Aprendiz de Terminal

Al cerrar cada ejercicio, actualiza esta fila, la sección **Estado Vivo** del Plan Maestro, la bitácora mensual y el commit quirúrgico correspondiente.
