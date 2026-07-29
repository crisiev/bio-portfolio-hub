# 📚 Documento 02 — Guía de Sílabos de Materias Pendientes

> [!IMPORTANT]
> **El contenido probable de las 23 materias que aún no ves, ambientado hacia el empleo**  
> *"Quiero llegar a cada materia ya sabiendo qué me van a enseñar y para qué me sirve en el trabajo."*  
> **Preparado para:** `cjalcivar@gmail.com` · **Fecha:** 28 de julio de 2026

---

## 📑 Tabla de Contenidos
- [Cómo usar esta guía](#cómo-usar-esta-guía)
- [Grupo A · Núcleo Computacional (Tus Minas de Oro)](#grupo-a--núcleo-computacional-tus-minas-de-oro)
- [Grupo B · Ómicas y Clínica (Alto Valor)](#grupo-b--ómicas-y-clínica-alto-valor)
- [Grupo C · Biotecnología Aplicada (Apoyo)](#grupo-c--biotecnología-aplicada-apoyo)
- [Grupo D · Formación Complementaria (Contexto)](#grupo-d--formación-complementaria-contexto)

---

## 🧭 Cómo usar esta guía

Esto no reemplaza el sílabo oficial de tu universidad —cada docente ajusta— pero te da el mapa típico de cada materia: lo que casi con certeza verás, el vocabulario que debes manejar, ejercicios para practicar desde ya, y —lo más importante para ti— el puente a empleo: qué competencia contratable le sacas a cada una.

> [!NOTE]
> **Etiquetas de Priorización:**
> - 🔥 **MINA DE ORO** — Núcleo directo de bioinformática. Exprímela al máximo; de aquí sale portafolio.
> - ⭐ **ALTO VALOR** — Ómica o clínica; muy empleable si la conviertes en proyecto.
> - 🛠️ **APOYO** — Contexto o skill transversal útil; da robustez a tu narrativa.
> - 📖 **CONTEXTO** — Apruébala bien, pero no le robes horas al portafolio.

> [!TIP]
> **Regla que gobierna todo:**  
> No memorizas conceptos para un examen: **los conviertes en algo que corre en tu GitHub**. Esta guía te dice qué dominar; los tickets de tu Campaña te hacen demostrarlo.

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 💻 Grupo A · Núcleo computacional (tus minas de oro)
Estas cuatro materias son tu carrera objetivo con nombre y apellido. Si algo tienes que dominar de la malla, es esto. A cada una le das roleplay laboral intenso: cada concepto sale en forma de repositorio.
1. Base de Datos y Programación para Bioinformática   ·  2 créditos
MINA DE ORO
La materia más importante de tu malla para el empleo. Aquí formalizas lo que el mercado paga: modelar, almacenar y consultar datos biológicos con SQL y programar sobre ellos con criterio de ingeniería.
Temario esperado
Modelo relacional: entidades, relaciones, claves primarias y foráneas, normalización (1FN–3FN).
SQL de principio a fin: SELECT, JOIN, GROUP BY, subconsultas, índices, vistas; diseño de esquemas.
Bases de datos biológicas públicas: NCBI (GenBank, RefSeq, dbSNP), Ensembl, UniProt, PDB, KEGG.
Programación aplicada: estructuras de datos (listas, diccionarios, sets), complejidad, parsing de formatos.
Bases NoSQL y formatos de intercambio (JSON, XML) para datos ómicos heterogéneos.
Integración: consultar bases remotas por API/E-utilities y cargar resultados a una BD local.
Glosario clave
Esquema (schema) — el plano de la base de datos: qué tablas hay, sus columnas y cómo se relacionan.
Clave foránea (FK) — columna que apunta a la clave primaria de otra tabla; garantiza integridad referencial.
Normalización — organizar tablas para evitar redundancia y anomalías de actualización.
JOIN — operación que combina filas de dos tablas según una condición; el corazón de SQL.
Índice — estructura que acelera búsquedas a cambio de espacio; decisiva con millones de variantes.
E-utilities / API — interfaz para consultar programáticamente bases del NCBI (esearch, efetch).
ORM — capa que mapea tablas a objetos del lenguaje (p. ej. SQLAlchemy) para no escribir SQL crudo.
Ejercicios para practicar (con sabor laboral)
Diseña el esquema de una base de datos genómica (muestras, variantes, anotaciones) y créalo en SQLite/PostgreSQL.
Escribe consultas SQL que respondan preguntas reales: “¿qué variantes patogénicas aparecen en >5 pacientes?”.
Automatiza con Python (Biopython + E-utilities) la descarga de secuencias de GenBank y cárgalas a tu BD.
Indexa una tabla de 1M de variantes y mide el antes/después del tiempo de consulta.
Puente a empleo · línea de CV/portafolio
Proyecto: base de datos genómica consultable + scripts de carga (ETL) desde bases públicas.
CV: “Diseñé y poblé una base de datos genómica (PostgreSQL) con pipeline ETL en Python desde NCBI/Ensembl, con consultas SQL optimizadas por índices.”
2. Estadística para Bioinformática   ·  2 créditos
MINA DE ORO
La biología te da el “qué”; la estadística te dice si es real o ruido. Interpretar mal un p-valor arruina conclusiones —y los reclutadores lo prueban en entrevista. Esta materia es el corazón del análisis de expresión y del ML.
Temario esperado
Estadística descriptiva e inferencial: distribuciones, estimación, intervalos de confianza.
Pruebas de hipótesis: t-test, Wilcoxon, chi-cuadrado; error tipo I y II, potencia estadística.
El problema de las pruebas múltiples: por qué miles de comparaciones inflan los falsos positivos.
Corrección múltiple: Bonferroni, Benjamini-Hochberg (FDR), q-valor.
Modelos para datos de conteo: Poisson y binomial negativa (base de RNA-seq).
Regresión lineal y logística; introducción a modelos lineales generalizados (GLM).
Reproducibilidad estadística y visualización honesta (volcano plot, MA plot, PCA).
Glosario clave
p-valor — probabilidad de ver un resultado igual o más extremo si la hipótesis nula fuera cierta. No es “probabilidad de acertar”.
FDR (tasa de falsos descubrimientos) — proporción esperada de falsos positivos entre los resultados llamados significativos; clave en ómica.
Binomial negativa — distribución que modela conteos con sobredispersión; la usan DESeq2 y edgeR para RNA-seq.
Potencia — probabilidad de detectar un efecto real; sube con tamaño de muestra y efecto grande.
PCA — reducción de dimensionalidad que revela estructura y lotes (batch) en datos ómicos.
Volcano plot — gráfico de significancia vs magnitud de cambio; el resumen visual estándar de expresión diferencial.
Ejercicios para practicar (con sabor laboral)
Simula 10.000 genes sin diferencia real y muestra cuántos “salen significativos” sin corrección: entiende el FDR con tus manos.
Aplica Benjamini-Hochberg a una tabla de p-valores y compara resultados con y sin corrección.
Ajusta un modelo binomial negativa a conteos de RNA-seq y explica por qué no usas una normal.
Construye un volcano plot en R (ggplot2) o Python y redáctalo como si se lo explicaras a un biólogo de laboratorio.
Puente a empleo · línea de CV/portafolio
Proyecto: análisis de expresión diferencial (DESeq2/edgeR) con control de FDR e interpretación biológica.
CV: “Análisis estadístico de datos ómicos: pruebas de hipótesis, corrección por pruebas múltiples (FDR) y modelos de conteo para expresión diferencial.”
3. Evolución Molecular y Filogenia   ·  2 créditos
MINA DE ORO
Algoritmos bioinformáticos clásicos y muy pedidos —salud pública, virología, epidemiología genómica—. Reconstruir parentescos desde secuencias es una competencia que pocos juniors muestran con un pipeline real.
Temario esperado
Homología, ortología y paralogía; sustituciones sinónimas y no sinónimas (dN/dS).
Alineamiento de secuencias: por pares (Needleman-Wunsch, Smith-Waterman) y múltiple (MAFFT, MUSCLE).
Modelos de sustitución nucleotídica y proteica (JC69, K80, GTR, WAG).
Métodos de reconstrucción: distancia (NJ), máxima parsimonia, máxima verosimilitud (RAxML/IQ-TREE), bayesiano (MrBayes/BEAST).
Soporte de ramas: bootstrap, probabilidad posterior; interpretación de árboles.
Reloj molecular y filogenética temporal; aplicaciones a brotes y virus.
Glosario clave
Alineamiento múltiple (MSA) — alinear 3+ secuencias para revelar posiciones conservadas; insumo de todo árbol.
Ortólogos vs parálogos — genes separados por especiación vs por duplicación; distinguirlos evita errores de anotación.
Máxima verosimilitud — método que elige el árbol que hace más probable los datos bajo un modelo de sustitución.
Bootstrap — remuestreo que estima la confianza de cada rama (valores >70 % se consideran sólidos).
dN/dS — razón que detecta selección: >1 positiva, <1 purificadora, =1 neutra.
Reloj molecular — supuesto de tasa de mutación ~constante para datar divergencias.
Ejercicios para practicar (con sabor laboral)
Descarga secuencias de un gen viral (p. ej. spike) de varias cepas, alinéalas con MAFFT y construye un árbol con IQ-TREE.
Interpreta los valores de bootstrap: ¿qué clados son confiables y cuáles no?
Calcula dN/dS de un gen y argumenta si está bajo selección positiva.
Automatiza el flujo (descarga→alineamiento→árbol→figura) en un script reproducible.
Puente a empleo · línea de CV/portafolio
Proyecto: pipeline filogenético reproducible (MSA → árbol ML → figura anotada) sobre un dataset viral real.
CV: “Pipeline de filogenia molecular (MAFFT + IQ-TREE) con soporte por bootstrap e interpretación de selección (dN/dS), aplicado a genómica de patógenos.”
4. Modelización de Sistemas y Estructuras Biológicas   ·  2 créditos
MINA DE ORO
Tu puerta al ML/IA aplicado y a la biología estructural —la franja mejor pagada de 2026—. Modelas redes biológicas y estructuras de proteínas; conecta directo con tu proyecto estrella.
Temario esperado
Biología de sistemas: redes de regulación génica, redes metabólicas, análisis de grafos.
Modelado dinámico: ecuaciones diferenciales, modelos basados en agentes, análisis de flujo metabólico (FBA).
Estructura de proteínas: niveles (1ª–4ª), predicción y plegamiento; AlphaFold y sucesores.
Docking molecular y bases de estructura (PDB); visualización (PyMOL, ChimeraX).
Introducción al machine learning aplicado a biología: clasificación, regresión, validación cruzada.
Sobreajuste, fuga de datos y métricas clínicas (ROC, AUC, precisión/recall).
Glosario clave
Red de regulación génica — grafo de qué genes activan/reprimen a cuáles; se modela y simula.
FBA (análisis de balance de flujos) — método para predecir flujos metabólicos sin cinética detallada.
AlphaFold — modelo de IA que predice estructura 3D de proteínas desde la secuencia; cambió el campo.
Docking — simular cómo una molécula pequeña se acopla a una proteína (descubrimiento de fármacos).
Fuga de datos (data leakage) — cuando información del test se filtra al entrenamiento e infla el rendimiento; error fatal en clínica.
AUC-ROC — métrica de un clasificador: área bajo la curva de sensibilidad vs 1-especificidad.
Ejercicios para practicar (con sabor laboral)
Descarga una estructura de PDB, visualízala en PyMOL y señala su sitio activo.
Entrena un clasificador (scikit-learn) sobre un dataset biológico y valida con validación cruzada, evitando fuga de datos.
Reporta AUC, precisión y recall, y explica por qué el accuracy engaña en clases desbalanceadas.
Modela una pequeña red de regulación y simula su dinámica.
Puente a empleo · línea de CV/portafolio
Proyecto: clasificador con validación biológica (el módulo ML de tu proyecto estrella de biomarcadores).
CV: “Modelo de ML (scikit-learn) para clasificación de biomarcadores con validación cruzada, control de fuga de datos y métricas clínicas (AUC-ROC), interpretado biológicamente.”
Grupo B · Ómicas y clínica (alto valor empleable)
Aquí está el “qué” biológico que interpretas con tu código, y el sector salud —que paga bien—. Convierte cada una en un notebook o módulo de portafolio.
5. Genómica Estructural y Funcional   ·  3 créditos
ALTO VALOR
El contexto del NGS moderno: ensamblar, anotar y medir expresión de genomas. Sostiene toda tu narrativa técnica de pipelines.
Temario esperado
Estructura del genoma: genes, elementos reguladores, repetidos, cromatina.
Ensamblado de genomas (de novo y guiado por referencia); métricas (N50, cobertura).
Anotación estructural y funcional (Ontología Génica, KEGG, InterPro).
Transcriptómica: RNA-seq, cuantificación de expresión, isoformas y splicing.
Genómica funcional: ATAC-seq, ChIP-seq, epigenómica (nociones).
Genómica comparada y sinténica.
Glosario clave
N50 — métrica de calidad de ensamblado: longitud tal que el 50 % del genoma está en contigs de ese tamaño o mayores.
Anotación — asignar identidad y función a regiones del genoma (dónde están los genes y qué hacen).
Ontología Génica (GO) — vocabulario controlado de funciones, procesos y componentes celulares.
Splicing alternativo — un gen produce varias isoformas de ARN; relevante en RNA-seq.
ATAC-seq — técnica que mapea cromatina accesible (regiones activas del genoma).
Ejercicios para practicar (con sabor laboral)
Ensambla un genoma bacteriano pequeño y calcula su N50 y cobertura.
Anota los genes de un contig y haz un análisis de enriquecimiento GO.
Cuantifica expresión (Salmon/featureCounts) y detecta genes diferencialmente expresados.
Puente a empleo · línea de CV/portafolio
Proyecto: pipeline RNA-seq / variant calling con anotación funcional.
CV: “Análisis de genómica funcional: ensamblado, anotación (GO/KEGG) y cuantificación de expresión con interpretación biológica.”
6. Proteómica y Metabolómica   ·  3 créditos
ALTO VALOR
Datos ómicos más allá del ADN. La integración multi-ómica es justo lo que separa al analista de $90k del científico de $150k+ en 2026.
Temario esperado
Espectrometría de masas: principios, LC-MS/MS, identificación y cuantificación de péptidos.
Bases y herramientas de proteómica (UniProt, MaxQuant, Perseus).
Metabolómica dirigida y no dirigida; anotación de metabolitos.
Análisis estadístico de datos ómicos de alta dimensión; normalización y control de lotes.
Integración multi-ómica (genómica + transcriptómica + proteómica + metabolómica).
Análisis de enriquecimiento de rutas (pathway analysis).
Glosario clave
LC-MS/MS — cromatografía líquida acoplada a espectrometría de masas en tándem; base de la proteómica moderna.
Espectro de masas — huella de razones masa/carga que identifica moléculas.
Multi-ómica — combinar varias capas ómicas para una visión de sistema; muy valorada.
Efecto de lote (batch effect) — variación técnica que confunde la señal biológica; hay que corregirla.
Análisis de rutas — ver qué vías metabólicas/señalización están alteradas, no solo genes sueltos.
Ejercicios para practicar (con sabor laboral)
Procesa una matriz de abundancia proteica: normaliza, corrige lote (con PCA antes/después) y haz test diferencial.
Haz un análisis de enriquecimiento de rutas sobre las proteínas alteradas.
Integra una lista de genes (transcriptómica) con proteínas (proteómica) y discute concordancias.
Puente a empleo · línea de CV/portafolio
Proyecto: notebook de análisis multi-ómico con integración e interpretación de rutas.
CV: “Integración multi-ómica (transcriptómica + proteómica) con corrección de efecto de lote y análisis de enriquecimiento de rutas.”
7. Diagnóstico Molecular   ·  3 créditos
ALTO VALOR
Tu ancla clínica: alimenta directo el proyecto estrella de biomarcadores en sangre y te abre el sector salud. Aplicación real que da empleo.
Temario esperado
Técnicas de diagnóstico: PCR, qPCR, RT-PCR, secuenciación clínica, paneles NGS.
Biomarcadores: descubrimiento, validación, sensibilidad/especificidad, valor predictivo.
Interpretación de variantes clínicas (ACMG), bases (ClinVar, OMIM).
Biopsia líquida y ADN tumoral circulante (ctDNA).
Control de calidad y validación de ensayos diagnósticos.
Marco regulatorio clínico (CLIA, IVD; nociones).
Glosario clave
Biomarcador — característica medible que indica un estado biológico o enfermedad.
Sensibilidad / especificidad — capacidad de detectar enfermos / de descartar sanos; definen un test.
Clasificación ACMG — criterios estándar para clasificar variantes (patogénica → benigna).
ctDNA — ADN tumoral libre en sangre; base de la biopsia líquida no invasiva.
Valor predictivo — probabilidad de que un resultado positivo/negativo sea correcto en una población.
Ejercicios para practicar (con sabor laboral)
Clasifica un set de variantes con criterios ACMG usando ClinVar y justifica cada llamada.
Calcula sensibilidad, especificidad y valores predictivos de un test a partir de una tabla 2×2.
Diseña, en papel, el flujo de un panel NGS clínico desde la muestra al reporte.
Puente a empleo · línea de CV/portafolio
Proyecto: refuerza el proyecto estrella de biomarcadores en sangre con interpretación clínica ACMG.
CV: “Interpretación de variantes clínicas (ACMG/ClinVar) y evaluación de desempeño diagnóstico (sensibilidad/especificidad) para paneles NGS.”
8. Ingeniería Genética   ·  3 créditos
ALTO VALOR
Manejo real de secuencias: FASTA/GenBank, BLAST, diseño de primers y constructos in silico. El “qué” molecular detrás de mucho análisis.
Temario esperado
Enzimas de restricción, clonación, vectores; diseño de constructos.
PCR y diseño de primers; mutagénesis dirigida.
Edición genómica: CRISPR-Cas9, diseño de guías (gRNA), off-targets.
Análisis de secuencias in silico: BLAST, mapas de restricción, ORF finding.
Biología sintética: ensamblaje modular, partes estándar.
Glosario clave
BLAST — herramienta que busca secuencias similares en bases; el “buscador” del bioinformático.
gRNA (ARN guía) — secuencia que dirige a Cas9 al sitio a editar; su diseño minimiza off-targets.
Off-target — corte no deseado en un sitio parecido al blanco; riesgo clave en edición.
ORF — marco abierto de lectura; región que potencialmente codifica proteína.
Vector — molécula de ADN que transporta e inserta un gen en una célula huésped.
Ejercicios para practicar (con sabor laboral)
Diseña primers para amplificar un gen y verifica especificidad con BLAST.
Diseña gRNAs para CRISPR y evalúa off-targets con una herramienta online/local.
Escribe un script Python (Biopython) que encuentre ORFs y sitios de restricción en un FASTA.
Puente a empleo · línea de CV/portafolio
Proyecto: script de análisis de secuencias (primers/ORFs/restricción) publicado en GitHub.
CV: “Análisis de secuencias in silico con Biopython y BLAST: diseño de primers y guías CRISPR con evaluación de especificidad.”
9. Inmunología Aplicada   ·  2 créditos
ALTO VALOR
La inmunoinformática es un nicho muy bien pagado (vacunas, anticuerpos) y conecta con tu proyecto clínico.
Temario esperado
Sistema inmune: innato y adaptativo, antígenos, epítopos, MHC/HLA.
Inmunoinformática: predicción de epítopos, diseño de vacunas in silico.
Repertorio inmune: secuenciación de BCR/TCR, análisis de diversidad.
Anticuerpos: estructura, ingeniería, humanización.
Aplicaciones: inmunoterapia, neoantígenos en cáncer.
Glosario clave
Epítopo — parte del antígeno que reconoce el sistema inmune; su predicción guía vacunas.
MHC/HLA — moléculas que presentan péptidos a las células T; su tipado importa en trasplantes e inmunoterapia.
Neoantígeno — antígeno nuevo por mutaciones tumorales; blanco de inmunoterapia personalizada.
Repertorio BCR/TCR — conjunto de receptores de células B/T; se secuencia y analiza su diversidad.
Ejercicios para practicar (con sabor laboral)
Predice epítopos de unión a MHC de una proteína viral con una herramienta estándar (IEDB).
Analiza diversidad de un repertorio TCR de datos públicos.
Prioriza neoantígenos a partir de una lista de mutaciones tumorales.
Puente a empleo · línea de CV/portafolio
Proyecto (opcional diferencial): mini-pipeline de predicción de epítopos para diseño de vacunas.
CV: “Inmunoinformática: predicción de epítopos MHC y priorización de neoantígenos para inmunoterapia.”
Grupo C · Bioprocesos e industria
Materias de dominio industrial. Su valor bioinformático llega cuando las conviertes en análisis de datos: series temporales, optimización y control de calidad de procesos.
10. Bioprocesos   ·  3 créditos
APOYO
De aquí sacas datos de proceso (fermentación, cultivos) que se analizan con Python/pandas y estadística: series temporales y optimización.
Temario esperado
Cinética de crecimiento microbiano y de reacción enzimática.
Diseño y escalado de biorreactores; variables de proceso (pH, OD, temperatura).
Balance de materia y energía; rendimiento y productividad.
Diseño de experimentos (DoE) y optimización de procesos.
Monitoreo y control; datos de sensores en el tiempo.
Glosario clave
Cinética de Monod — modelo de crecimiento microbiano en función del sustrato limitante.
Biorreactor — recipiente controlado donde ocurre un bioproceso; genera series de datos.
DoE — metodología estadística para explorar factores con pocos experimentos.
Rendimiento (yield) — producto obtenido por unidad de sustrato consumido.
Ejercicios para practicar (con sabor laboral)
Ajusta una curva de crecimiento (Monod/logística) a datos reales con Python (scipy).
Analiza una serie temporal de fermentación con pandas y detecta la fase exponencial.
Diseña un DoE simple y analiza qué factor impacta más el rendimiento.
Puente a empleo · línea de CV/portafolio
Proyecto: notebook de análisis de datos de proceso (ajuste de curvas + series temporales).
CV: “Análisis de datos de bioprocesos en Python: ajuste cinético, series temporales y diseño de experimentos.”
11. Microbiología Industrial   ·  3 créditos
CONTEXTO
Contexto de bioprocesos y datos de cultivos. Su gancho bioinformático es la metagenómica y el análisis de comunidades microbianas.
Temario esperado
Microorganismos de interés industrial; fermentaciones (alcohólica, láctica, etc.).
Producción de metabolitos, enzimas y biofármacos.
Cultivo, esterilización, control microbiológico.
Nociones de metagenómica y microbioma industrial.
Glosario clave
Cepa productora — microorganismo seleccionado/mejorado para producir un compuesto.
Metagenómica — secuenciar el ADN de una comunidad completa sin cultivar.
16S rRNA — gen marcador para identificar bacterias en estudios de microbioma.
OTU/ASV — unidades para agrupar secuencias en perfiles de comunidad.
Ejercicios para practicar (con sabor laboral)
Analiza un dataset 16S: de lecturas a tabla de abundancias y diversidad (alfa/beta).
Compara la composición microbiana de dos condiciones con un gráfico de barras apiladas.
Puente a empleo · línea de CV/portafolio
Proyecto (opcional): pipeline básico de metagenómica 16S (QIIME2/DADA2).
CV: “Perfilado de comunidades microbianas (16S) con análisis de diversidad.”
12. Bioproductos y Biodescubrimiento   ·  2 créditos
CONTEXTO
Screening y cribado de compuestos: nociones de bases de datos biológicas y pipelines de búsqueda. Conecta con quimioinformática.
Temario esperado
Descubrimiento de productos naturales y compuestos bioactivos.
Cribado de alto rendimiento (HTS) y bibliotecas de compuestos.
Bases de datos químicas (PubChem, ChEMBL) y nociones de quimioinformática.
Bioprospección y propiedad intelectual.
Glosario clave
HTS — cribado automatizado de miles de compuestos para hallar candidatos.
SMILES — notación de texto que representa estructuras químicas; consultable en bases.
ChEMBL/PubChem — bases de bioactividad y compuestos químicos.
Hit / lead — compuesto candidato inicial / candidato optimizado.
Ejercicios para practicar (con sabor laboral)
Consulta ChEMBL vía API para compuestos activos contra un blanco y arma una tabla.
Filtra una biblioteca por reglas de Lipinski con RDKit.
Puente a empleo · línea de CV/portafolio
Proyecto (opcional): script de consulta automatizada a bases químicas + filtrado de candidatos.
CV: “Consulta programática de bases de bioactividad (ChEMBL) y filtrado quimioinformático de candidatos.”
13. Bio-Nanotecnología   ·  3 créditos
CONTEXTO
Frontera tecnológica; poco código bioinformático directo, pero buen contexto para biosensores y diagnóstico.
Temario esperado
Nanomateriales en biología; nanopartículas y funcionalización.
Biosensores y nanodiagnóstico.
Nanomedicina y entrega dirigida de fármacos.
Caracterización y análisis de datos de nanoescala.
Glosario clave
Nanopartícula — material de escala 1–100 nm con propiedades únicas.
Biosensor — dispositivo que convierte un evento biológico en señal medible.
Funcionalización — unir moléculas a una superficie para darle especificidad.
Ejercicios para practicar (con sabor laboral)
Analiza datos de un biosensor (curva de respuesta) y estima límite de detección.
Puente a empleo · línea de CV/portafolio
Nota: materia de contexto. Apruébala bien; su valor de empleo es indirecto (biosensores/diagnóstico).
Grupo D · Contexto biológico y agro-biotech
Estas materias te dan el marco biológico para interpretar resultados y, si te interesa el nicho agro, la puerta a genómica de plantas (GWAS, selección genómica). No les robes horas al portafolio, pero úsalas para no confundir señal con ruido.
14. Biología Funcional Animal y Vegetal   ·  2 créditos
APOYO
Contexto biológico para interpretar resultados ómicos con criterio; el “sentido común” biológico que evita conclusiones absurdas.
Temario esperado
Fisiología comparada animal y vegetal; sistemas y funciones.
Regulación hormonal y respuesta a estrés.
Metabolismo y homeostasis.
Bases moleculares de la función.
Glosario clave
Homeostasis — mantenimiento del equilibrio interno; marco para interpretar cambios ómicos.
Respuesta a estrés — reprogramación de expresión ante estímulos; explica muchos DEGs.
Fenotipo — rasgo observable resultante de genotipo + ambiente.
Ejercicios para practicar (con sabor laboral)
Toma una lista de genes diferencialmente expresados y explícala con fisiología (no solo estadística).
Puente a empleo · línea de CV/portafolio
Uso: interpretación biológica en los READMEs de tus proyectos ómicos. Es tu credibilidad frente a biólogos.
15. Biotecnología Vegetal   ·  3 créditos
CONTEXTO
Aplicación; poco código directo. Contexto para genómica de plantas si apuntas a agro-biotech.
Temario esperado
Cultivo de tejidos y micropropagación.
Transformación genética de plantas.
Marcadores moleculares en mejoramiento.
Genómica vegetal (nociones).
Glosario clave
Marcador molecular — variante de ADN asociada a un rasgo; guía selección.
Transgénesis — introducir un gen externo en una planta.
QTL — región genómica asociada a un rasgo cuantitativo.
Ejercicios para practicar (con sabor laboral)
Asocia marcadores a un rasgo en un dataset de ejemplo (análisis QTL básico).
Puente a empleo · línea de CV/portafolio
Nota: contexto agro. Valor de empleo solo si eliges ese nicho.
16. Fundamentos de Agronomía y Fitopatología   ·  2 créditos
CONTEXTO
Dominio agrícola; útil si apuntas a agro-biotech o fitomejoramiento.
Temario esperado
Sistemas de cultivo y manejo agronómico.
Enfermedades de plantas: patógenos, diagnóstico, manejo.
Interacción planta-patógeno.
Diagnóstico molecular de fitopatógenos.
Glosario clave
Fitopatógeno — organismo que causa enfermedad en plantas.
Resistencia (gen R) — gen vegetal que confiere defensa contra un patógeno.
Diagnóstico molecular vegetal — detección de patógenos por PCR/secuenciación.
Ejercicios para practicar (con sabor laboral)
Diseña un ensayo PCR para detectar un fitopatógeno (diseño de primers específicos).
Puente a empleo · línea de CV/portafolio
Nota: nicho agro. Conecta con diagnóstico molecular si te interesa el sector.
17. Biotecnología Agrícola   ·  2 créditos
CONTEXTO
Dominio agro; su gancho bioinformático es el GWAS y la selección genómica en cultivos.
Temario esperado
Cultivos mejorados y transgénicos; bioseguridad.
Biofertilizantes y biocontroladores.
Genómica aplicada a la agricultura (GWAS, selección genómica).
Glosario clave
GWAS — estudio de asociación de todo el genoma con un rasgo; mucha estadística.
Selección genómica — predecir valor de mejora con marcadores de todo el genoma.
Heredabilidad — proporción de la variación fenotípica explicada por genética.
Ejercicios para practicar (con sabor laboral)
Corre un GWAS de ejemplo (PLINK) y lee el Manhattan plot.
Puente a empleo · línea de CV/portafolio
Proyecto (opcional): pipeline GWAS con Manhattan plot e interpretación.
CV: “GWAS y selección genómica en cultivos (PLINK), con control de estructura poblacional.”
18. Mejoramiento Genético Vegetal   ·  2 créditos
CONTEXTO
Genómica de plantas; nicho agro. Estadística cuantitativa y marcadores.
Temario esperado
Genética cuantitativa; heredabilidad y ganancia genética.
Selección asistida por marcadores (MAS).
Predicción genómica.
Diseño de esquemas de mejoramiento.
Glosario clave
MAS — selección asistida por marcadores: elegir individuos por su ADN.
BLUP — método estadístico para estimar valores de mejora.
Ganancia genética — mejora esperada por ciclo de selección.
Ejercicios para practicar (con sabor laboral)
Estima valores de mejora (BLUP) en un dataset de ejemplo con R.
Puente a empleo · línea de CV/portafolio
Nota: muy afín a estadística; si te gusta lo cuantitativo, aquí hay nicho.
19. Biotecnología Ambiental   ·  3 créditos
APOYO
Metagenómica ambiental si te interesa ese nicho: comunidades microbianas de suelos, aguas, biorremediación.
Temario esperado
Biorremediación y tratamiento de residuos.
Microbiología ambiental y ciclos biogeoquímicos.
Metagenómica ambiental y monitoreo.
Bioindicadores y calidad ambiental.
Glosario clave
Biorremediación — usar organismos para limpiar contaminantes.
Metagenómica ambiental — secuenciar ADN de una muestra ambiental completa.
Bioindicador — especie/comunidad cuyo estado refleja la salud del ambiente.
Ejercicios para practicar (con sabor laboral)
Analiza un dataset metagenómico ambiental: perfil taxonómico y funcional.
Puente a empleo · línea de CV/portafolio
Proyecto (opcional): pipeline de metagenómica ambiental con perfil taxonómico.
CV: “Metagenómica ambiental: perfilado taxonómico y funcional de comunidades microbianas.”
Grupo E · Marco profesional (tu multiplicador de sueldo)
Estas materias “no técnicas” son tu ventaja secreta: convierten conocimiento en argumento de venta y de precio. El que conecta la técnica con el dinero y con el cumplimiento cobra más.
20. Regulación de la Biotecnología   ·  2 créditos
APOYO
Marco legal y ético que conecta directo con tu diferencial de seguridad de datos clínicos. En pharma/clínica, la confianza vale más que la técnica.
Temario esperado
Marcos regulatorios: bioseguridad, OGM, propiedad intelectual.
Ética en biotecnología y datos.
Protección de datos de salud (HIPAA, GDPR; nociones).
Aprobación de productos y ensayos.
Glosario clave
HIPAA / GDPR — marcos legales de datos de salud (EE. UU. / Europa); exigidos por multinacionales.
Bioseguridad — normas para manejar organismos y materiales con seguridad.
Consentimiento informado — base ética para usar datos/muestras de personas.
Ejercicios para practicar (con sabor laboral)
Redacta cómo tu proyecto de biomarcadores cumpliría nociones de HIPAA/GDPR (acceso, cifrado, anonimización).
Puente a empleo · línea de CV/portafolio
Uso: argumento de entrevista de altísimo valor. Refuerza tu diferencial de seguridad de datos (Rango IV de la Campaña).
CV: “Conocimiento de marcos de datos de salud (HIPAA/GDPR) aplicado a pipelines clínicos.”
21. Sistemas de Gestión de Calidad   ·  2 créditos
APOYO
ISO y buenas prácticas: valioso en farmacéutica y labs clínicos, donde la reproducibilidad es ley. Conecta con tu narrativa de pipelines reproducibles.
Temario esperado
Normas ISO (9001) y buenas prácticas (GLP, GMP).
Documentación, trazabilidad y control de versiones de procesos.
Validación y verificación; auditorías.
Mejora continua (PDCA).
Glosario clave
GLP/GMP — buenas prácticas de laboratorio/manufactura; requisito en pharma.
Trazabilidad — poder rastrear cada resultado a su origen; hermana de la reproducibilidad.
Validación — demostrar que un proceso hace lo que debe, documentado.
Ejercicios para practicar (con sabor laboral)
Documenta un pipeline tuyo con criterios de trazabilidad y validación (como exigiría un lab clínico).
Puente a empleo · línea de CV/portafolio
Uso: argumento que conecta calidad con reproducibilidad (FAIR, CI/CD). Diferenciador en pharma/clínica.
CV: “Prácticas de calidad (ISO/GLP) aplicadas a la reproducibilidad y trazabilidad de análisis.”
22. Bioeconomía   ·  3 créditos
CONTEXTO
Visión de negocio: útil para freelance/startup y para entender el valor de lo que produces. Conecta con tu meta de arbitraje geográfico.
Temario esperado
Modelos de negocio en bioeconomía y bioindustria.
Valorización de bioproductos y servicios.
Innovación, emprendimiento y transferencia tecnológica.
Sostenibilidad y economía circular.
Glosario clave
Propuesta de valor — qué problema resuelves y por qué pagarían por ello.
Transferencia tecnológica — llevar ciencia del laboratorio al mercado.
Cotización por valor — poner precio por el impacto, no por la hora; rompe tu techo de ingreso.
Ejercicios para practicar (con sabor laboral)
Escribe la propuesta de valor de un servicio bioinformático freelance que podrías ofrecer.
Puente a empleo · línea de CV/portafolio
Uso: base para freelance y para tu narrativa de negocio; conecta técnica con dinero.
Grupo F · Tu titulación
23. Integración Curricular   ·  5 créditos
MINA DE ORO
Tu proyecto final y la jugada maestra: haz que tu proyecto de titulación SEA tu proyecto estrella de portafolio. Te titulas Y tienes la pieza que impresiona a reclutadores, respaldada por tu universidad.
Temario esperado
Formulación del problema y objetivos de investigación.
Estado del arte y marco metodológico.
Ejecución del proyecto integrador.
Análisis de resultados y discusión.
Defensa y comunicación científica.
Glosario clave
Proyecto integrador — trabajo que reúne las competencias de la carrera en un producto final.
Reproducibilidad — que otro pueda repetir tu análisis y obtener lo mismo; tu sello profesional.
Defensa — exposición oral donde argumentas tu trabajo bajo preguntas; ensayo de la entrevista técnica.
Ejercicios para practicar (con sabor laboral)
Define tu proyecto de biomarcadores en sangre como proyecto de titulación: problema, datos, método, entregable.
Escribe el README de nivel profesional que servirá tanto para el tribunal como para el reclutador.
Prepara una defensa de 10 minutos: es un ensayo directo del “Dragón” (entrevista técnica).
Puente a empleo · línea de CV/portafolio
Estrategia clave: no hagas dos proyectos distintos; funde el académico con el profesional. Un solo esfuerzo, dos recompensas: título + portafolio estrella.
CV: “Proyecto de titulación: pipeline reproducible de diagnóstico de biomarcadores en sangre con manejo seguro de datos clínicos (respaldado académicamente).”
Mapa de prioridades (resumen de una mirada)
Si solo pudieras exprimir seis materias de esta guía para tu empleo, serían estas. El resto: apruébalas bien y saca de ellas el contexto biológico que hace creíble tu narrativa.
Prioridad
Materia
Lo que te llevas al portafolio
1
Base de Datos y Programación
BD genómica consultable + ETL en Python.
2
Estadística para Bioinformática
Expresión diferencial con control de FDR.
3
Modelización de Sistemas
Modelo de ML con validación biológica.
4
Evolución Molecular y Filogenia
Pipeline filogenético reproducible.
5
Diagnóstico Molecular
Interpretación clínica de tu proyecto estrella.
6
Integración Curricular
El proyecto estrella, respaldado por tu título.