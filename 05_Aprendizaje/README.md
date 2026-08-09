# 📖 Aprendizaje — Tus Notas Escritas a Mano

> [!IMPORTANT]
> **Aquí vives tú, no el LLM.** Un subfolder por dominio. La regla de [`AGENTS.md`](../AGENTS.md):  
> **El LLM te guía; tú escribes cada nota y cada línea de código.** Escribir con tus palabras es lo que convierte *"vi un tutorial"* en *"lo domino"*.

---

## 📑 Tabla de Contenidos
- [1. Subcarpetas por Dominio](#1-subcarpetas-por-dominio)
- [2. Cómo Usar Cada Nota](#2-cómo-usar-cada-nota)

---

## 🗂️ 1. Subcarpetas por Dominio

- [`Linux/`](./Linux/README.md) — Comandos, permisos, procesos, SSH, bash scripting, administración. Tu oficina diaria.
- [`Python/`](./Python/README.md) — Fundamentos, pandas, Biopython, FastAPI, tests.
- [`Git/`](./Git/README.md) — Versionado, ramas, flujo colaborativo, GitHub.
- [`SQL/`](./SQL/README.md) — Modelo relacional, consultas, diseño de esquemas.
- [`Bioinformatica/`](./Bioinformatica/README.md) — NGS, formatos, pipelines, estadística aplicada, IA/foundation models.
  - 📖 **[Glosario Maestro de Formatos & Herramientas](./Bioinformatica/GLOSARIO_FORMATOS_Y_HERRAMIENTAS.md)** (VCF, SAM, GFF, FastQC, Nextflow, Snakemake).

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## ⚙️ 2. Mecanismo Global para LLMs: Captura de Conocimiento & Pivoteo de Skills

> [!IMPORTANT]
> **Instrucción Operativa para cualquier LLM en esta codebase:**
> 1. **Centralización por Dominio:** Cada vez que en una sesión se expliquen conceptos teóricos nuevos, formatos de datos (ej. VCF, BAM, GFF), arquitecturas o herramientas, el LLM debe indicar o actualizar la nota correspondiente dentro de `05_Aprendizaje/<Dominio>/`.
> 2. **Diferenciación Clara:**
>    - `04_Bitacora/`: Registra el *diario de avance* (qué se hizo hoy, horas, XP, comandos específicos).
>    - `05_Aprendizaje/`: Registra la *Base de Conocimiento / Obsidian Vault* (los conceptos teóricos en limpio para repaso continuo).
> 3. **Refuerzo de Puntos Débiles (Pivoteo):** Antes de cada Checkpoint o Boss Fight, el LLM debe consultar este directorio para identificar temas flojos y plantear ejercicios de refuerzo personalizados.

---

## ✍️ 3. Cómo Usar Cada Nota

Para cada tema que estudies, crea `AAAA-MM-DD_tema.md` o actualiza el Glosario del dominio y escribe:
1. **Qué es** (en tus palabras, no copiado).
2. **Cómo se usa** (comando/código que TÚ tecleaste y probaste).
3. **Un ejemplo propio** (no el del tutorial).
4. **Dónde me atoré** y cómo lo resolví.

> [!TIP]
> Estas notas + tus commits son la prueba real de que no usaste "vibe coding". Registra tu avance diario en tu [`../04_Bitacora/README.md`](../04_Bitacora/README.md).

[⬆️ Volver al inicio](#-tabla-de-contenidos)
