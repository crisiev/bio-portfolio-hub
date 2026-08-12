# Registro de Campaña — Progreso y XP

> [!IMPORTANT]
> Este archivo registra el progreso real. El inventario, orden de ejecución y horas viven exclusivamente en [`PLAN_MAESTRO.md`](../PLAN_MAESTRO.md); no se duplican aquí para evitar divergencias.

## Estado actual

| Campo | Valor |
|---|---|
| Rango actual | I — Aprendiz de Terminal |
| XP actual | 445 |
| Último ejercicio cerrado | `R1-XUB-011` — Script Bash automatizado para QC de muestras en lote + auditoría Q30 |
| Próximo ejercicio | `R1-BOSS-01` — ☠ **EL REPOSITORIO FANTASMA** (Auditoría Hostil de Portafolio) |
| Siguiente bloque | Semana 4 Día 1 |

> El orden cronológico lo define el calendario del Plan Maestro, no la numeración del ticket. Por eso el primer ejercicio fue `R1-XUB-002`.

## Tablero de campaña

| Rango | Unidades | XP al cerrar | Estado |
|---|---:|---:|---|
| I — Aprendiz de Terminal | 15 ejercicios + 1 jefe | 600 | En curso (445 / 600 XP) |
| II — Domador de Secuencias | 11 ejercicios + 1 jefe | 650 | Bloqueado hasta Rango I |
| III — Arquitecto de Flujos | 11 ejercicios + 1 jefe | 825 | Bloqueado hasta Rango II |
| IV — Guardián de Datos | 10 ejercicios + 1 jefe | 875 | Bloqueado hasta Rango III |
| V — Cazador de Dragones | 9 ejercicios + 1 jefe | 900 | Bloqueado hasta Rango IV |
| **Total** | **56 ejercicios + 5 jefes** | **3,850** | — |

## Bitácora de progreso

| Código | Fecha de cierre | XP | Evidencia verificable | Cicatriz / aprendizaje |
|---|---|---:|---|---|
| `R1-ROSA-03` | 2026-08-06 | 25 | Traducción ARN a Proteína con tabla de codones y búsqueda de motivos `find_motif` | Manejo de codón de parada (Stop '*') y offsets de posición 1-indexed vs 0-indexed |
| `R1-XUB-006` | 2026-08-06 | 25 | Script Python `fasta_n50.py`: parsear FASTA, acumular sumas y calcular N50/L50 | N50 es la longitud de contig donde el 50% del ensamblaje está contenido; L50 es el conteo mínimo de contigs |
| `R1-XUB-001` | 2026-08-07 | 50 | FastQC/MultiQC en `scratch/qc_test` y dictamen bioinformáticos sobre Phred Q30 | Distinguir artefactos de %GC/primers vs fallos reales de la celdilla de flujo Illumina |
| `R1-XUB-007` | 2026-08-07 | 50 | Script `clean_metadata.py`: estandarización `.str.lower()`, filtrado `dropna` y `groupby` | Preparación de samplesheets sin nulos ni incoherencias de texto para pipelines NGS |
| `R1-XUB-008` | 2026-08-07 | 25 | Claves SSH `WSL-AlmaLinux` y `PowerShell-Windows11` vinculadas en GitHub | Autenticación criptográfica ed25519 activa para push directo sin passwords |
| `R1-XUB-009` | 2026-08-09 | 50 | Paquete `src/seq_stats/`, CLI `cli.py` y suite `pytest` verificada en verde (`4 passed`) | La separación de la interfaz CLI respecto a la lógica pura permite la reutilización e inmunidad de tests |
| `R1-XUB-012` | 2026-08-09 | 25 | Perfil `crisiev/crisiev` activo en GitHub con badges, métricas y repos destacados | El Profile README es la tarjeta de presentación #1 evaluada por reclutadores técnicos en 2026 |
| `R1-XUB-011` | 2026-08-09 | 50 | Script `scripts/auto_qc.sh` e integración con `scripts/audit_qc.py` parseando JSON | La combinación de orquestación Shell con parsing CPython permite crear pipelines autónomos con decisión de paso/fallo |
| `R1-BOSS-01` | 2026-08-10 | 250 | Clean Architecture `src/seq_stats/`, `pytest.ini`, `environment.yml` declarativo y commit `a993d83` | La victoria en la auditoría hostil depende de la reproducibilidad 1-click y la suite de pruebas unitarias al 100% |
| `R2-XUB-002` | 2026-08-10 | 25 | Descarga e indexación del genoma de referencia *E. coli* con Transformada de Burrows-Wheeler (`bwa index`) | Conocer la estructura interna del FM-index evita errores críticos de despliegue en HPC al alinear FASTQs masivos |
| `R2-XUB-003` | 2026-08-11 | 55 | Alineamiento NGS con `bwa mem`, conversión a BAM y QC de mapeo con `samtools flagstat` | Manejar la conversión texto-binario (SAM/BAM) es fundamental para evitar cuellos de botella de I/O en bioinformática |

**XP total actual:** 800  
**Rango:** II — Domador de Secuencias (DESBLOQUEADO ⚔️)

Al cerrar cada ejercicio, actualiza esta fila, la sección **Estado Vivo** del Plan Maestro, la bitácora mensual y el commit quirúrgico correspondiente.
