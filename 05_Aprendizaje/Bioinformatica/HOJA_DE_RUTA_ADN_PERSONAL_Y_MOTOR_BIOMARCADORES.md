# 🧬 HOJA DE RUTA: Análisis de ADN Personal & Motor Integrado de Biomarcadores

> [!IMPORTANT]
> **Documento de Visión y Arquitectura Integrada (Genotipo + Fenotipo).**
> Define la hoja de ruta para personalizar el plan de estudios con tus propios datos genéticos, la lista de pendientes para adquirir/practicar, y el **Puente Arquitectónico** que conecta el Variant Calling de ADN con tu motor de recomendación de biomarcadores para laboratorios clínicos y el ecosistema universitario.

---

## 📑 Tabla de Contenidos
- [1. El Propósito: Aprender para Uno Mismo y Servir a la Comunidad](#1-el-propósito-aprender-para-uno-mismo-y-servir-a-la-comunidad)
- [2. Lista de Pendientes para Personalizar tu ADN](#2-lista-de-pendientes-para-personalizar-tu-adn)
- [3. El Puente Arquitectónico: Genotipo (VCF) ↔ Fenotipo (Biomarcadores)](#3-el-puente-arquitectónico-genotipo-vcf--fenotipo-biomarcadores)
- [4. Aplicación en el Taller MVP & Laboratorios Universitarios](#4-aplicación-en-el-taller-mvp--laboratorios-universitarios)
- [5. Fases de Implementación en el Plan Maestro](#5-fases-de-implementación-en-el-plan-maestro)

---

## 🎯 1. El Propósito: Aprender para Uno Mismo y Servir a la Comunidad

Este proyecto no nace como un ejercicio pasivo de clase, sino como un **motor de aprendizaje personal y de impacto real**:

1. **Motivación Intrínseca (Tu propio ADN):** Al procesar tu propia secuencia biológica, cada variante ($Q$-score, SNP, alineamiento) tiene significado personal. Se acaba la abstracción.
2. **Impacto Comunitario y Universitario:** La tecnología construida para ti se empaqueta en la plataforma **Bull.Tech / Taller MVP**, permitiendo a laboratorios clínicos universitarios y estudiantes analizar biomarcadores alterados con inteligencia bioinformática integrada.

---

## 📋 2. Lista de Pendientes para Personalizar tu ADN

Para llevar a producción tu propio análisis genético, estos son los pendientes categorizados por fases (desde $0 USD hasta la versión completa):

### 🆓 Fase A: Inmediata y Gratuita ($0 USD)
- [x] **Claves SSH & Entornos de Cómputo:** Configurado en WSL AlmaLinux y Git (`R1-XUB-008`).
- [ ] **Muestra de Control Genómico Estándar (GIAB HG002 / NA12878):** Descargar FASTQ y VCF crudos del NIST (EE.UU.) para calibrar tus pipelines en WSL y AWS antes de usar tu propio ADN.
- [ ] **Créditos AWS Educate / GCP:** Solicitar el bono de $300 - $1,000 USD de crédito educativo para ejecutar pipelines cloud sin costo.

### 💳 Fase B: Genotipado por Microarrays ($50 - $99 USD)
- [ ] **Adquisición de Kit de ADN (AncestryDNA / 23andMe / MyHeritage):**
  - *Materia prima obtenida:* Archivo `raw_data.txt` con ~700,000 SNPs genotipados.
  - *Uso:* Construir el primer motor en Python/pandas que lea tus SNPs de baja densidad y los cruce con la base de datos `dbSNP` y `ClinVar`.

### 🧪 Fase C: Genoma Completo 30x / Exoma WES ($149 - $299 USD - Promociones)
- [ ] **Adquisición de WGS 30x / WES (Nebula Genomics / Dante Labs):**
  - *Materia prima obtenida:* Archivos `FASTQ.gz` (~100 GB), `BAM` (~60 GB) y `VCF` (~1 GB).
  - *Uso:* Correr tu pipeline completo e2e en **Nextflow DSL2 + Docker + AWS Batch**, ejecutando variant calling con `GATK HaplotypeCaller` y anotación de impacto clínico.

---

## 🌉 3. El Puente Arquitectónico: Genotipo ↔ Fenotipo ↔ Estructura ↔ Awareness

Existe un **puente biológico, estructural y computacional directo** entre las 4 capas del sistema:

```mermaid
graph TD
    subgraph CAPA 1: GENOTIPO (ADN Fijo)
        A[Archivo VCF / SNPs] -->|Variantes p.ej. MTHFR, CYP2D6| B[Predisposición & Farmacogenómica CPIC]
    end
    
    subgraph CAPA 2: FENOTIPO (Fisiología Dinámica)
        C[Analítica Sanguínea / HMDB] -->|Biomarcadores p.ej. Homocisteína, ApoB, HOMA-IR| D[Estado Metabólico Funcional]
    end

    subgraph CAPA 3: ESTRUCTURA & CADD (IA Molecular)
        E[Modelado 3D Boltz-2 / DiffDock] -->|Afinidad ligando-receptor Kd| F[Intervención Fito-Farmacológica Precisa]
    end

    B & D & F --> G{MOTOR INTEGRADO BULL.TECH<br/>Optimizador Pleiotrópico}

    subgraph CAPA 4: AWARENESS MECANÍSTICO (XAI)
        G --> H[Reporte Causal al Paciente]
        H --> I1[Explicación Bioquímica: mTOR/AMPK/Circadiano]
        H --> I2[Crononutrición & Hábitos Estratégicos]
        H --> I3[Fitoterapia Biodisponible sin Toxicidad]
    end
```

### 💡 Ejemplo Práctico de Integración (El Caso MTHFR / CYP2D6 / Homocisteína):

1. **Analítica de Sangre (Fenotipo):** El examen de laboratorio del paciente muestra **Homocisteína elevada (18 µmol/L)** e índice HOMA-IR alto.
2. **Análisis de ADN (Genotipo):** El archivo VCF revela homocigosis en **`MTHFR C677T (TT)`** (reducción del 65% en la actividad de la enzima) y metabolizador intermedio en citocromo **`CYP2D6*4`**.
3. **Capa Estructural / CADD:** Boltz-2 y DiffDock evalúan la cavidad catalítica de la enzima mutada frente a sustratos sintéticos vs. formas reducidas y cofactores activos.
4. **La Acción del Motor Integrado (Awareness XAI):**
   - El motor no solo dice "toma esta pastilla".
   - **Explicación al Paciente:** *"Tu variante genética MTHFR disminuye la velocidad para transformar el ácido fólico inactivo. Al combinarse con cenas tardías ricas en carbohidratos, se eleva la homocisteína y se frena la metilación hepática. Recomendamos sincronizar la ingesta de alimentos con tu ventana de luz natural (8 AM – 6 PM) y utilizar L-metilfolato (forma activa 5-MTHF) junto con colina para desviar la remetilación vía BHMT."*

---

## 🏭 4. Aplicación en el Taller MVP & Laboratorios Universitarios

Esta arquitectura se despliega modularmente en tu proyecto comercial/universitario:

1. **Fase MVP Inicial (Laboratorios Clínicos Básicos):**  
   Ingesta de datos de análisis de sangre (Valores del biomarcador vs Rangos de Referencia Estadísticos) $\rightarrow$ Motor de alertas y recomendaciones de hábitos.
2. **Fase MVP Avanzada (Módulo Genómico & Farmacogenómica):**  
   Carga del archivo VCF/RAW de ADN del paciente $\rightarrow$ El motor cruza variantes enzimáticas con guías **CPIC/PharmGKB** y biomarcadores alterados.
3. **Fase MVP Pro (Capa Estructural con IA & XAI Educativo):**  
   Cribado de fitocompuestos con **Boltz-2 / DiffDock / RDKit** + Generador de reportes visuales causales para el paciente.

---

## 📅 5. Fases de Implementación en el Plan Maestro

- **Rango II (Semana 5–9):** Práctica del flujo NGS con dataset gratis `HG002` (GIAB) para dominar el archivo VCF.
- **Rango III (Semana 10–14):** Automatización del pipeline de Variant Calling en **Nextflow DSL2 + Docker**.
- **Rango IV (Semana 15–19):** Despliegue en **AWS Cloud** + Cifrado HIPAA/GPG de datos de ADN.
- **Rango V / MVP (Semana 20–25):** Integración del **Motor de Recomendación Genotipo ↔ Fenotipo** y presentación del proyecto estrella.

---

*Documento vivo de arquitectura. Registrado en el repositorio `empleoBio`.*
