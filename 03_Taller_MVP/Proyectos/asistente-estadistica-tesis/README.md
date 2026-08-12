# 📊 Asistente de Estadística y Termodinámica para Tesis

<div align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Biopython-000000?style=for-the-badge&logo=python&logoColor=white" alt="Biopython" />
</div>

> **El motor computacional diseñado para reducir de semanas a segundos el análisis de datos biológicos y el diseño de primers en investigaciones de tesis.**

---

## 🎯 El Problema
Los estudiantes de posgrado en biología molecular pierden hasta el 40% de su tiempo de investigación peleando con calculadoras web gratuitas que se cuelgan, copiando y pegando secuencias manualmente en Excel, y dudando sobre qué prueba estadística utilizar para validar sus resultados en el laboratorio.

## 🚀 La Solución
Una API RESTful robusta y contenerizada que expone algoritmos matemáticos y bioinformáticos de grado industrial (Scipy, Statsmodels, Biopython). Permite procesamiento por lotes masivo (batch processing) y automatización de toma de decisiones estadísticas.

### Capacidades Actuales (MVP)
- **Termodinámica de ADN (`/tm`)**: Cálculo instantáneo de la Temperatura de Fusión (Tm) usando la regla de Wallace para validación de primers cortos.
- **Inferencia Estadística (`/v1/stats`)**: Pipeline automatizado de validación de varianzas y aplicación del Test T de Student.

---

## 🏗️ Arquitectura del Sistema

La arquitectura sigue el patrón **Clean Architecture**, asegurando que la lógica de negocio (matemática y biológica) esté completamente aislada de la capa de red (HTTP), facilitando la migración futura a arquitecturas serverless o microservicios distribuidos.

```text
asistente-estadistica-tesis/
├── src/
│   ├── core/           ← Configuraciones globales y manejo de excepciones
│   ├── domain/         ← Modelos de datos y validación estricta (Pydantic)
│   ├── services/       ← Motores de cálculo puro (Biopython, SciPy)
│   ├── api/            ← Enrutadores y controladores REST
│   └── main.py         ← Punto de entrada asíncrono (FastAPI)
├── tests/              ← Suite de pruebas TDD (Red-Green-Refactor)
└── Dockerfile          ← Infraestructura inmutable para despliegue
```

---

## 💻 Despliegue Rápido (1-Click)

Levanta el ecosistema completo en tu máquina local usando Docker sin preocuparte por dependencias o versiones de Python:

```bash
# 1. Construir la imagen del contenedor
docker build -t bio-assistant:latest .

# 2. Desplegar el servicio en el puerto 8000
docker run -p 8000:8000 bio-assistant:latest
```
*La documentación interactiva de la API estará disponible automáticamente en `http://localhost:8000/docs` gracias al estándar OpenAPI.*

---

## 🧪 Pruebas y Cobertura (TDD)
Este proyecto fue construido usando Desarrollo Guiado por Pruebas (Test-Driven Development). Para auditar la integridad matemática:
```bash
PYTHONPATH=. pytest tests/ -v
```

---
*Desarrollado con rigor técnico para estudiantes que exigen precisión.*
