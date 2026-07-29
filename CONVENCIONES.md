# CONVENCIONES.md — cómo se organiza y crece esta codebase

Reglas simples para que la carpeta sea navegable por ti y por cualquier LLM, y crezca sin volverse un desorden.

## Nomenclatura

- **Documentos de estrategia:** prefijo numérico de dos dígitos + snake_case: `03_Perfil_Ideal_y_CV.docx`.
- **Carpetas:** `PascalCase` o `Snake_Case` con inicial mayúscula: `Taller_MVP/`, `Mercado_Universitario/`.
- **Notas y logs:** `AAAA-MM.md` (bitácora mensual), `AAAA-MM-DD_tema.md` para notas puntuales.
- **Plantillas:** prefijo `_PLANTILLA_` para que floten arriba y no se confundan con contenido real.
- **Tickets:** `PREFIJO-###` (ej. `MVP-001`, `R1-XUB-001`). El prefijo indica el sistema.

## Estructura (dónde va cada cosa)

| Tipo de contenido | Ubicación |
|-------------------|-----------|
| Gobernanza (cómo trabajar) | Raíz: `README`, `AGENTS`, `CONVENCIONES` |
| Estrategia (leer, no editar a diario) | Raíz: `NN_*.docx` |
| Registro fechado de práctica | `Bitacora/` |
| Notas de estudio por dominio | `Aprendizaje/<Dominio>/` |
| Producto: planeación y negocio | `Taller_MVP/` (md y xlsx) |
| Producto: código real | `Taller_MVP/Proyectos/<proyecto>/` (y repo aparte en GitHub) |

## Reglas de crecimiento

1. **Un tema, un archivo.** No mezcles estudio de Linux con notas de un MVP. Si dudas dónde va, mira la tabla de arriba.
2. **Markdown para lo que editas tú a diario** (notas, logs, tableros): es ligero, va en Git y lo lees en cualquer lado. Los `.docx`/`.xlsx` son entregables "de presentación".
3. **Cada carpeta nueva lleva un `README.md`** de una línea que diga qué contiene. Así el mapa nunca se pierde.
4. **Actualiza `README.md` raíz** cuando agregues una carpeta o documento importante (una línea en el árbol).
5. **Git manda.** Todo cambio serio = un commit con mensaje real. La fecha del commit es tu respaldo de experiencia.

## Convención de commits (Conventional Commits + OS Tag en Inglés)

`type(scope-os): short description in English` — ejemplos:
- `feat(infra-rocky): configure dnf package manager and systemd services`
- `infra(wsl): setup SSH ed25519 authentication for GitHub integration`
- `feat(mvp-xubuntu): implement /tm endpoint using Biopython parser`
- `docs(governance): update project roadmap and English commit rules`

## Idioma & Estrategia de Demostración (Show, Don't Tell)

1. **Inglés Técnico Profesional (100% en GitHub):**
   - **Commits, PRs, Issues, Comentarios de código, Readmes de proyectos y ADRs (Architecture Decision Records):** **100% en Inglés.**
   - Esto actúa como prueba viva e irrefutable de tu fluidez en inglés (C1/B2) ante reclutadores internacionales de EE.UU. y Europa.
2. **Notas internas de estudio y bitácora personal:** Pueden ser en Español o Spanglish técnico en tus archivos locales de estudio.
