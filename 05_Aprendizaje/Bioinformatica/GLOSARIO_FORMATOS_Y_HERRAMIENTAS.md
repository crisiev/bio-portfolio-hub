# 🧬 Glosario Maestro: Formatos, Herramientas y Pipelines NGS

> [!IMPORTANT]
> **Fuente de Verdad de Conceptos Técnicos** en Bioinformática y Secuenciación de Nueva Generación (NGS).
> Este documento centraliza las definiciones, anatomía de archivos y flujos de trabajo para repaso continuo, preparación de exámenes universitarios y entrevistas técnicas.

---

## 📑 Tabla de Contenidos
- [1. El Flujo de Datos Genómicos (Pipeline E2E)](#1-el-flujo-de-datos-genómicos-pipeline-e2e)
- [2. Formatos de Archivos Fundamentales](#2-formatos-de-archivos-fundamentales)
  - [FASTQ (Lecturas Crudas + Calidad Phred)](#fastq-lecturas-crudas--calidad-phred)
  - [FASTA (Secuencias Biológicas)](#fasta-secuencias-biológicas)
  - [SAM / BAM (Lecturas Alineadas al Genoma)](#sam--bam-lecturas-alineadas-al-genoma)
  - [VCF (Llamada de Variantes y Mutaciones)](#vcf-llamada-de-variantes-y-mutaciones)
  - [GFF / GTF (Anotación de Genes y Estructura Genómica)](#gff--gtf-anotación-de-genes-y-estructura-genómica)
- [3. Herramientas y Orquestadores de Producción](#3-herramientas-y-orquestadores-de-producción)
  - [FastQC & MultiQC (Control de Calidad)](#fastqc--multiqc-control-de-calidad)
  - [Nextflow & Snakemake (Workflow Management Systems)](#nextflow--snakemake-workflow-management-systems)
  - [Rosalind (Algoritmos y Práctica de Código)](#rosalind-algoritmos-y-práctica-de-código)

---

## 🔄 1. El Flujo de Datos Genómicos (Pipeline E2E)

En bioinformática, los datos transitan secuencialmente por formatos y herramientas específicas desde el secuenciador hasta la variante clínica:

```mermaid
graph TD
    A[Muestra Biológica / ADN / ARN] --> B[Secuenciador Illumina / PacBio / Nanopore]
    B --> C[Archivos FASTQ: Lecturas + Phred Scores]
    C --> D[FastQC / MultiQC: Control de Calidad]
    D --> E[Nextflow / Snakemake: Orquestador del Pipeline]
    E --> F[BWA / STAR: Alineamiento al Genoma de Referencia]
    F --> G[Archivos SAM / BAM: Secuencias Mapeadas]
    G --> H[GATK HaplotypeCaller / bcftools: Variant Calling]
    H --> I[Archivos VCF: Variantes y Mutaciones SNP/Indel]
    J[Archivos GFF / GTF: Anotación de Genes] -. Cruce de Coordenadas .-> G
```

---

## 📄 2. Formatos de Archivos Fundamentales

### FASTQ (Lecturas Crudas + Calidad Phred)
- **Qué es:** Formato estándar de salida de secuenciadores. Grupos estStrictos de 4 líneas por lectura.
- **Estructura:**
  - Línea 1: `@Header` (ID del secuenciador, flowcell, coordenadas de cluster).
  - Línea 2: Secuencia de nucleótidos (`ATCGN`).
  - Línea 3: `+` (Separador).
  - Línea 4: Caracteres ASCII Phred+33 ($Q = -10 \log_{10} P$).

### FASTA (Secuencias Biológicas)
- **Qué es:** Formato de texto simple para secuencias de ADN, ARN o proteínas (referencias genómicas, contigs).
- **Estructura:**
  - Línea 1: `>Header` (Nombre del cromosoma, contig o proteína).
  - Líneas siguientes: Cadena continua de nucleótidos o aminoácidos.

### SAM / BAM (Lecturas Alineadas al Genoma)
- **Qué es:** Contiene las lecturas del FASTQ mapeadas con coordenadas sobre un genoma de referencia.
- **Diferencia SAM vs BAM:**
  - **SAM (Sequence Alignment Map):** Texto plano legible por humanos.
  - **BAM (Binary Alignment Map):** Versión binaria comprimida e indexada para búsqueda rápida (`samtools`).

### VCF (Llamada de Variantes y Mutaciones)
- **Qué es:** Formato estándar para almacenar mutaciones y variaciones genéticas (SNPs, Indels, SVs) detectadas en un individuo.
- **Campos clave:** `CHROM`, `POS`, `ID`, `REF` (base de referencia), `ALT` (base mutada), `QUAL` (confianza Phred), `FILTER`, `INFO`, `FORMAT`, `SAMPLE`.

### GFF / GTF (Anotación de Genes y Estructura Genómica)
- **Qué es:** Formato tabulado de 9 columnas que define las coordenadas biológicas de elementos del genoma (genes, exones, intrones, promotores, UTRs).
- **Uso:** Permite saber en qué gen o región funcional cae una variante VCF o una lectura BAM.

### PDB & mmCIF (Estructuras Macromoleculares 3D)
- **PDB (.pdb):** Formato histórico de coordenadas atómicas en 3D ($X, Y, Z$) de proteínas, ácidos nucleicos y ligandos resueltos por Rayos X, RMN o Cryo-EM.
- **mmCIF (.cif):** Estándar moderno del PDB para estructuras gigantescas (complejos ribosomales) sin límite de 99,999 átomos ni 62 cadenas.

### SDF & SMILES (Formatos Químicos de Moléculas y Fármacos)
- **SMILES (Simplified Molecular Input Line Entry System):** Notación de texto de una línea para estructuras químicas (ej. Cafeína: `CN1C=NC2=C1C(=O)N(C(=O)N2C)C`).
- **SDF / MOL2 (.sdf, .mol2):** Formato con coordenadas espaciales 3D, enlaces, órdenes de enlace y cargas parciales de ligandos y fitocompuestos.

---

## 🛠️ 3. Herramientas y Orquestadores de Producción

### FastQC & MultiQC (Control de Calidad)
- **FastQC:** Diagnostica la salud de un archivo FASTQ ($Q$-scores per base, adaptadores Illumina, contenido %GC).
- **MultiQC:** Consolida múltiples reportes de FastQC en una sola interfaz interactiva `.html`.

### Nextflow & Snakemake (Workflow Management Systems)
- **Nextflow:** Orquestador DSL2 dominante en la industria clínica y farmacéutica (comunidad `nf-core`). Ejecuta pipelines reproducibles conectando Docker, Apptainer, SLURM y Cloud AWS/GCP.
- **Snakemake:** Orquestador basado en sintaxis Python, ampliamente utilizado en investigación académica y análisis de datos genómicos.

### Rosalind (`rosalind.info`)
- **Plataforma de algoritmos:** Entorno de problemas bioinformáticos para dominar manipulación de cadenas, estructuras de datos y lógica biológica en Python.

---

## ⚛️ 4. Herramientas de CADD, Biofísica e IA Estructural

### Boltz-1 & Boltz-2 (Foundation Model de Co-folding & Afinidad)
- **Mecanismo:** Modelo abierto (MIT) de co-folding multimodal (Proteína-Ligando-Ácidos Nucleicos). Boltz-2 predice afinidad de unión (*binding affinity* $\Delta G / K_d$).
- **Uso:** Cribado de fármacos y metabolitos sin restricciones de licencia comercial.

### DiffDock / DynamicBind (Docking Generativo con Difusión)
- **Mecanismo:** Modelos de difusión sobre el grupo euclidiano $SE(3)$ para acoplar ligandos flexibles en cavidades proteicas inducidas (*induced fit*).

### RDKit (Quimioinformática en Python)
- **Mecanismo:** Librería estándar para calcular descriptores fisicoquímicos (LogP, TPSA, peso molecular), fingerprints moleculares (Morgan/ECFP4) y similitud química (Tanimoto).

### OpenMM & GROMACS (Dinámica Molecular y Biofísica)
- **OpenMM:** Motor de dinámica molecular acelerado por GPU con API nativa en Python (`import openmm`), ideal para automatizar pipelines.
- **GROMACS:** Motor de alto rendimiento en C++/CUDA para simulación masiva de estabilidad conformacional, solvatación explícita y análisis RMSD/RMSF en clusters HPC/SLURM.

---

## 🏛️ 5. Bases de Datos de Farmacogenómica, Fitoquímica y Metaboloma

* **CPIC & PharmGKB:** Guías de dosificación clínica basadas en genotipo y alelos estrella (*Star Alleles* en citocromos $CYP2D6, CYP2C19$).
* **HMDB (Human Metabolome Database):** Enciclopedia de más de 200,000 metabolitos humanos y sus rangos fisiológicos en sangre y orina.
* **COCONUT Database & FooDB:** Repositorios abiertos de metabolitos secundarios de plantas, fitocompuestos y alimentos bioactivos.
* **ChEMBL & PubChem:** Bases de datos de bioactividad molecular, afinidades de unión ($IC_{50}, K_i$) y propiedades farmacológicas.

---

*Glosario vivo. Se actualiza al incorporar nuevos formatos o herramientas durante La Campaña.*
