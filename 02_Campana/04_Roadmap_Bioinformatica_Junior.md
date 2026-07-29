# 🗺️ ROADMAP GLOBAL — De Estudiante a Bioinformático Junior Empleado

> [!IMPORTANT]
> **Plan de empleabilidad acelerado · Ritmo full-time (vacaciones)**  
> **Objetivo:** Primer empleo junior (remoto o Ecuador) superando el base de $400, con proyección de crecimiento no atado a la economía local.  
> **Preparado para:** `cjalcivar@gmail.com` · **Fecha:** 27 de julio de 2026

---

## 📑 Tabla de Contenidos
- [0. Cómo leer este documento](#0-cómo-leer-este-documento)
- [1. La foto grande: qué debes dominar SÍ o SÍ](#1-la-foto-grande-qué-debes-dominar-sí-o-sí)

---

## 🧭 0. Cómo leer este documento

Este no es un temario académico. Es un mapa de empleabilidad: lo que un reclutador de bioinformática junior busca en 2026, ordenado por lo que de verdad mueve la aguja de una contratación. La universidad te da el fundamento (biología, genética, estadística); este roadmap te da lo que la malla casi no toca y que sin embargo decide si te llaman: código real, línea de comandos, pipelines reproducibles y un portafolio que se pueda abrir en GitHub.

> [!NOTE]
> **Dato de Mercado 2026:**  
> Una encuesta de 2026 reporta que el **68 % de los hiring managers** percibe una brecha grande entre la formación teórica y la destreza lista-para-el-trabajo de los recién graduados. Tu ventaja competitiva no será tu promedio: será demostrar que ya cruzaste esa brecha.

> [!TIP]
> **Trabajamos en dos carriles simultáneos:**
> - **Carril A — Universidad con doble propósito:** Las materias las estudiamos de forma que apruebes Y salga material de portafolio.
> - **Carril B — Empleabilidad (los tickets):** Simulación laboral que te hace contratable. Es el carril que genera el CV.

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 🔍 1. La foto grande: qué debes dominar SÍ o SÍ
Cruzando las vacantes junior remotas y de LatAm de 2026, el stack que se repite es sorprendentemente consistente. No necesitas dominar todo el universo bioinformático: necesitas dominar este núcleo y demostrarlo con proyectos. Divido en tres anillos por prioridad.
Anillo 1 — Innegociables (sin esto no pasas el filtro)
Competencia
Qué significa en la práctica
Distro
Python
pandas, numpy, biopython; automatizar análisis y parsear formatos (FASTA/FASTQ/VCF).
Xubuntu
Línea de comandos Linux
bash, pipes, grep/awk/sed, permisos, SSH. El 80 % del trabajo real vive aquí.
Xubuntu → Rocky
Git / GitHub
Versionar, ramas, commits limpios. Tu GitHub ES tu CV técnico.
Xubuntu
NGS básico
FASTQ→QC→alineamiento→variantes. Herramientas: FastQC, BWA/STAR, samtools, bcftools, GATK.
Xubuntu
Estadística aplicada
Distribuciones, pruebas de hipótesis, corrección de múltiples pruebas (FDR). Interpretar, no solo calcular.
Xubuntu
Anillo 2 — Lo que te separa del montón
Competencia
Por qué importa en 2026
Distro
Nextflow (DSL2)
DOMINA las ofertas de industria en 2026. Pipelines reproducibles en HPC/cloud. Es el skill 'de oro' junior.
Xubuntu → Rocky
Docker / Apptainer
Contenerizar pipelines que sobreviven a scans de seguridad y caídas de cluster. Ya casi es obligatorio.
Xubuntu → Rocky
R + Bioconductor
DESeq2/edgeR para RNA-seq, ggplot2. Competencia funcional basta al inicio.
Xubuntu
HPC / SLURM
Enviar jobs a un cluster, gestionar colas y recursos. Diferencia junior 'de laptop' vs 'de producción'.
Rocky Linux
Anillo 3 — Tu diferencial poco común
Seguridad de datos genómicos (hardening, permisos, cifrado, cumplimiento tipo HIPAA/GDPR para datos clínicos) en AthenaOS. Casi ningún junior lo trae. En un contexto de diagnóstico clínico —justo tu proyecto de biomarcadores en sangre— esto es un argumento de venta enorme: los datos de pacientes son sensibles y pocos candidatos junior saben protegerlos. No lo desarrollamos primero, pero lo reservamos como carta fuerte para entrevistas y para tu proyecto estrella.
2. Realidad del mercado (datos 2026)
Para que decidas con números, no con ilusión. Hay que separar dos mundos, porque tu salario dependerá de a cuál apuntes:
Vía
Rango típico
Qué implica
Local Ecuador (junior)
Supera con claridad el base de $400; objetivo realista de arranque.
Puerta de entrada, primera experiencia y referencias.
Remoto contratado en LatAm
Rango regional reportado ~US$69k–98k/año (varía mucho por empresa y seniority).
Salario en moneda/mercado local del empleador; el salto grande.
Remoto a estándar US
Entry-level ~US$71k–90k; algunas remotas igualan escala 'Boston'.
Muy competitivo; portafolio y Nextflow/Docker son la llave.
Lectura estratégica: tu primer empleo probablemente sea local o remoto-LatAm para romper el 'sin experiencia'. Pero el stack que construimos (Nextflow + Docker + portafolio en GitHub) es exactamente el que habilita el salto a remoto internacional en el segundo empleo. Por eso no bajamos el nivel técnico aunque el primer sueldo sea modesto: estás construyendo para el empleo #2 desde el #1.
Los rangos internacionales son referencias de EE. UU. y no representan el salario local en Ecuador; sirven para fijar la trayectoria, no la expectativa inmediata.
3. Tu 5.º semestre como cantera de portafolio
Tu idea es exactamente la correcta: hacer roleplay laboral sobre los sílabos que verás, para interiorizar los conceptos desde ya y pivotear a lo que da dinero. Aquí está el puente entre cada materia y la competencia empleable que le sacamos.
Materia (5.º sem)
Puente a bioinformática
Sale de portafolio
Ingeniería Genética
Diseño de constructos, edición, análisis de secuencias → manejo real de FASTA/GenBank, BLAST, primers in silico.
Script Python de análisis de secuencias
Genómica Estructural y Funcional
El corazón del NGS: ensamblado, anotación, expresión. Aquí vive RNA-seq y variant calling.
Pipeline RNA-seq / variant calling
Bioprocesos
Datos de proceso, optimización, series temporales → análisis de datos con Python/pandas y estadística.
Notebook de análisis de datos de proceso
Biología Funcional Animal y Vegetal
Contexto biológico para interpretar resultados ómicos (no confundir señal con ruido).
Interpretación en READMEs de proyectos
Bioproductos y Biodescubrimiento
Screening, cribado de compuestos → nociones de bases de datos biológicas y pipelines de búsqueda.
Consulta automatizada a bases públicas
Nota: no todas las materias del 5.º tienen el mismo peso para empleo. Genómica Estructural y Funcional e Ingeniería Genética son tus dos minas de oro; a esas les damos roleplay laboral intenso.
3-bis. Visión completa de la malla (4.º → 8.º + Integración)
Aquí está el mapa total, semestre por semestre. Cada materia la clasifico por su valor para tu objetivo de empleo en bioinformática, no por su valor académico. Uso tres etiquetas: MINA DE ORO (núcleo directo de tu carrera objetivo — exprímela al máximo), APOYO (da contexto o skill transversal útil) y CONTEXTO (apruébala bien, pero no le robes horas al portafolio). Recuerda: la biología te da el 'qué' interpretar; el código te da el empleo.
4.º semestre — ya cursado (tu base actual)
Ya lo pasaste; lo listo para que veas qué cimientos ya tienes y cuáles conviene reforzar por tu cuenta.
Materia
Valor empleo
Puente a bioinformática
Portafolio / skill
Bioinformática
MINA DE ORO
Tu materia homónima: fundamentos que debes tener sólidos sí o sí.
Repasar y reforzar
Probabilidad y Estadística
MINA DE ORO
Base para todo análisis de datos ómicos y para 'Estadística para Bioinformática' (7.º).
Python: numpy/scipy
Genética General
APOYO
Vocabulario y lógica biológica para interpretar variantes y expresión.
Contexto en READMEs
Técnicas Instrumentales
CONTEXTO
De dónde salen los datos (secuenciadores, espectrómetros). Útil para entender el origen del FASTQ.
—
Principios de Ing. Química
CONTEXTO
Aprobada (88). Fundamento de proceso; poco peso directo en bioinfo.
—
6.º semestre — el salto a datos
Materia
Valor empleo
Puente a bioinformática
Portafolio / skill
Base de Datos y Programación para Bioinformática
MINA DE ORO
LA materia clave de la malla para ti: SQL, estructuras de datos, programación aplicada. Es tu carrera objetivo con nombre y apellido.
Proyecto: BD genómica consultable + scripts
Proteómica y Metabolómica
APOYO
Datos ómicos más allá del ADN; pipelines de espectrometría, análisis multi-ómico (muy valorado en 2026).
Notebook de análisis ómico
Microbiología Industrial
CONTEXTO
Contexto de bioprocesos; datos de cultivos y fermentación.
Análisis de datos opcional
Biotecnología Vegetal
CONTEXTO
Aplicación; poco código directo.
—
Fund. de Agronomía y Fitopatología
CONTEXTO
Dominio agrícola; útil solo si apuntas a agro-biotech.
—
Regulación de la Biotecnología
APOYO
Marco legal/ético — conecta con tu diferencial de seguridad de datos clínicos.
Argumento de entrevista
7.º semestre — bioinformática pura y diagnóstico
Materia
Valor empleo
Puente a bioinformática
Portafolio / skill
Estadística para Bioinformática
MINA DE ORO
Estadística aplicada a datos biológicos: pruebas múltiples, modelos. Directo al corazón del análisis RNA-seq / expresión diferencial.
Análisis DESeq2/edgeR en R
Evolución Molecular y Filogenia
MINA DE ORO
Alineamientos múltiples, árboles filogenéticos — herramientas y algoritmos bioinformáticos clásicos y muy pedidos.
Pipeline filogenético
Diagnóstico Molecular
MINA DE ORO
Conecta DIRECTO con tu proyecto estrella de biomarcadores en sangre. Aplicación clínica real que da empleo en el sector salud.
Refuerza proyecto estrella
Bio-Nanotecnología
CONTEXTO
Frontera tecnológica; poco código bioinformático directo.
—
Sistemas de Gestión de Calidad
APOYO
ISO / buenas prácticas — valioso en farmacéutica y labs clínicos (reproducibilidad).
Argumento de entrevista
Biotecnología Agrícola
CONTEXTO
Dominio agro; nicho.
—
8.º semestre — modelado y especialización
Materia
Valor empleo
Puente a bioinformática
Portafolio / skill
Modelización de Sistemas y Estructuras Biológicas
MINA DE ORO
Biología de sistemas, modelado computacional, estructura de proteínas. Alta demanda y buen salario; conecta con IA/ML aplicado.
Proyecto de modelado computacional
Inmunología Aplicada
APOYO
Inmunoinformática es un nicho muy pagado (vacunas, anticuerpos); conecta con tu proyecto clínico.
Análisis inmuno-ómico opcional
Bioeconomía
CONTEXTO
Visión de negocio; útil para freelance/startup, no técnico.
—
Biotecnología Ambiental
CONTEXTO
Metagenómica ambiental si te interesa ese nicho.
Opcional: pipeline metagenómica
Mejoramiento Genético Vegetal
CONTEXTO
Genómica de plantas; nicho agro (GWAS, selección genómica).
Opcional: GWAS
Integración Curricular — tu titulación
5 créditos, proyecto final. Estrategia clave: haz que tu proyecto de titulación SEA tu proyecto estrella de portafolio (biomarcadores en sangre). Matas dos pájaros — te titulas Y tienes la pieza que impresiona a reclutadores, respaldada por tu universidad. No hagas dos proyectos distintos; funde el académico con el profesional.
Lectura estratégica de la malla completa
Tu carrera es afín pero no idéntica a 'bioinformática pura'. La malla tiene mucho de biotecnología aplicada (vegetal, agrícola, ambiental). Eso NO es malo: es tu contexto biológico. Pero el empleo lo dan las materias-código, que son pocas y debes exprimirlas.
Las 4 materias que deciden tu empleabilidad dentro de la malla: Base de Datos y Programación (6.º), Estadística para Bioinformática (7.º), Evolución Molecular y Filogenia (7.º) y Modelización de Sistemas (8.º). A esas les das todo.
Diagnóstico Molecular (7.º) es tu ancla clínica: alimenta directamente tu proyecto estrella de biomarcadores y te abre el sector salud, que paga bien.
Lo que la malla NO te dará y debes aprender por fuera (los tickets): Nextflow, Docker, Git profesional, HPC/SLURM y seguridad de datos. Ninguna materia los cubre y son justo los innegociables del mercado 2026.
★ Línea de CV/portafolio:  Formación en biotecnología con especialización en bioinformática (bases de datos, estadística aplicada, filogenia y modelado de sistemas biológicos), complementada con dominio autodidacta de pipelines reproducibles (Nextflow, Docker) y seguridad de datos genómicos.
4. El roadmap por fases
Ritmo full-time (~30–40 h/semana reales) durante vacaciones. Cuando reinicie el semestre, este mismo plan se reescala a medio tiempo. Cada fase termina con un entregable concreto en GitHub, porque un reclutador no lee tu plan: revisa tu repositorio.
Fase 0 — Cimientos (Semana 1–2)
Xubuntu como oficina diaria: terminal, Conda/mamba, entornos aislados por proyecto.
Python para datos: pandas, numpy, biopython. Git + primer repo público con README serio.
Refresco de línea de comandos hasta que sea reflejo (grep, awk, pipes, permisos).
★ Línea de CV/portafolio:  Configuré un entorno reproducible de bioinformática (Linux + Conda + Git) y publiqué mi primer repositorio con control de versiones.
Fase 1 — NGS de punta a punta (Semana 3–5)
QC de FASTQ (FastQC/MultiQC), trimming, alineamiento (BWA/STAR), samtools/bcftools.
Variant calling siguiendo GATK Best Practices (incluye SplitNCigarReads para RNA-seq). Este es el Ticket #001 y siguientes.
Interpretación biológica del resultado, no solo ejecutar comandos.
★ Línea de CV/portafolio:  Construí un pipeline NGS de extremo a extremo (FASTQ → QC → alineamiento → llamado de variantes) siguiendo GATK Best Practices, documentado en GitHub.
Fase 2 — Reproducibilidad de nivel industria (Semana 6–8)
Nextflow (DSL2): reescribir tu pipeline de la Fase 1 como workflow reproducible. Este es el salto que te separa del 'junior de laptop'.
Docker/Apptainer: contenerizar el pipeline para que corra en cualquier máquina.
Rocky Linux: llevar el pipeline a un entorno tipo cluster; nociones de SLURM.
★ Línea de CV/portafolio:  Refactoricé un pipeline NGS a Nextflow (DSL2) con contenedores Docker, ejecutable de forma reproducible en entornos HPC.
Fase 3 — Proyecto estrella: diagnóstico de biomarcadores en sangre (Semana 9–12)
Tu proyecto piloto con Claude Code se convierte en la pieza central del portafolio. Aquí converge todo: pipeline multilínea, contenerizado, con una capa de seguridad de datos (AthenaOS) por ser datos clínicos sensibles. Esto es lo que te hace memorable en una entrevista.
Pipeline multilínea reproducible (idea recomendada en tu proyecto Claude Code): ingesta → QC → alineamiento/cuantificación → selección de biomarcadores → reporte.
Capa diferencial (AthenaOS): permisos, cifrado en reposo, manejo seguro de datos de pacientes. Pocos juniors lo muestran.
README de nivel profesional: problema, datos, método, resultados, cómo reproducir. Es lo primero que lee un reclutador.
★ Línea de CV/portafolio:  Desarrollé un pipeline reproducible de diagnóstico de biomarcadores en sangre con manejo seguro de datos clínicos (cifrado y control de accesos), documentado para reproducibilidad.
Fase 4 — Postular en serio (transversal, desde la Semana 6)
No esperas a 'estar listo'. Cada 3–4 tickets hacemos una pausa para actualizar el CV real y postular a vacantes reales —aunque el stack no esté completo— para leer el mercado y practicar entrevistas. Rechazos tempranos = información gratis sobre qué te falta.
★ Línea de CV/portafolio:  Apliqué a N vacantes junior de bioinformática, obteniendo entrevistas y retroalimentación que orientó mi preparación técnica.
5. Cómo estudiamos: la dinámica de tickets
Cada 'ticket' es una tarea laboral real simulada. Rotamos entre lab académico, startup biotech, farmacéutica y freelance. Estructura fija de cada ticket:
Contexto: quién te escribe y por qué (para ambientarte en el rol real).
Cotización de mercado: cuánto valdría esa tarea, para que sepas lo que produces.
Resolución técnica paso a paso, juntos, en la distro que corresponda.
Una línea de CV/portafolio extraída al final.
Estado actual: Ticket #001 en Xubuntu — QC de FASTQ de sample_01: la calidad Phred cae bruscamente después de la posición 100/150, adapter content bajo, duplicación normal. Pendiente: tu recomendación (¿seguir a alineamiento o pedir re-secuenciación?) y qué paso técnico añadirías antes de continuar.
6. Qué hacemos esta semana (arranque inmediato)
Cerrar el Ticket #001: decidir el destino de sample_01 y el paso técnico previo (te guío en el razonamiento; hay una respuesta 'correcta' de la industria).
Montar la oficina en Xubuntu: Conda + entorno del proyecto + primer repo en GitHub.
Empezar Fase 1: correr un QC real end-to-end sobre datos de ejemplo públicos.
Regla de oro del plan: cada semana algo nuevo entra a tu GitHub. Sin repositorio no hay contratación; con repositorio, incluso incompleto, ya eres candidato.
Documento de trabajo · se actualiza al cerrar cada fase. Los rangos salariales internacionales son referenciales (EE. UU./LatAm) y no representan el salario local en Ecuador.