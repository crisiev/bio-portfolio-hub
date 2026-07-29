# 💾 Directorio de Datos — Ecosistema empleoBio

> [!IMPORTANT]
> **Estándar de gestión de datos genómicos y clínicos.**  
> Los datos pesados (`.fastq`, `.bam`, `.vcf`) están excluidos del control de versiones mediante `.gitignore` para mantener el repositorio liviano y rápido.

---

## 🗂️ Estructura de Subcarpetas

- **`raw/`**: Datos crudos sin procesar (archivos FASTQ descargados o simulados). Ignorados por Git.
- **`processed/`**: Salidas intermedias (archivos BAM filtrados, VCFs anotados, matrices de expresión). Ignorados por Git.
- **`reference/`**: Genomas de referencia (FASTA, GTF/GFF). Ignorados por Git.

> [!TIP]
> Cada subcarpeta contiene un archivo `.gitkeep` para preservar la estructura del directorio en GitHub sin subir los datasets pesados.
