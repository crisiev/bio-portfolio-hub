# 🛠️ Taller MVP — Construir Software Vendible Mientras Practico

> [!IMPORTANT]
> **Carril paralelo al empleo:** Aquí construyes software real, con sentido comercial, para **practicar el stack objetivo** (FastAPI, Docker, Cloud, LLMs, APIs) y tener una **segunda carta de presentación imbatible** ante reclutadores.

---

## 📑 Tabla de Contenidos
- [1. Reglas del Taller](#1-reglas-del-taller)
- [2. Estrategia Evolutiva de Arquitectura (Monolito a Microservicios)](#2-estrategia-evolutiva-de-arquitectura-monolito-a-microservicios)
- [3. Estructura y Flujo de Trabajo](#3-estructura-y-flujo-de-trabajo)

---

## ⚙️ 1. Reglas del Taller

1. **Un usuario que pague al mes = éxito de validación.** No buscas hacerte rico aún; buscas probar que alguien paga por algo que construiste. Esa frase en una entrevista vale oro.
2. **Barrera de pago mínima.** Precio "ganga" hasta validar ($1.99 – $4.99). Freemium o pago-por-uso. El objetivo temprano es el *primer dólar*, no el ingreso grande.
3. **Calidad siempre.** Aunque sea práctica, nada cutre: es portafolio. README serio, código limpio, contenedores, deploy real.
4. **Trabajo por Sprints.** Ciclos cortos (1–2 semanas) con un objetivo y un entregable demostrable. Ver [`TABLERO.md`](./TABLERO.md).
5. **Todo commiteado.** Cada avance = commit fechado (respalda tu bitácora y tu experiencia).

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 🏗️ 2. Estrategia Evolutiva de Arquitectura (Monolito a Microservicios)

> [!NOTE]
> **Aprender ambos mundos sin sobrecomplicar el Día 1:**  
> Arrancamos con un **Monolito Modular (Clean Architecture)** para validar el producto sin fricción de red. Conforme el software madura, ejecutamos la **Extracción a Microservicios** de forma estratégica.

### Mapa de Fases de Arquitectura

```
Fase 1: Monolito Modular (Día 1 - Sprint 0 a 1)
├── src/core/           ← Configuración
├── src/domain/         ← Esquemas Pydantic / Entidades
├── src/services/       ← Motores de cálculo (Stats / Bio)
└── src/api/            ← FastAPI routers
    ↓
Fase 2: Extracción a Microservicio (Sprint 2 / Rango III)
├── microservicio-api/            ← Servidor Principal (Puerto 8000)
└── microservicio-stats-engine/   ← Contenedor Docker dedicado (Puerto 8001)
```

### Guardarrayas & Gatillos de Extracción (Triggers)
Cualquier LLM que te asista DEBE alertarte y proponerte la extracción a microservicio cuando ocurra uno de estos gatillos:
- **Gatillo 1 (Cómputo):** El cálculo bioestadístico o algorítmico supera los 500ms o requiere más de 512MB RAM.
- **Gatillo 2 (Reutilización):** Quieres usar el mismo motor de cómputo en otro proyecto distinto.
- **Gatillo 3 (Demostración CV):** Quieres practicar comunicación inter-servicio (REST/gRPC/Docker Compose) para entrevistas senior.

[⬆️ Volver al inicio](#-tabla-de-contenidos)

---

## 🗂️ 3. Estructura y Flujo de Trabajo

```
03_Taller_MVP/
├── README.md                 ← este archivo
├── IDEAS.md                  ← backlog de ideas rankeadas
├── TABLERO.md                ← kanban + objetivo del sprint actual
├── Roadmap_Monetizacion.md   ← estrategia de precios y tracción
├── _PLANTILLA_ticket.md      ← plantilla para cada tarea
├── Mercado_Universitario/    ← ideas mapeadas a facultades/materias
├── Modelo_de_Valor/          ← tracker de precios (.md)
└── Proyectos/                ← repos de código real (asistente-estadistica-tesis, etc.)
```

> [!TIP]
> **Flujo Continuo:**  
> **Elegir idea ([`IDEAS.md`](./IDEAS.md)) → definir Sprint 0 ([`TABLERO.md`](./TABLERO.md)) → crear tickets → construir → deploy → conseguir el primer usuario → iterar.**

[⬆️ Volver al inicio](#-tabla-de-contenidos)
