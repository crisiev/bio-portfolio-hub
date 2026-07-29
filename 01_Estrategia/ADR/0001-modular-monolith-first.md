# ADR-0001: Adopción de Monolito Modular con Clean Architecture como Baseline Inicial

* **Estado:** Aprobado
* **Fecha:** 2026-07-29
* **Autor:** Christian Alcivar (`cjalcivar@gmail.com`)

---

## Contexto y Problema
Al iniciar el desarrollo de productos y proyectos de portafolio en `03_Taller_MVP/`, se requería seleccionar un patrón de arquitectura de software que permitiera validar rápidamente hipótesis de negocio sin introducir complejidad accidental ni sobrecostos de infraestructura distribuida en etapas tempranas.

## Opción Elegida y Razón
Se seleccionó la estrategia **Monolith First** utilizando una arquitectura limpia modular (**Modular Monolith**):
- Separación estricta de capas (`src/core/`, `src/domain/`, `src/services/`, `src/api/`).
- Desacoplamiento total entre el motor de cómputo y la capa de presentación (FastAPI).

### Razón Técnica:
1. Permite ejecutar el ciclo completo de TDD (`pytest`) en un solo proceso sin latencia de red.
2. Mantiene una alta cohesión interna y bajo acoplamiento, dejando cada módulo (`src/services/`) preparado para ser extraído a su propio microservicio en Docker en el momento en que escale el cómputo o el dominio.

## Consecuencias

### Positivas
- Velocidad máxima de desarrollo inicial y despliegue simple.
- Cero sobrecosto de orquestación de red temprana.
- Estructura 100% preparada para migración evolutiva a Microservicios.

### Negativas / Trade-offs
- Se debe ser disciplinado para no violar las fronteras entre módulos dentro del mismo monolito (mitigado por las reglas de `CONVENCIONES.md`).
