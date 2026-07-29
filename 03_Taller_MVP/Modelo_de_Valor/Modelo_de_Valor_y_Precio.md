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
