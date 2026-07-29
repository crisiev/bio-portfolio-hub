# 🏛️ ADR (Architecture Decision Records) — Registro de Decisiones de Arquitectura

> [!IMPORTANT]
> **Estándar de Ingeniería Senior (Nygard Format):**  
> Los **ADRs** son documentos breves e inmutables que registran *por qué* tomamos una decisión técnica específica (ej. por qué usar Monolito Modular antes de Microservicios, por qué usar DuckDB o FastAPI).  
> **Para qué sirven:** Muestran a los evaluadores de empleo que tomas decisiones basadas en trade-offs ingenieriles y no en modas.

---

## 📑 Registro de Decisiones

| ID | Fecha | Título | Estado |
|----|-------|--------|--------|
| [ADR-0001](./0001-modular-monolith-first.md) | 2026-07-29 | Adopción de Monolito Modular con Clean Architecture como baseline inicial | Aprobado |

---

## 📐 Plantilla de un ADR (`_PLANTILLA_adr.md`)

```markdown
# ADR-0000: [Título corto de la decisión]

* **Estado:** [Propuesto / Aprobado / Reemplazado]
* **Fecha:** AAAA-MM-DD
* **Autor:** Christian Alcivar (`cjalcivar@gmail.com`)

## Contexto y Problema
[Describe el problema técnico o de negocio que necesitabas resolver]

## Opción Elegida y Razón
[Explica la opción seleccionada y la justificación técnica]

## Consecuencias
* **Positivas:** [Beneficios ganados]
* **Negativas / Trade-offs:** [Complejidad o desventajas asumidas]
```
