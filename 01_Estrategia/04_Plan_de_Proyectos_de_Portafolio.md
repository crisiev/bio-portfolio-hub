# 🚀 Documento 04 — Plan de Proyectos de Portafolio

> [!IMPORTANT]
> **Los repositorios de GitHub que demuestran tu stack completo · 2026**  
> *"El reclutador no lee tu plan: revisa tu repositorio. Construyamos los que lo hacen decir sí."*  
> **Preparado para:** `cjalcivar@gmail.com` · **Fecha:** 28 de julio de 2026

---

## 📑 Tabla de Contenidos
- [1. La filosofía: 5 repos que cubren todo el stack](#1--la-filosofía-5-repos-que-cubren-todo-el-stack)
- [2. Matriz de Proyectos vs. Stack](#2-matriz-de-proyectos-vs-stack)
- [3. Especificaciones de los Proyectos Núcleo](#3-especificaciones-de-los-proyectos-núcleo)

---

## 💡 1. La filosofía: 5 repos que cubren todo el stack

El reporte de mercado 2026 es directo: para graduarte y ser contratable necesitas 3–4 proyectos de producción en GitHub. Te propongo cinco núcleo (que forman una progresión natural) más dos diferenciales opcionales. Juntos cubren el 100 % del stack que el mercado llama “top 5 % de candidatos”: Python, NGS, Nextflow, Docker, cloud, CI/CD, ML con validación biológica y seguridad de datos.

> [!TIP]
> **El principio que gobierna tu portafolio:**  
> Cada proyecto termina cuando un extraño puede clonarlo, correrlo con un comando, y entender qué hace en 30 segundos leyendo el README. Si no cumple eso, no está listo para enlazar en tu CV.

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 📊 2. Matriz de Proyectos vs. Stack
1
Fundamentos + parser
Linux, Python, Git, Conda
I
2
Pipeline NGS variant calling
GATK, BWA, SAMtools, bcftools
II
3
Refactor a Nextflow + Docker + CI/CD
Nextflow DSL2, Docker, GitHub Actions
III
4
Despliegue en cloud
AWS Batch / GCP, S3, SLURM
IV
5
Proyecto estrella: biomarcadores
ML + seguridad + todo lo anterior
V + titulación
+
Diferenciales: single-cell · filogenia
Scanpy/Seurat · MAFFT/IQ-TREE
opcional
2 · Anatomía de un repo que contrata
Antes de los proyectos, la plantilla de calidad que aplicas a todos. Esto es lo que un reclutador técnico revisa en tu repositorio:
README profesional: problema → datos → método → resultados → cómo reproducir (comandos exactos). Con una figura o diagrama del pipeline.
Un comando para correr: nextflow run main.nf o bash run.sh. Nada de “instala 40 cosas a mano”.
Entorno declarado: environment.yml (Conda) o Dockerfile. Reproducibilidad = empleabilidad.
Datos de ejemplo o cómo obtenerlos: un subset pequeño en el repo o un script de descarga.
Commits limpios: mensajes reales (“add QC step for adapter trimming”), no “asdf” ni “fix”.
Tests + CI: aunque sea un test mínimo que GitHub Actions corra en cada push. El check verde impresiona.
Licencia + .gitignore: detalles de profesional. MIT es una elección segura.
Estructura de carpetas recomendada
proyecto/  ├─ README.md  ├─ main.nf (o src/)  ├─ Dockerfile  ├─ environment.yml  ├─ data/ (o download.sh)  ├─ results/ (ejemplo)  ├─ tests/  └─ .github/workflows/ci.yml
3 · Los proyectos, uno por uno
Cada ficha te da el objetivo, qué demuestra, qué datos usar, los pasos, el entregable y la línea de CV. Constrúyelos en orden: cada uno prepara el siguiente.
PROYECTO 1  Fundamentos + tu primer parser bioinformático
Tu carta de presentación técnica: demuestra que dominas el entorno (Linux, Conda, Git) y que escribes Python limpio sobre datos biológicos reales. Pequeño pero impecable.
Qué demuestra (skills para el CV)
Linux/CLI, entornos reproducibles (Conda/Mamba), Git/GitHub con commits limpios, Python (Biopython, pandas), lectura de formatos biológicos (FASTA/FASTQ).
Datos que puedes usar
Cualquier FASTA/FASTQ público pequeño (p. ej. un genoma bacteriano de NCBI, o reads de ejemplo de la documentación de FastQC).
Pasos / especificación
Monta un entorno Conda aislado (environment.yml) y un repo Git con README.
Escribe un script Python que parsee un FASTA y reporte: número de secuencias, longitudes, %GC, N50.
Añade una versión que procese un FASTQ: cuenta reads y calcula calidad Phred media por posición.
Genera un gráfico simple (matplotlib) de la distribución de longitudes o calidad.
Escribe un test con pytest y documenta cómo correrlo en el README.
Entregable + línea de CV
Repo: seq-stats — un CLI Python que reporta estadísticas de FASTA/FASTQ, con tests y README.
CV: “Herramienta CLI en Python (Biopython) para estadísticas de secuencias, con entorno reproducible (Conda), tests (pytest) y documentación.”
↳ Mapea a tu Campaña: Rango I — Aprendiz de Terminal (R1-XUB-001 a R1-BOSS-01).
PROYECTO 2  Pipeline NGS de variant calling (GATK Best Practices)
El corazón técnico que te hace “bioinformático de verdad”: de FASTQ a variantes anotadas, siguiendo las buenas prácticas de la industria.
Qué demuestra (skills para el CV)
NGS completo: QC (FastQC/MultiQC), trimming (fastp), alineamiento (BWA/STAR), SAMtools/BCFtools, variant calling (GATK HaplotypeCaller), anotación (SnpEff), interpretación biológica.
Datos que puedes usar
Subset de datos públicos: 1000 Genomes (una región cromosómica pequeña) o datos de ejemplo de nf-core/test-datasets. Usa un subset para que corra rápido.
Pasos / especificación
QC de los FASTQ (FastQC + MultiQC) y decide trimming con criterio (documenta la decisión).
Alinea contra un genoma de referencia (BWA para ADN) y procesa el BAM (sort, index, marcar duplicados).
Llama variantes con GATK HaplotypeCaller siguiendo Best Practices; filtra el VCF con bcftools.
Anota con SnpEff e interpreta: ¿qué variantes son relevantes y por qué?
Documenta cada paso y su justificación biológica en el README; incluye un MultiQC final.
Entregable + línea de CV
Repo: ngs-variant-calling — pipeline por scripts (bash/Python) FASTQ→VCF anotado, reproducible y documentado.
CV: “Pipeline NGS de extremo a extremo (FASTQ→QC→alineamiento→variant calling) siguiendo GATK Best Practices, con anotación funcional e interpretación.”
↳ Mapea a tu Campaña: Rango II — Domador de Secuencias (R2-XUB-001 a R2-BOSS-01).
PROYECTO 3  Refactor a Nextflow + Docker + CI/CD
El salto que separa al “junior de laptop” del profesional de producción. Conviertes el Proyecto 2 en un workflow reproducible que corre igual en cualquier máquina — y lo pruebas automáticamente.
Qué demuestra (skills para el CV)
Nextflow (DSL2), contenedores (Docker/Apptainer), parametrización y config, CI/CD (GitHub Actions), reproducibilidad de nivel industria. Este es el skill de oro más pedido en 2026.
Datos que puedes usar
Los mismos del Proyecto 2 (reutilizas). Añade un dataset de prueba mínimo para que el CI corra en segundos.
Pasos / especificación
Reescribe el pipeline del Proyecto 2 como Nextflow DSL2: procesos, canales, nextflow.config.
Escribe un Dockerfile que empaquete todas las herramientas; corre el pipeline dentro del contenedor.
Parametriza (entradas, referencia, recursos) para que sea reutilizable, no hardcodeado.
Añade un GitHub Actions que ejecute el pipeline sobre el dataset de prueba en cada push (check verde).
Convierte a Apptainer para HPC y documenta cómo lanzarlo en un cluster con SLURM.
Entregable + línea de CV
Repo: ngs-nextflow — el pipeline del P2 como Nextflow + Docker, con CI/CD que pasa en verde.
CV: “Refactoricé un pipeline NGS a Nextflow (DSL2) con contenedores Docker/Apptainer y CI/CD (GitHub Actions), ejecutable de forma reproducible en HPC.”
↳ Mapea a tu Campaña: Rango III — Arquitecto de Flujos (R3-XUB-001 a R3-BOSS-01).
PROYECTO 4  Despliegue en la nube (AWS Batch / S3 + Single-Cell)
El diferencial que en 2026 pasó de “deseable” a filtro: correr tu pipeline en la nube bajo demanda e integrar análisis Single-Cell (scRNA-seq).
Qué demuestra (skills para el CV)
Cloud (AWS S3 + Batch), IAM políticas de acceso, Seqera Platform (Nextflow Tower), scRNA-seq (Scanpy), estimación y control de costos, anonimización clínica (HIPAA/GDPR).
Datos que puedes usar
Dataset público de Single-Cell (ej. PBMC 3k o 10x Genomics) procesado con Nextflow y subido a AWS S3.
Pasos / especificación
Sube los datos a un bucket S3 con políticas de acceso IAM de mínimo privilegio.
Configura Nextflow para ejecutar en AWS Batch con monitoreo en Seqera Platform.
Procesa scRNA-seq con Scanpy: filtrado, PCA/UMAP, clustering (Leiden) y marker genes.
Documenta costo y tiempo de ejecución: “procesó N muestras en X min por ~$Y”.
Entregable + línea de CV
Repo/README: ngs-aws-singlecell — pipeline Nextflow en AWS Batch para scRNA-seq con benchmarking de costo y privacidad clínica.
CV: “Desplegué un pipeline scRNA-seq en AWS Batch (S3 + IAM) con monitoreo en Seqera Platform y anonimización clínica.”
↳ Mapea a tu Campaña: Rango IV — Guardián Cloud & Single-Cell Genomics (R4-SCRNA-001..003, R4-AWS-001..002, R4-CLIN-001).
PROYECTO 5 ★  Proyecto estrella: diagnóstico de biomarcadores multi-ónicos
Tu pieza central y tu proyecto de titulación fundido en uno. Aquí converge todo: pipeline multi-ómico (Bulk + scRNA-seq), contenerizado en Nextflow/Docker, desplegado en AWS, con figuras de nivel de publicación en R (Bioconductor, ComplexHeatmap) y ML aplicado simple.
Qué demuestra (skills para el CV)
Todo lo anterior + R/Bioconductor (ComplexHeatmap, clusterProfiler) + ML aplicado con validación biológica (scikit-learn, AUC-ROC) + comunicación de resultados en inglés.
Datos que puedes usar
Datos públicos de expresión/variantes asociados a una condición (p. ej. GEO, TCGA-subset). Elige un caso donde puedas seleccionar biomarcadores y clasificar muestras.
Pasos / especificación
Diseña la arquitectura end-to-end: ingesta → QC → alineamiento/cuantificación → selección de biomarcadores → clasificación → reporte.
Implementa el módulo de ML: selección de features, entrenamiento, validación cruzada, métricas clínicas (AUC-ROC, precisión/recall). Evita fuga de datos.
Añade la capa de seguridad (tu diferencial): cifrado en reposo (LUKS/GPG), control de accesos, anonimización del dataset.
Empaqueta todo en Nextflow + Docker; ejecútalo en cloud (reutilizas P3–P4).
Escribe un README de nivel profesional: problema, datos, método, resultados (con figuras), cómo reproducir, y consideraciones éticas/regulatorias.
Prepara un pitch de 60 segundos y una defensa de 10 min (sirve para el tribunal Y para la entrevista técnica).
Entregable + línea de CV
Repo estrella: blood-biomarker-dx — el pipeline completo con ML, seguridad y documentación de nivel profesional.
CV: “Desarrollé un pipeline reproducible de diagnóstico de biomarcadores en sangre (Nextflow + Docker, ejecutado en cloud) con módulo de ML validado (AUC-ROC) y una capa de seguridad de datos clínicos (cifrado, control de accesos).”
↳ Mapea a tu Campaña: Rango V — Cazador Multi-Ómico & El Dragón (R5-ALL-001 a R5-BOSS-01) + Integración Curricular.
DIFERENCIAL A  Mini-proyecto de single-cell (scRNA-seq)
Single-cell pasó a demanda caliente y bien pagada en 2026, y pocos juniors lo muestran. Un mini-proyecto te distingue visiblemente.
Qué demuestra (skills para el CV)
scRNA-seq: Scanpy (Python) o Seurat (R), control de calidad de células, normalización, reducción de dimensionalidad (PCA/UMAP), clustering, marcadores por cluster.
Datos que puedes usar
Datasets de ejemplo de Scanpy/Seurat (PBMC 3k es el clásico) o de 10x Genomics.
Pasos / especificación
QC de células (filtrar por genes/mitocondrial), normaliza y escala.
Reduce dimensionalidad (PCA → UMAP) y haz clustering (Leiden).
Identifica marcadores por cluster y anota tipos celulares; interpreta biológicamente.
Documenta con figuras (UMAP coloreado por cluster/tipo celular).
Entregable + línea de CV
Repo: scrna-pbmc — notebook/pipeline de análisis single-cell con anotación de tipos celulares.
CV: “Análisis single-cell (scRNA-seq) con Scanpy: QC, clustering (Leiden/UMAP) y anotación de tipos celulares.”
DIFERENCIAL B  Pipeline de filogenia molecular
Conecta con tu materia de Evolución Molecular y con salud pública/virología. Un algoritmo bioinformático clásico, muy pedido, empaquetado limpio.
Qué demuestra (skills para el CV)
Alineamiento múltiple (MAFFT), reconstrucción filogenética (IQ-TREE), soporte por bootstrap, interpretación de árboles y selección (dN/dS).
Datos que puedes usar
Secuencias de un gen viral (p. ej. de NCBI Virus) de varias cepas/regiones.
Pasos / especificación
Descarga automatizada de secuencias (Biopython/E-utilities).
Alineamiento múltiple con MAFFT; construcción del árbol con IQ-TREE + bootstrap.
Genera una figura del árbol anotada y discútela.
Empaqueta el flujo completo como script/Nextflow reproducible.
Entregable + línea de CV
Repo: phylo-pipeline — descarga→MSA→árbol→figura, reproducible.
CV: “Pipeline de filogenia molecular (MAFFT + IQ-TREE) con soporte por bootstrap, aplicado a genómica de patógenos.”
4 · Datasets públicos recomendados
Todo lo anterior corre con datos abiertos y gratuitos. Usa siempre subsets pequeños para que tus pipelines corran rápido (y tu CI también).
Fuente
Qué tiene
Para qué proyecto
nf-core/test-datasets
Datos mínimos de prueba para pipelines NGS.
P2, P3 (ideal para CI).
1000 Genomes
Variantes y reads humanos públicos.
P2, P5 (usa una región pequeña).
NCBI SRA / GenBank
Reads crudos y secuencias de todo tipo.
P1, P2, Diferencial B.
GEO / ArrayExpress
Datos de expresión (RNA-seq, microarrays).
Estadística, P5.
10x Genomics / Scanpy datasets
Datos single-cell de ejemplo (PBMC 3k).
Diferencial A.
TCGA (subset)
Datos genómicos de cáncer.
P5 (biomarcadores).
NCBI Virus
Secuencias virales por cepa/región.
Diferencial B (filogenia).
5 · Orden de construcción y ritmo
No construyas todo a la vez. Sigue la escalera: cada proyecto reutiliza al anterior, así que el esfuerzo se compone en vez de repetirse.
Semanas 1–2: Proyecto 1 (fundamentos). Cierra el Rango I de tu Campaña.
Semanas 3–5: Proyecto 2 (NGS variant calling). Rango II.
Semanas 6–8: Proyecto 3 (Nextflow + Docker + CI/CD). Rango III. Aquí ya eres candidato serio.
Semanas 9–10: Proyecto 4 (cloud). Rango IV. Cierras el filtro cloud de 2026.
Semanas 11–13: Proyecto 5 (estrella + titulación). Rango V. Empieza a postular en paralelo.
Cuando puedas: un diferencial (single-cell o filogenia) para destacar del montón.
Empieza a postular en la semana 6, no en la 13
Con los Proyectos 1–3 ya eres candidato. Postula aunque el stack no esté completo: cada rechazo es información gratis sobre qué te falta, y cada entrevista es práctica para el “Dragón”. No esperes a sentirte listo — el mercado te dirá cuándo lo estás.
6 · Checklist: “listo para enlazar en el CV”
Antes de poner un repo en tu CV o LinkedIn, que cumpla TODO esto. Si falla uno, aún no está listo:
README con problema, método, resultados y comandos exactos de reproducción.
Se clona y corre con un solo comando en una máquina limpia.
Entorno declarado (Conda/Docker). Sin “instala esto a mano”.
Commits con mensajes reales. Historia limpia.
Al menos un test y, si aplica, CI en verde.
Una figura o diagrama que comunique el resultado de un vistazo.
Licencia y .gitignore presentes.
El cierre de todo
Estos cuatro documentos + tu sistema de Campaña son tu equipo completo: sabes qué pide el mercado, cuánto pedir, qué estudiar, cómo venderte y qué construir. Lo único que falta ahora no se escribe: se ejecuta. Cada semana, un commit nuevo. Nos vemos en el Rango I.