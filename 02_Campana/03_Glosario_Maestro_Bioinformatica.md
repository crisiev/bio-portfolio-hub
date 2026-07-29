# 📖 GLOSARIO MAESTRO — Temario Técnico & de Carrera

> [!IMPORTANT]
> **Documento-pivote · Se lee al inicio de cada chat de la dinámica de tickets**  
> Todo lo que debes llegar a dominar para el arbitraje geográfico: sueldo internacional, costos de Ecuador, capital para la startup.  
> **Preparado para:** `cjalcivar@gmail.com` · **Fecha:** 27 de julio de 2026

---

## 📑 Tabla de Contenidos
- [1. Cómo usar este documento](#1-cómo-usar-este-documento)
- [2. Dominio 1 — Sistema Operativo y CLI](#dominio-1--sistema-operativo-y-línea-de-comandos)

---

## 🧭 1. Cómo usar este documento

Este es tu mapa de conocimiento y archivo de continuidad. Tiene dos funciones:
1. **Temario de maestría:** Todo lo que debes llegar a dominar, agrupado por dominios. Recórrelo y marca tu nivel conforme avanzas.
2. **Pivote entre chats:** Al abrir un chat nuevo, dime qué dominio/skill quieres entrenar y montamos un ticket laboral simulado (situación real pagada) sobre eso.

> [!NOTE]
> **Etiquetas de Prioridad:**
> - 🔴 `[INNEGOCIABLE]` — Sin esto no pasas el filtro de un reclutador internacional.
> - 🟡 `[DIFERENCIAL]` — Lo que te separa del montón y justifica cobrar más.
> - 🟢 `[APOYO]` — Te da contexto, robustez o argumento de venta; útil pero no bloqueante.

> [!TIP]
> **Regla que gobierna todo:**  
> No memorizas conceptos para un examen; **los conviertes en algo que corre en tu GitHub**. La maestría se demuestra con un repositorio, no con una lista marcada. Este glosario te dice QUÉ dominar; los tickets te hacen DEMOSTRARLO.

> [!IMPORTANT]
> **Los tres niveles de maestría que perseguimos:**
> 1. **Fundamentos:** Entiendes el concepto y puedes seguir un tutorial.
> 2. **Trabajo:** Lo usas solo en un proyecto real sin guía paso a paso.
> 3. **Maestría:** Lo enseñas, lo depuras cuando falla, y lo defiendes en una entrevista técnica.

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 💻 Dominio 1 — Sistema operativo y línea de comandos
El 80% del trabajo real de bioinformática vive en la terminal de Linux. Esto es tu oficina (Xubuntu), tu producción (Rocky) y tu seguridad (AthenaOS). Si no te mueves con fluidez aquí, todo lo demás cojea.
Shell / Bash [INNEGOCIABLE]
Qué es: El intérprete de comandos donde escribes órdenes al sistema. Scripts .sh que automatizan tareas repetitivas.
Por qué te pagan: Automatizar = hacer en segundos lo que a otros toma horas. Es la base de todo pipeline.
Navegación y archivos (cd, ls, cp, mv, rm, find) [INNEGOCIABLE]
Qué es: Moverte, copiar, mover, borrar y encontrar archivos sin ratón.
Por qué te pagan: Manejas datasets de gigas donde no hay interfaz gráfica; solo terminal.
Pipes y redirección (| > >> <) [INNEGOCIABLE]
Qué es: Encadenar la salida de un comando como entrada de otro; guardar salidas en archivos.
Por qué te pagan: Es cómo construyes pipelines de datos sin escribir un solo programa completo.
grep / awk / sed [INNEGOCIABLE]
Qué es: Trío para buscar, filtrar y transformar texto/tablas gigantes línea por línea.
Por qué te pagan: Los archivos biológicos (FASTQ, VCF, GTF) son texto enorme; esto los dobla a tu voluntad.
Permisos y usuarios (chmod, chown) [INNEGOCIABLE]
Qué es: Controlar quién puede leer/escribir/ejecutar cada archivo.
Por qué te pagan: Base de la seguridad de datos: datos de pacientes mal permitidos = brecha legal.
SSH y trabajo remoto [INNEGOCIABLE]
Qué es: Conectarte de forma segura a servidores y clusters remotos desde tu máquina.
Por qué te pagan: El cómputo pesado no corre en tu laptop; corre en servidores a los que entras por SSH.
Gestión de procesos (top, htop, kill, &, nohup) [APOYO]
Qué es: Ver, priorizar y matar procesos; correr trabajos en segundo plano.
Por qué te pagan: Un análisis puede tardar horas; debes lanzarlo y que sobreviva aunque cierres sesión.
tmux / screen [APOYO]
Qué es: Sesiones de terminal persistentes que no mueren al desconectar.
Por qué te pagan: Trabajo remoto profesional: dejas un análisis corriendo y vuelves mañana.
Dominio 2 — Programación
Aquí está el cruce que más paga: bioinformática + ingeniería de software. El biólogo que pipetea no cobra internacional; el que construye software sobre datos biológicos sí. Python es tu lenguaje principal; R tu segundo idioma.
Python (tu lenguaje principal)
Fundamentos de Python [INNEGOCIABLE]
Qué es: Variables, tipos, control de flujo, funciones, estructuras (listas, dicts), manejo de archivos y errores.
Por qué te pagan: Es el lenguaje #1 de bioinformática; todo lo demás se construye encima.
pandas [INNEGOCIABLE]
Qué es: Librería para manipular tablas de datos (filtrar, agrupar, unir, transformar) como en Excel pero a escala.
Por qué te pagan: El 90% del análisis de datos es limpiar y reordenar tablas; pandas es cómo.
NumPy [INNEGOCIABLE]
Qué es: Cálculo numérico rápido sobre arreglos y matrices.
Por qué te pagan: Base de rendimiento para cualquier cómputo científico serio.
Biopython [INNEGOCIABLE]
Qué es: Librería específica para parsear FASTA/FASTQ/GenBank, manejar secuencias, consultar bases.
Por qué te pagan: Te ahorra reinventar la rueda con los formatos biológicos estándar.
Matplotlib / Seaborn [APOYO]
Qué es: Graficar resultados: distribuciones, calidad, expresión.
Por qué te pagan: Un análisis sin visualización no comunica; el cliente compra el gráfico, no el CSV.
Entornos virtuales (venv, Conda/mamba) [INNEGOCIABLE]
Qué es: Aislar dependencias por proyecto para que no choquen entre sí.
Por qué te pagan: Reproducibilidad: que tu código corra igual en tu máquina y en la del cliente.
Programación orientada a objetos [APOYO]
Qué es: Organizar código en clases reutilizables.
Por qué te pagan: Diferencia el script de juguete del software mantenible que una empresa acepta.
Testing (pytest) [APOYO]
Qué es: Escribir pruebas que verifican que tu código hace lo que debe.
Por qué te pagan: Software sin pruebas no entra a producción en una empresa seria.
R (tu segundo idioma, para estadística/ómica)
R base + tidyverse [APOYO]
Qué es: Lenguaje estadístico; tidyverse (dplyr, ggplot2) para manipular y graficar datos elegantemente.
Por qué te pagan: El estándar en análisis estadístico de expresión génica; muchos labs lo exigen.
Bioconductor [INNEGOCIABLE]
Qué es: Ecosistema de paquetes R para datos ómicos (DESeq2, edgeR, limma).
Por qué te pagan: Es la herramienta estándar de RNA-seq y expresión diferencial en la industria.
Control de versiones
Git [INNEGOCIABLE]
Qué es: Sistema para versionar código: guardar historia, ramas, revertir cambios.
Por qué te pagan: Ninguna empresa de software trabaja sin Git; no saberlo te descarta al instante.
GitHub / GitLab [INNEGOCIABLE]
Qué es: Plataforma donde publicas repos, colaboras y muestras tu trabajo.
Por qué te pagan: Tu GitHub ES tu CV técnico. El reclutador lo abre antes de leer tu hoja de vida.
Flujo colaborativo (branches, PR, code review) [APOYO]
Qué es: Trabajar en equipo sin pisarse: ramas, pull requests, revisión de código.
Por qué te pagan: Demuestra que sabes trabajar en un equipo distribuido, no solo en tu cueva.
Dominio 3 — Secuenciación de nueva generación (NGS)
El corazón técnico de la bioinformática moderna. Dominar el flujo FASTQ→resultado es lo que te hace 'bioinformático' de verdad. Empresas como Illumina, Genentech y Moderna viven de esto.
Formatos: FASTQ, FASTA, SAM/BAM, VCF, BED, GTF/GFF [INNEGOCIABLE]
Qué es: Los formatos de archivo estándar: lecturas crudas, secuencias, alineamientos, variantes, anotaciones.
Por qué te pagan: Hablar estos formatos es el alfabeto del campo; sin ellos no lees ni un dato.
Puntuación de calidad Phred [INNEGOCIABLE]
Qué es: Escala logarítmica que mide la confianza de cada base secuenciada (Q30 = 1 error en 1000).
Por qué te pagan: Es cómo decides si un dato es usable o basura — la decisión que te pagan (ver Ticket #001).
Control de calidad: FastQC / MultiQC [INNEGOCIABLE]
Qué es: Herramientas que evalúan la calidad de lecturas crudas y agregan reportes de muchas muestras.
Por qué te pagan: El primer paso de todo proyecto; el cliente confía en tu lectura del QC.
Trimming: Trimmomatic / fastp / cutadapt [INNEGOCIABLE]
Qué es: Recortar bases de mala calidad y adaptadores de las lecturas.
Por qué te pagan: Limpiar bien = resultados confiables; limpiar mal = arruinar el experimento del cliente.
Alineamiento: BWA / Bowtie2 (ADN), STAR / HISAT2 (ARN) [INNEGOCIABLE]
Qué es: Mapear las lecturas contra un genoma de referencia.
Por qué te pagan: Paso central de casi todo pipeline; elegir el alineador correcto es criterio experto.
samtools / bcftools [INNEGOCIABLE]
Qué es: Manipular alineamientos (BAM) y variantes (VCF): ordenar, indexar, filtrar.
Por qué te pagan: Las navajas suizas del NGS; se usan en absolutamente todos los flujos.
Variant calling: GATK (HaplotypeCaller), DeepVariant [INNEGOCIABLE]
Qué es: Detectar variantes (SNPs, indels) a partir de alineamientos, siguiendo GATK Best Practices.
Por qué te pagan: El producto de mayor valor en diagnóstico y genómica clínica; aquí está el dinero clínico.
RNA-seq: cuantificación (Salmon, featureCounts) y expresión diferencial (DESeq2) [INNEGOCIABLE]
Qué es: Medir cuánto se expresa cada gen y qué cambia entre condiciones.
Por qué te pagan: Uno de los análisis más solicitados en industria y academia.
Anotación funcional (SnpEff, VEP, ANNOVAR) [APOYO]
Qué es: Darle significado biológico a las variantes: ¿en qué gen?, ¿qué efecto?
Por qué te pagan: Convierte una lista de variantes cruda en una decisión clínica accionable.
scRNA-seq (single-cell): Seurat / Scanpy [DIFERENCIAL]
Qué es: Análisis de expresión célula por célula, no en promedio.
Por qué te pagan: Área de altísima demanda y salario en 2026; pocos juniors la dominan.
SplitNCigarReads y manejo de splice para RNA variant calling [APOYO]
Qué es: Paso técnico específico para llamar variantes desde datos de ARN.
Por qué te pagan: Detalle experto que demuestra que sabes GATK Best Practices de verdad.
Dominio 4 — Pipelines y reproducibilidad (el salto de sueldo)
Este dominio es la línea que separa al 'junior de laptop' del profesional de producción. Nextflow domina las ofertas de industria en 2026. Dominar esto es lo que dispara tu salario de local a internacional.
Nextflow (DSL2) [INNEGOCIABLE]
Qué es: Lenguaje/framework para escribir pipelines reproducibles que corren igual en laptop, cluster o cloud.
Por qué te pagan: DOMINA las vacantes de industria 2026; es el skill 'de oro' que más piden. Tu prioridad tras el NGS básico.
nf-core [DIFERENCIAL]
Qué es: Colección de pipelines Nextflow revisados por la comunidad, listos para producción.
Por qué te pagan: Contribuir o usar nf-core en tu portafolio te posiciona como profesional serio, no aficionado.
Snakemake [APOYO]
Qué es: Alternativa a Nextflow basada en Python para pipelines reproducibles.
Por qué te pagan: Algunas empresas/academia lo prefieren; saber ambos te hace flexible.
Docker [INNEGOCIABLE]
Qué es: Empaquetar tu software + dependencias en un 'contenedor' que corre idéntico en cualquier máquina.
Por qué te pagan: Casi obligatorio en 2026; garantiza reproducibilidad y pasa scans de seguridad.
Apptainer / Singularity [APOYO]
Qué es: Contenedores diseñados para clusters HPC (sin privilegios de root).
Por qué te pagan: El estándar en entornos académicos y de supercómputo; complementa a Docker.
Make / flujos de trabajo básicos [APOYO]
Qué es: Automatizar secuencias de pasos con dependencias.
Por qué te pagan: Fundamento conceptual que hace que Nextflow tenga sentido.
Reproducibilidad y FAIR [APOYO]
Qué es: Principios para que un análisis sea repetible y verificable por otros.
Por qué te pagan: En farma y clínica, un resultado no reproducible no vale nada legalmente.
Dominio 5 — Cómputo de alto rendimiento y nube
Donde corre el trabajo pesado de verdad. Rocky Linux es tu terreno de cluster. La nube (AWS/GCP) es lo que las multinacionales usan y pagan por que sepas.
SLURM (gestor de colas HPC) [INNEGOCIABLE]
Qué es: Enviar y gestionar trabajos en un cluster compartido: colas, recursos, prioridades.
Por qué te pagan: Diferencia al que corre análisis en su laptop del que opera en infraestructura real.
Conceptos HPC (nodos, cores, memoria, paralelismo) [INNEGOCIABLE]
Qué es: Entender cómo repartir un trabajo grande entre muchas máquinas.
Por qué te pagan: Sin esto, un análisis que debería tardar horas te tarda semanas.
Cloud: AWS (S3, Batch, EC2) / Google Cloud [DIFERENCIAL]
Qué es: Almacenar datos y correr pipelines en la nube bajo demanda.
Por qué te pagan: Las multinacionales operan en cloud; saber esto es requisito explícito en muchas vacantes de sueldo alto.
Almacenamiento y transferencia de datos grandes [APOYO]
Qué es: Mover terabytes de forma eficiente y segura (rsync, aws s3, globus).
Por qué te pagan: Los datos genómicos son enormes; moverlos mal cuesta tiempo y dinero.
Dominio 6 — Estadística y machine learning aplicado
La biología te da el 'qué'; la estadística te dice si es real o ruido. El ML aplicado es la frontera mejor pagada, y conecta con tu proyecto de biomarcadores y con Modelización de Sistemas (8.º).
Estadística inferencial (pruebas de hipótesis, p-valor, intervalos) [INNEGOCIABLE]
Qué es: Decidir si una diferencia observada es real o azar.
Por qué te pagan: Interpretar mal un p-valor arruina conclusiones; los reclutadores prueban esto en entrevista.
Corrección de pruebas múltiples (FDR, Bonferroni) [INNEGOCIABLE]
Qué es: Ajustar por hacer miles de comparaciones a la vez (típico en ómica).
Por qué te pagan: Sin esto, reportas 'hallazgos' que son puro azar; error clásico que te descalifica.
Distribuciones y modelos (normal, binomial negativa, regresión) [APOYO]
Qué es: Los modelos matemáticos detrás de los datos de conteo (RNA-seq usa binomial negativa).
Por qué te pagan: Entender el modelo correcto es lo que separa análisis experto de recetas ciegas.
Machine learning: clasificación, regresión, validación cruzada [DIFERENCIAL]
Qué es: Entrenar modelos que predicen (ej. ¿este paciente tiene el biomarcador?).
Por qué te pagan: El núcleo de tu proyecto estrella y de las áreas mejor pagadas de 2026.
scikit-learn [DIFERENCIAL]
Qué es: Librería estándar de ML en Python.
Por qué te pagan: La herramienta con la que construyes y evalúas modelos predictivos reales.
Sobreajuste, fuga de datos y métricas (ROC, AUC, precisión/recall) [DIFERENCIAL]
Qué es: Errores clásicos de ML y cómo medir bien un modelo clínico.
Por qué te pagan: En diagnóstico, un modelo mal validado mata; saber evitarlo es premium clínico.
Biología de sistemas / modelado [APOYO]
Qué es: Modelar redes biológicas y estructuras (conecta con tu materia de 8.º).
Por qué te pagan: Área de alta demanda que cruza biología, matemática y cómputo.
Dominio 7 — Seguridad de datos genómicos (tu diferencial raro)
Tu carta fuerte poco común. AthenaOS es tu terreno. En datos clínicos —tu proyecto de biomarcadores— esto justifica cobrar el doble, porque nadie contrata al más barato para tocar sangre de pacientes.
Hardening de sistemas [DIFERENCIAL]
Qué es: Endurecer un sistema Linux para minimizar superficies de ataque.
Por qué te pagan: Casi ningún bioinformático junior lo sabe; es diferencial puro en entrevista.
Cifrado en reposo y en tránsito [DIFERENCIAL]
Qué es: Proteger datos guardados y en transferencia (LUKS, GPG, TLS).
Por qué te pagan: Datos de pacientes sin cifrar = ilegal. Saberlo es requisito en clínica/farma.
Control de accesos y principio de mínimo privilegio [DIFERENCIAL]
Qué es: Dar a cada usuario solo lo justo que necesita.
Por qué te pagan: Base de cualquier cumplimiento; una fuga por permisos laxos hunde una empresa.
Cumplimiento: HIPAA / GDPR (nociones) [DIFERENCIAL]
Qué es: Marcos legales que rigen datos de salud (EE.UU./Europa).
Por qué te pagan: Las multinacionales de salud EXIGEN esto; conecta con tu materia de Regulación.
Anonimización y pseudonimización de datos clínicos [APOYO]
Qué es: Quitar o enmascarar la identidad del paciente de los datos.
Por qué te pagan: Permite investigar sin violar privacidad; habilidad muy valorada en biotech clínica.
Dominio 8 — Fundamento biológico (el 'qué' interpretar)
No te pagan por esto directamente, pero sin ello no puedes interpretar resultados ni hablar con biólogos. Tu malla universitaria cubre bien este dominio; aquí solo lo anclas al vocabulario que usarás.
Dogma central (ADN→ARN→proteína) [APOYO]
Qué es: El flujo fundamental de la información genética.
Por qué te pagan: Marco mental de todo análisis; hablarlo con soltura te da credibilidad.
Genómica, transcriptómica, proteómica, metabolómica [APOYO]
Qué es: Las capas 'ómicas' de datos y qué mide cada una.
Por qué te pagan: Saber cuál capa responde qué pregunta es lo que te hace útil al cliente.
Variantes genéticas (SNP, indel, CNV, SV) y su efecto [APOYO]
Qué es: Los tipos de cambios en el ADN y sus consecuencias.
Por qué te pagan: Vocabulario diario en diagnóstico molecular; conecta con tu materia de 7.º.
Expresión génica y regulación [APOYO]
Qué es: Cómo y cuándo se activan los genes.
Por qué te pagan: Base para interpretar RNA-seq, el análisis estrella de la industria.
Filogenia y evolución molecular [APOYO]
Qué es: Reconstruir parentescos evolutivos desde secuencias.
Por qué te pagan: Conecta con tu materia de 7.º y con áreas de salud pública/epidemiología.
Inmunología aplicada / inmunoinformática [DIFERENCIAL]
Qué es: Análisis computacional del sistema inmune (vacunas, anticuerpos).
Por qué te pagan: Nicho muy bien pagado; conecta con tu materia de 8.º y tu proyecto clínico.
Dominio 9 — Negocio, venta y carrera (el multiplicador de sueldo)
El técnico puro es reemplazable y cobra por hora. El que conecta la técnica con el dinero pone su propio precio. Estas 'materias no técnicas' de tu malla (Bioeconomía, Regulación, Calidad, Biodescubrimiento) son tu ventaja secreta.
Traducir técnica a valor de negocio [DIFERENCIAL]
Qué es: Explicar qué DECISIÓN o ahorro habilita tu análisis, no qué comando corriste.
Por qué te pagan: Es la diferencia entre cobrar $80/hora y cobrar $5.000 por proyecto. El skill de dinero #1.
Cotización por valor (no por hora) [DIFERENCIAL]
Qué es: Poner precio según lo que le ahorras/haces ganar al cliente, no según tu tiempo.
Por qué te pagan: Rompe el techo de ingreso; te saca de competir con el freelance más barato del mundo.
Portafolio y personal branding [INNEGOCIABLE]
Qué es: Empaquetar tu trabajo (GitHub, README, LinkedIn) como evidencia de problemas resueltos.
Por qué te pagan: Es tu idioma de venta al reclutador internacional; sin esto, 'sé Python' no vale nada.
Comunicación y trabajo remoto (Slack, Jira, async) [INNEGOCIABLE]
Qué es: Colaborar en equipos distribuidos, escribir claro, actualizar sin que te persigan.
Por qué te pagan: Las multinacionales contratan LatAm por costo Y por poder trabajar así; demuéstralo.
Entrevista técnica y negociación salarial [INNEGOCIABLE]
Qué es: Defender tu trabajo bajo presión y negociar el sueldo sin miedo.
Por qué te pagan: Negociar bien una vez = miles de dólares/año; es el mejor ROI de tu carrera.
Lectura de mercado y oportunidad [DIFERENCIAL]
Qué es: Detectar qué problema tiene un cliente/empresa y cómo tu skill lo resuelve por dinero.
Por qué te pagan: La base del freelance y de tu futura startup; conecta con Bioeconomía y Biodescubrimiento.
Regulación y calidad como argumento de venta [APOYO]
Qué es: Usar tu conocimiento de normas (ISO, HIPAA) para justificar confianza y precio premium.
Por qué te pagan: En farma/clínica, la confianza vale más que la técnica; esto la respalda.
Orden de ataque recomendado
Todo lo anterior es el destino. Este es el ORDEN inteligente para llegar sin dispersarte, dado que ya dominas el inglés (tu ventaja competitiva #1 ya ganada):
#
Etapa
Qué dominas y por qué
1
Cimientos
Linux/Bash + Python (pandas, biopython) + Git. Sin esto nada corre.
2
NGS básico
FASTQ→QC→alineamiento→variantes. Tu primer pipeline real en GitHub.
3
Reproducibilidad
Nextflow + Docker. EL salto de sueldo de local a internacional.
4
Proyecto estrella
Biomarcadores en sangre: junta todo + seguridad de datos + ML. Tu pieza de venta y tu titulación.
5
Cloud/HPC
AWS + SLURM. Lo que exige la multinacional para el sueldo alto.
6
Negocio + postular
Portafolio pulido, cotizar por valor, entrevistas. Transversal desde el paso 3.
Recuerda la ecuación final: empleo internacional (paga las cuentas + da capital, red y 'MBA gratis') → acumulación durante años acomodados → startup desde posición de fuerza. Cada skill de este glosario es un ladrillo de ese camino.
Documento-pivote vivo. Ábrelo al iniciar cada chat y dime qué dominio entrenamos con el próximo ticket. Se amplía conforme descubramos skills nuevas que pida el mercado.