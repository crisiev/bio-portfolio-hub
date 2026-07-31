# 📐 CONVENCIONES.md — Arquitectura y Estándares de la Codebase

> [!NOTE]
> Reglas simples, estrictas y adaptadas a tu caso específico para que la carpeta sea navegable por ti y por cualquier LLM, y crezca con orden sin volverse un desorden.

---

## 📑 Tabla de Contenidos
- [1. Nomenclatura](#1-nomenclatura)
- [2. Estructura (Dónde va cada cosa)](#2-estructura-dónde-va-cada-cosa)
- [3. Reglas de Crecimiento](#3-reglas-de-crecimiento)
- [4. Convención de Commits](#4-convención-de-commits-conventional-commits--os-tag-en-inglés)
- [5. Idioma & Estrategia de Demostración](#5-idioma--estrategia-de-demostración-show-dont-tell)
- [6. Ergonomía Cognitiva y Límites de Archivo (Límite Anti-Monolito)](#6-ergonomía-cognitiva-y-límites-de-archivo-límite-anti-monolito)
- [7. Arquitectura de Software & Estándares de Código](#7-arquitectura-de-software--estándares-de-código)
- [8. Optimización RAG & LLMs (Indexación de Conocimiento)](#8-optimización-rag--llms-indexación-de-conocimiento)
- [9. Metodología TDD / Contract-First](#9-metodología-tdd--contract-first-red-green-refactor)
- [10. Escalera de Verificación (Verification Ladder)](#10-escalera-de-verificación-verification-ladder)
- [11. Mapa de Fuentes de Verdad (Source of Truth)](#11-mapa-de-fuentes-de-verdad-source-of-truth)
- [12. Privacidad y Ética de Datos Genómicos](#12-privacidad-y-ética-de-datos-genómicos)

---

## 🏷️ 1. Nomenclatura

- **Documentos de estrategia:** Prefijo numérico de dos dígitos + `snake_case`: `03_Perfil_Ideal_y_CV.md`.
- **Carpetas:** `PascalCase` o `Snake_Case` con inicial mayúscula e índice numérico para pilares: `01_Estrategia/`, `03_Taller_MVP/`.
- **Notas y logs:** `AAAA-MM.md` (bitácora mensual), `AAAA-MM-DD_tema.md` para notas puntuales.
- **Plantillas:** Prefijo `_PLANTILLA_` para que floten arriba y no se confundan con contenido real.
- **Tickets:** `PREFIJO-###` (ej. `MVP-001`, `R1-XUB-001`). El prefijo indica el sistema.

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 🗂️ 2. Estructura (Dónde va cada cosa)

| Tipo de contenido | Ubicación |
|-------------------|-----------|
| **Gobernanza** (cómo trabajar) | Raíz: [`README.md`](./README.md), [`AGENTS.md`](./AGENTS.md), [`CONVENCIONES.md`](./CONVENCIONES.md), [`PLAN_MAESTRO.md`](./PLAN_MAESTRO.md) |
| **01 Estrategia** (fuente de verdad) | [`01_Estrategia/`](./01_Estrategia/) — Documentos `01_` a `08_` |
| **02 Campaña** (sistema gamificado) | [`02_Campana/`](./02_Campana/) — Baselines `01_` a `04_` |
| **03 Taller MVP** (producto y negocio) | [`03_Taller_MVP/`](./03_Taller_MVP/) |
| **04 Bitácora** (registro fechado & Git) | [`04_Bitacora/`](./04_Bitacora/) |
| **05 Aprendizaje** (notas por dominio) | [`05_Aprendizaje/`](./05_Aprendizaje/) |
| **Control de Git & CI/CD** | `.gitignore`, `.gitattributes`, `.github/` (templates de PR e Issues) |
| **Datos genómicos & datasets** | `data/raw/`, `data/processed/`, `data/reference/` (excluidos de Git via `.gitignore`) |
| **Scripts & Utilidades** | `scripts/` (automatizaciones, descarga NCBI, setup) |
| **Borradores & Pruebas** | `scratch/` (pruebas aisladas de un solo uso, ignoradas por Git) |

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 📏 3. Reglas de Crecimiento

> [!IMPORTANT]
> **Prohibición Absoluta de `.docx`:** Todo documento de texto, estrategia o nota debe ser obligatoriamente `.md`. El texto plano es la única fuente de verdad para garantizar velocidad, cero corrupción y compatibilidad con Git/LLMs.

1. **Un tema, un archivo.** No mezcles estudio de Linux con notas de un MVP. Si dudas dónde va, mira la tabla de estructura.
2. **Cada carpeta nueva lleva un `README.md`** de una línea que diga qué contiene. Así el mapa nunca se pierde.
3. **Actualiza `README.md` raíz** cuando agregues una carpeta o documento importante (una línea en el árbol).
4. **Git manda.** Todo cambio serio = un commit con mensaje real. La fecha del commit es tu respaldo de experiencia comprobable.

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 💬 4. Convención de Commits (Conventional Commits + OS Tag en Inglés)

Formato: `type(scope-os): short description in English`

> [!TIP]
> **Ejemplos prácticos de commits:**
> - `feat(infra-rocky): configure dnf package manager and systemd services`
> - `infra(wsl): setup SSH ed25519 authentication for GitHub integration`
> - `feat(mvp-xubuntu): implement /tm endpoint using Biopython parser`
> - `docs(governance): update project roadmap and English commit rules`

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 🌐 5. Idioma & Estrategia de Demostración (Show, Don't Tell)

1. **Inglés Técnico Profesional (100% en GitHub):**
   - **Commits, PRs, Issues, Comentarios de código, Readmes de proyectos y ADRs (Architecture Decision Records):** **100% en Inglés.**
   - Esto actúa como prueba viva e irrefutable de tu fluidez en inglés (C1/B2) ante reclutadores internacionales de EE.UU. y Europa.
2. **Notas internas de estudio y bitácora personal:** Pueden ser en Español o Spanglish técnico en tus archivos locales de estudio.

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 🧠 6. Ergonomía Cognitiva y Límites de Archivo (Límite Anti-Monolito)

> [!WARNING]
> **Estándar de Longitud Basado en Memoria de Trabajo (Miller's Law 7±2):**
> 1. **Archivos Markdown (`.md`):** Máximo **600 a 800 líneas**. Si un documento supera las 800 líneas, debe dividirse modularmente en una subcarpeta dedicada con su respectivo `README.md` (evita fatiga visual y degradación de atención en LLMs).
> 2. **Archivos de Código (`.py`, `.sh`, `.nf`):** Máximo **200 a 300 líneas por módulo**. Queda **estrictamente prohibido crear scripts monolíticos de 1,000 o 10,000 líneas**.

### ¿Por qué prohibimos el script monolítico gigante?
- **Fricción para Tests:** Un script de 5,000 líneas no se puede probar con unit tests aislados (`pytest`).
- **Filtro de Reclutador:** Los ingenieros senior rechazan código spaghetti monolítico.
- **Ventana de Atención IA:** Los scripts modulares pequeños se pueden auditar y refactorizar sin errores de truncamiento.

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 🏗️ 7. Arquitectura de Software & Estándares de Código

Para cualquier MVP o desarrollo en `03_Taller_MVP/Proyectos/`, aplicaremos una **Arquitectura Modular Limpia (Modular Monolith)** adaptada a Python/FastAPI:

```
mi_proyecto_mvp/
├── src/
│   ├── core/           ← Configuración, constantes, logging, excepciones personalizadas
│   ├── domain/         ← Entidades biológicas, validaciones Pydantic, lógica de negocio pura
│   ├── services/       ← Algoritmos, parsers Biopython, procesamiento NGS, scipy
│   ├── api/            ← Endpoints FastAPI, routers por versión (/v1/alignments)
│   └── infrastructure/ ← Clientes externos (e-utilities NCBI), conexiones BD, wrapper CLI (samtools)
├── tests/              ← Pruebas unitarias e integración (pytest)
├── Dockerfile          ← Contenerización reproducible
├── requirements.txt    ← Dependencias fijadas
└── README.md           ← Documentación del proyecto en Inglés
```

### Reglas de Calidad de Código Python
- **PEP 8:** Estándar de formato (usar `ruff` o `black` como linter).
- **Type Hints:** Declaración explícita de tipos en todas las funciones (`def parse_fasta(filepath: Path) -> List[SeqRecord]:`).
- **Google Docstrings:** Documentación explícita de argumentos y retornos.
- **Manejo de Errores Riguroso:** No tragar excepciones silenciosamente (`try/except: pass` está prohibido).

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 🤖 8. Optimización RAG & LLMs (Indexación de Conocimiento)

Para garantizar que cualquier LLM o sistema de búsqueda vectorial (RAG) indexe este repositorio con precisión impecable:
1. **Encabezados Semánticos:** Cada sección debe usar H2 (`##`) o H3 (`###`) con títulos explícitos y descriptivos.
2. **Rutas Relativas Explícitas:** Todos los enlaces inter-documentos deben usar rutas relativas explícitas con prefijo `./` o `../` (ejemplo: `[`01_Estrategia/01_Auditoria...`](./01_Estrategia/01_Auditoria_y_Estrategia_Salarial_2026.md)`).
3. **Tablas de Contenido:** Todos los archivos de más de 100 líneas deben mantener su `📑 Tabla de Contenidos` al inicio.

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 🧪 9. Metodología TDD / Contract-First (Red-Green-Refactor)

> [!IMPORTANT]
> **Fin del Vibe Coding — Desarrollo Basado en Contratos:**
> Para abandonar definitivamente el código improvisado ("vibe coding") y adquirir un nivel senior, todo desarrollo de código sigue el ciclo **Red-Green-Refactor**:

1. **RED (Definir el Contrato):** Escribir primero la prueba en `tests/test_*.py`. Definir qué entradas recibe la función y qué salida exacta debe retornar. Ejecutar `pytest` y **confirmar que el test falla (RED)**.
2. **GREEN (Implementación Quirúrgica):** Christian escribe a mano en `src/` el código mínimo indispensable para hacer pasar la prueba en `pytest` **(GREEN)**.
3. **REFACTOR (Limpieza & Optimización):** Refactorizar el código para mejorar legibilidad, tipado (Type Hints) y rendimiento, asegurando que todos los tests sigan pasando.

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 🪜 10. Escalera de Verificación (Verification Ladder)

Ningún LLM debe declarar una tarea como "completa" sin evidencia. Aplica la prueba mínima confiable según el riesgo:

1. **Smoke Test (Riesgo Bajo):** Verificar que compila o importa correctamente tras un cambio menor (ej. `python -c "from src.main import app; print('OK')"`).
2. **Focused Test (Riesgo Medio):** Correr únicamente el test del módulo afectado (ej. `pytest tests/test_stats.py -k nombre_test`).
3. **Full Suite (Riesgo Alto):** Si se cambia la arquitectura o lógica compartida, ejecutar toda la suite: `pytest tests/ -x`. Fallos detienen la entrega.

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 🗺️ 11. Mapa de Fuentes de Verdad (Source of Truth)

Prohibida la duplicación de datos o crear "Objetos Dios". Cada tipo de dato vive estrictamente en su capa:

- **Archivos crudos masivos (FASTQ, BAM, VCF):** `data/raw/` (Solo lectura, jamás parsear completo en RAM).
- **Diccionarios Biológicos / Ontologías:** `data/reference/*.json` o `.csv` (El código de Python solo lo lee).
- **Lógica de validación / Entidades:** `src/domain/models.py`.
- **Proyección de Interfaz:** Todo cambio en el Source of Truth (Backend) debe verificarse en su consumidor final antes de cerrarse.

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 🔒 12. Privacidad y Ética de Datos Genómicos

En un entorno bioinformático profesional:
1. **Jamás uses secuencias reales de pacientes (PHI/HIPAA)** para pruebas locales o en APIs públicas de LLMs.
2. Utiliza siempre genomas sintéticos, datos de `data/reference/` o genomas públicos anonimizados (ej. 1000 Genomes Project).
3. El software bioinformático proporciona parámetros y p-valores; **la interpretación clínica final siempre recae en un profesional de la salud o biólogo molecular certificado.**

[⬆️ Volver al inicio](#-tabla-de-contenidos)
