# Registro de Campaña — Progreso y XP

> [!IMPORTANT]
> Este archivo registra el progreso real. El inventario, orden de ejecución y horas viven exclusivamente en [`PLAN_MAESTRO.md`](../PLAN_MAESTRO.md); no se duplican aquí para evitar divergencias.

## Estado actual

| Campo | Valor |
|---|---|
| Rango actual | I — Aprendiz de Terminal |
| XP actual | 35 |
| Último ejercicio cerrado | `R1-XUB-003` — Navegar dataset genómico por terminal |
| Próximo ejercicio | `R1-XUB-004` — Inspeccionar FASTQ gigante sin abrirlo |
| Siguiente bloque | `R1-XUB-005` (grep/awk) + Checklist BioSocial Tarea 5 |

> El orden cronológico lo define el calendario del Plan Maestro, no la numeración del ticket. Por eso el primer ejercicio fue `R1-XUB-002`.

## Tablero de campaña

| Rango | Unidades | XP al cerrar | Estado |
|---|---:|---:|---|
| I — Aprendiz de Terminal | 15 ejercicios + 1 jefe | 600 | En curso (35 / 600 XP) |
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

**XP total actual:** 35  
**Rango:** I — Aprendiz de Terminal

Al cerrar cada ejercicio, actualiza esta fila, la sección **Estado Vivo** del Plan Maestro, la bitácora mensual y el commit quirúrgico correspondiente.
