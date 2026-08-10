# 📊 Modelo de Valor y Registro de Precio (Tracker en Markdown)

> [!IMPORTANT]
> **Brújula de Precio Respaldada por Evidencia**  
> Empiezas en $0 y cada commit/feature suma valor mensual justificado hacia un precio que puedas defender ante usuarios y reclutadores.

---

## 📑 Tabla de Contenidos
- [1. Tiers de Precio](#1-tiers-de-precio)
- [2. Registro de Valor Acumulado (Libro Mayor)](#2-registro-de-valor-acumulado-libro-mayor)
- [3. Modelo de Crecimiento y Simulación](#3-modelo-de-crecimiento-y-simulación)
- [4. Reglas de Cotización y Filosofía](#4-reglas-de-cotización-y-filosofía)
- [5. Matriz de Valoración de Mercado Individual (Personal Market Rate)](#5-matriz-de-valoración-de-mercado-individual-personal-market-rate)
- [6. Realidad Empírica del Mercado Local en Ecuador (Auditoría 2026)](#6-realidad-empírica-del-mercado-local-en-ecuador-auditoría-2026)

---

## 💵 1. Tiers de Precio

| Tier | Rango de Valor Acumulado ($/mes ahorrado) | Precio Sugerido (USD) | Descripción |
|------|-------------------------------------------|-----------------------|-------------|
| **Tier 0 (Freemium / Gratis)** | $0.00 – $4.99 / mes | **$0.00** | Funcionalidad básica para captar usuarios. |
| **Tier 1 (Básico / Estudiantil)** | $5.00 – $14.99 / mes | **$1.99 / mes** | Ahorro directo de tiempo en tareas pequeñas. |
| **Tier 2 (Pro / Tesis)** | $15.00 – $49.99 / mes | **$4.99 / mes** | Herramientas avanzadas, exportación y análisis. |
| **Tier 3 (Institucional / Lab)** | $50.00+ / mes | **$9.99 / usuario / mes** | Multi-usuario, pipelines reproducibles e integración. |

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 📝 2. Registro de Valor Acumulado (Libro Mayor)

> [!TIP]
> **Instrucción de uso diario:**  
> Cada vez que cierres un ticket en Git, añade una fila en esta tabla con el valor estimado de ahorro mensual que le genera al usuario final.

| Fecha | Ticket / Feature | Descripción del Valor Aportado | Valor Est. ($/mes) | Acumulado Total ($/mes) | Tier Desbloqueado |
|-------|------------------|--------------------------------|-------------------|------------------------|-------------------|
| 2026-07-29 | `MVP-001` | Setup inicial de arquitectura FastAPI | $0.00 | $0.00 | Tier 0 (Gratis) |
| *Ejemplo* | `MVP-002` | Parser automático de archivos FASTA | +$2.50 | $2.50 | Tier 0 (Gratis) |
| *Ejemplo* | `MVP-003` | Algoritmo de cálculo de Tm y primers | +$3.50 | $6.00 | **Tier 1 ($1.99)** |

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 📈 3. Modelo de Crecimiento y Simulación

> [!NOTE]
> **Proyección de Usuarios & Ingresos Mensuales Recurrentes (MRR):**

| Escenario | Usuarios Activos | Tier Dominante | Precio Promedio | MRR Estimado (USD) |
|-----------|------------------|----------------|-----------------|-------------------|
| **Inicial (Validación)** | 10 | Tier 1 (Básico) | $1.99 | **$19.90 / mes** |
| **Conservador** | 50 | Tier 1 (Básico) | $1.99 | **$99.50 / mes** |
| **Objetivo Local** | 100 | Tier 2 (Pro) | $4.99 | **$499.00 / mes** |
| **Escala Regional** | 300 | Tier 2 (Pro) | $4.99 | **$1,497.00 / mes** |

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## ⚖️ 4. Reglas de Cotización y Filosofía

1. **El precio no es el costo de desarrollo:** Es la fracción del valor/tiempo ahorrado al usuario.
2. **Ecuador = Internacional:** Al cotizar en USD, el precio local es idéntico al internacional ($1.99 USD en Ecuador es una ganga afuera).
3. **Validación primero:** No cobres $50 hasta no tener 10 personas felices pagando $1.99.

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 🎯 5. Matriz de Valoración de Mercado Individual (Personal Market Rate)

> [!IMPORTANT]
> **Ponderador de Cotización Personal — Cero Complacencia**  
> Vincula tu XP acumulada y Horas auditadas en `PLAN_MAESTRO.md` con tu valor de mercado medido (Remoto Contractor LatAm-to-US vs. Local Ecuador).  
> *Regla de Oro:* El mercado paga por **riesgo de negocio eliminado y reproducibilidad de código**, no por intenciones.

| Rango | Semanas | Horas Acum. | XP Medida | Entregables Clave en GitHub | Remoto Int. (Suelo Conservador) | Remoto Int. (Techo Agresivo Startups) | Local Ecuador (Mercado Medido) | Nivel Técnico Real |
|-------|---------|------------|-----------|-----------------------------|---------------------------------|--------------------------------------|--------------------------------|-------------------|
| **Rango I** | Sem 1–3 | 0 – 57 h | 0 – 600 | Scripting Bash/Python QC + Git + Profile README | **$400 – $600 / mes** | $800 / mes | **$480 – $650 / mes** | **Trainee / Pasante Scripting** |
| **Rango II** | Sem 4–8 | 58 – 120 h | 601 – 1500 | Pipeline NGS manual (BWA, GATK, DESeq2) | **$1,000 – $1,400 / mes** | $1,800 / mes | **$900 – $1,200 / mes** | **Analista NGS Junior (Asistido)** |
| **Rango III** | **Sem 9–14** | **121 – 210 h** | **1501 – 2500** | **Nextflow DSL2 + Docker + HPC SLURM + 3 Repos** | 🎯 **$1,800 – $2,200 / mes** | **$2,500 / mes** | **$1,200 – $1,600 / mes** | **Junior Bioinformatician Autónomo** |
| **Rango IV** | Sem 15–19 | 211 – 315 h | 2501 – 3200 | Cloud AWS S3/Batch + Rocky HPC + HIPAA/GDPR | **$2,200 – $2,800 / mes** | $3,400 / mes | **$1,600 – $2,000 / mes** | **Bioinformatics Cloud & Sec Junior** |
| **Rango V** | **Sem 20–29** | **316 – 465 h** | **3201 – 3890** | **ML Biomarcadores + Dragón + 5 Repos + scRNA** | 🚀 **$3,000 – $3,800 / mes** | **$4,500 – $5,000 / mes** | **$2,000 – $2,500 / mes** | **Junior Sólido con Destellos Senior** |

---

### 💡 Desglose de Realidad de Mercado (Anti-Ilusión)

1. **¿Por qué la Semana 14 (Rango III) es el punto de postulación internacional ($1,800 – $2,500 / mes)?**
   * **El motivo:** Al dominar **Nextflow DSL2 + Docker**, eliminas el mayor dolor de cabeza de los laboratorios: *"el código de un estudiante que solo corre en su máquina y se rompe al cambiar de servidor"*.
   * **La verdad salarial:** $1,800 – $2,200 USD/mes es el suelo realista conservador de entrada en remoto desde LatAm para Startups/Contractors. Pedir $2,500/mes es el techo agresivo para candidatos de Rango III que destaquen en vivo.

2. **¿Cómo se alcanza el techo de $4,500 – $5,000 / mes?**
   * **No es por acumular semanas en el papel, es por la combinación de Rango V:** Cloud AWS S3/Batch + ML en genómica sin data leakage + Contribución aceptada en `nf-core` + Entrevista en inglés fluida (El Dragón).
   * Cifras de **$5,000 USD/mes ($60,000 USD/año)** corresponden al techo de entrada de contratistas remotos altamente competitivos en EE. UU./Europa o al salto tras 1–2 años de experiencia probada en la industria (transición a Mid-Level).

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 🇪🇨 6. Realidad Empírica del Mercado Local en Ecuador (Auditoría 2026)

> [!NOTE]
> **Datos de Mercado Medidos (Multitrabajos, Computrabajo, LOSEP y Sector Farma/Acuícola 2026):**

| Rol en Ecuador | Rango Salarial Real (USD/mes) | Fuente de Evidencia en Mercado |
|----------------|-------------------------------|--------------------------------|
| **Desarrollador Junior / Programador** | **$480 – $750 / mes** | Promedios en Multitrabajos / Computrabajo Ecuador ($517–$670 prom.). |
| **Analista de Datos Junior** | **$600 – $900 / mes** | Pretensión promedio en portales ($866/mes) con SQL + Python + Excel. |
| **Analista de Laboratorio Clínico/Calidad** | **$630 – $900 / mes** | Promedio sector privado e insumos industriales ($630 prom.). |
| **Ingeniero en Biotecnología (Recién Graduado)**| **$900 – $1,200 / mes** | Escala inicial industria agro/acuícola y laboratorios especializados. |
| **Especialista Junior en Bioinformática** | **$1,200 – $1,600 / mes** | Centros de investigación, farma privada y consultoría técnica. |
| **Especialista Senior / LOSEP Público Escala Alta**| **$1,800 – $2,500 / mes** | Techo máximo local en laboratorios estatales o multinacionales. |

> [!TIP]
> **Conclusión de Mercado Local vs. Remoto:**  
> En Ecuador, el techo local para un Bioinformático con experiencia o posgrado llega a **$2,500 USD/mes**. En cambio, el mercado **Remoto Internacional arranca en $2,000 USD/mes (Semana 14)** y escala a **$4,500–$5,000 USD/mes**. Por eso tu plan prioriza el remoto internacional.

[⬆️ Volver al inicio](#-tabla-de-contenidos)


