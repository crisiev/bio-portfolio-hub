# 🧬 `seq-stats` — Toolkit Bioinformático de Secuencias & Métricas de Ensamblaje (P1)

![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)
![Build Status](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Bioinformatics](https://img.shields.io/badge/domain-NGS%20%26%20Genomics-orange.svg)

`seq-stats` es un paquete modular en Python y herramienta CLI diseñada para el análisis de secuencias genómicas, cálculo de métricas de calidad de ensamblaje (*N50 / L50*), contenido %GC, distancia Hamming y control de calidad NGS.

---

## 🚀 Quickstart & Instalación

### 1. Clonar el Repositorio y Crear el Entorno
```bash
git clone https://github.com/crisiev/bio-portfolio-hub.git
cd bio-portfolio-hub
mamba env create -f environment.yml
conda activate bio-env





# 🧬 empleoBio — Codebase Fundacional de Christian

> [!IMPORTANT]
> Base de conocimiento y trabajo para:
> 1. Conseguir su primer empleo junior de bioinformática a través de un **Portafolio Multivariado en GitHub**.
> 2. Construir **software propio vendible** en su ecosistema universitario.
>
> **Entornos de desarrollo:** Rocky Linux (Main), AthenaOS, Xubuntu conectados vía WSL/GitHub.
> **Metodología:** El LLM guía, Christian codea manualmente (ver [`AGENTS.md`](./AGENTS.md)).

**Dueño:** cjalcivar@gmail.com · **Inicio:** julio 2026 · **Modo:** Práctica deliberada tecleada a mano.

---

## 📑 Tabla de Contenidos
- [1. Mapa de Navegación Rápida](#1-mapa-de-navegación-rápida)
- [2. Estructura de los 5 Pilares](#2-estructura-de-los-5-pilares)
- [3. Árbol de Carpetas del Proyecto](#3-árbol-de-carpetas-del-proyecto)
- [4. Estado Actual y Próximo Paso](#4-estado-actual-y-próximo-paso)

---

## 🧭 1. Mapa de Navegación Rápida

| Si buscas… | Ve a |
|------------|------|
| Cómo debe comportarse un LLM aquí | **[`AGENTS.md`](./AGENTS.md)** |
| **Guía de Colaboración y Manifiesto** | **[`CONTRIBUTING.md`](./CONTRIBUTING.md)** |
| **Plan completo con horas medidas** | **[`PLAN_MAESTRO.md`](./PLAN_MAESTRO.md)** ← fuente de verdad operativa |
| Reglas de nombres y arquitectura | **[`CONVENCIONES.md`](./CONVENCIONES.md)** |
| **01 Estrategia de Empleo** (Suite 01 al 08) | **[`01_Estrategia/`](./01_Estrategia/)** |
| **02 Sistema Gamificado** (La Campaña 01 al 04) | **[`02_Campana/`](./02_Campana/)** |
| **03 Taller de Producto Comercial** | **[`03_Taller_MVP/`](./03_Taller_MVP/)** |
| **04 Registro Fechado de Práctica** | **[`04_Bitacora/`](./04_Bitacora/)** |
| **05 Notas de Estudio por Dominio** | **[`05_Aprendizaje/`](./05_Aprendizaje/)** |

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 📚 2. Estructura de los 5 Pilares

> [!NOTE]
> La codebase está organizada en **5 nodos pilares limpios y numerados** para garantizar una navegación de alta eficiencia tanto en la terminal como en GitHub.

### 💼 Pilar 1: [`01_Estrategia/`](./01_Estrategia/) (Suite de Empleo & Carrera)
- [`01_Auditoria_y_Estrategia_Salarial_2026.md`](./01_Estrategia/01_Auditoria_y_Estrategia_Salarial_2026.md) — Mercado, brechas y techos salariales.
- [`02_Guia_de_Silabos_Materias_Pendientes.md`](./01_Estrategia/02_Guia_de_Silabos_Materias_Pendientes.md) — Las 23 materias pendientes con glosario y ejercicios.
- [`03_Perfil_Ideal_y_CV.md`](./01_Estrategia/03_Perfil_Ideal_y_CV.md) — Perfil objetivo, CV ES/EN, LinkedIn y keywords ATS.
- [`04_Plan_de_Proyectos_de_Portafolio.md`](./01_Estrategia/04_Plan_de_Proyectos_de_Portafolio.md) — Los repos de GitHub que demuestran el stack.
- [`05_IA_Horizonte_y_Recursos.md`](./01_Estrategia/05_IA_Horizonte_y_Recursos.md) — IA/LLMs, tendencias, recursos y autoevaluación.
- [`06_Taller_MVP_Ideas_y_Sprints.md`](./01_Estrategia/06_Taller_MVP_Ideas_y_Sprints.md) — Mentalidad, ideas, arquitectura y sistema de sprints.
- [`07_Mercado_Universitario_y_Precio.md`](./01_Estrategia/07_Mercado_Universitario_y_Precio.md) — Ideas por audiencia y filosofía de precio.
- [`08_Expediente_BioSocial_y_Networking.md`](./01_Estrategia/08_Expediente_BioSocial_y_Networking.md) — Ecosistema social, Discords, campaña Reddit e inglés C1.

### 🎮 Pilar 2: [`02_Campana/`](./02_Campana/) (Sistema Gamificado Baseline)
- [`01_La_Campana_Sistema_Gamificado.md`](./02_Campana/01_La_Campana_Sistema_Gamificado.md)
- [`02_Registro_de_Campana_Ejercicios.md`](./02_Campana/02_Registro_de_Campana_Ejercicios.md)
- [`03_Glosario_Maestro_Bioinformatica.md`](./02_Campana/03_Glosario_Maestro_Bioinformatica.md)
- [`04_Roadmap_Bioinformatica_Junior.md`](./02_Campana/04_Roadmap_Bioinformatica_Junior.md)

### 🏬 Pilar 3: [`03_Taller_MVP/`](./03_Taller_MVP/) (Producto Comercial)
- [`IDEAS.md`](./03_Taller_MVP/IDEAS.md) · [`TABLERO.md`](./03_Taller_MVP/TABLERO.md) · [`Roadmap_Monetizacion.md`](./03_Taller_MVP/Roadmap_Monetizacion.md) · [`Modelo_de_Valor/`](./03_Taller_MVP/Modelo_de_Valor/README.md)

### 📓 Pilar 4: [`04_Bitacora/`](./04_Bitacora/) (Registros Fechados & Git)
- [`README.md`](./04_Bitacora/README.md) · [`_PLANTILLA_dia.md`](./04_Bitacora/_PLANTILLA_dia.md) · [`2026-07.md`](./04_Bitacora/2026-07.md)

### 📖 Pilar 5: [`05_Aprendizaje/`](./05_Aprendizaje/) (Notas de Estudio por Dominio)
- [`Linux/`](./05_Aprendizaje/Linux/README.md) · [`Python/`](./05_Aprendizaje/Python/README.md) · [`Git/`](./05_Aprendizaje/Git/README.md) · [`SQL/`](./05_Aprendizaje/SQL/README.md) · [`Bioinformatica/`](./05_Aprendizaje/Bioinformatica/README.md)

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 🗂️ 3. Árbol de Carpetas del Proyecto

```
empleoBio/
├── README.md                 ← este mapa
├── AGENTS.md                 ← manual para cualquier LLM (la mecánica)
├── PLAN_MAESTRO.md           ← ★ 404.5h calendarizadas, 25 semanas, día por día
├── CONVENCIONES.md           ← nomenclatura y estructura
├── .gitignore                ← reglas de exclusión de datos pesados (FASTQ, BAM, VCF)
├── .gitattributes            ← normalización de saltos de línea LF (Linux/WSL)
│
├── .github/                  ← plantillas profesionales de Pull Request e Issues
├── data/                     ← gestión de datasets (raw, processed, reference)
├── scripts/                  ← utilidades y automatización
├── scratch/                  ← borradores y experimentos aislados
├── _archivacion/             ← respaldas .docx, .xlsx y .txt originales intactos
│
├── 01_Estrategia/            ← [PILAR 1] Documentos 01 al 08 (Empleo, Carrera, Redes)
├── 02_Campana/               ← [PILAR 2] Documentos 01 al 04 (Sistema Gamificado Baseline)
├── 03_Taller_MVP/            ← [PILAR 3] Taller MVP (IDEAS, TABLERO, Modelo_de_Valor, Proyectos)
├── 04_Bitacora/              ← [PILAR 4] Registros Fechados & Certificación Git
└── 05_Aprendizaje/           ← [PILAR 5] Notas de Estudio Escritas a Mano por Dominio
```

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## ▶️ 4. Estado Actual y Próximo Paso

> [!TIP]
> **Rango Actual:** Rango I (Aprendiz de Terminal) · **XP:** 445 / 600 · **Semana 4 EN CURSO (Día 1 completado)** · **Siguiente Tarea:** `R1-BOSS-01` (Día 2: Redacción final de badges/docs + Cierre de Rango I con +250 XP).

- **Proyecto P1 Destacado (`src/seq_stats`):** Toolkit modular en Python y CLI para cálculo de N50/L50, %GC, complemento reverso y distancia Hamming. Verificado con `pytest` (`4 passed in 0.36s`) y entorno reproducible `environment.yml`.
- **Plan Maestro:** [`PLAN_MAESTRO.md`](./PLAN_MAESTRO.md) — **404.5 horas calendarizadas**, 56 ejercicios + 5 jefes en 25 semanas. Fuente de verdad operativa.
- **Empleo:** Plan completo en [`01_Estrategia/`](./01_Estrategia/).
- **Producto:** Estructura lista en [`03_Taller_MVP/`](./03_Taller_MVP/). MVP arranca en Semana 4 Día 3 con `MVP-001`.
- **Infraestructura:** WSL2 + AlmaLinux-9 + Git SSH activo + repo `bio-portfolio-hub` en GitHub.

[⬆️ Volver al inicio](#-tabla-de-contenidos)
