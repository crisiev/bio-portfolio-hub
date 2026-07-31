# 🤝 CONTRIBUTING.md — Guía de Colaboración & Manifiesto de Comunidad

> [!IMPORTANT]
> **El Nodo Honeypot de Empleabilidad & Valor de Mercado**  
> `bio-portfolio-hub` / `empleoBio` no es solo un repositorio de código; es un **Gimnasio de Entrenabilidad de Mercado**. Aquí construimos evidencia técnica irrefutable para justificar sueldos justos en USD ($1,200–$1,800 local / $2,500–$4,500+ remoto) respaldados por estándares Enterprise (Linux RHEL, TDD, CI/CD, Docker).

---

## 📑 Tabla de Contenidos
- [1. Filosofía & El Manifiesto](#1-filosofía--el-manifiesto)
- [2. Estructura de Niveles de Contribución](#2-estructura-de-niveles-de-contribución)
- [3. Estándares Técnicos Obligatorios](#3-estándares-técnicos-obligatorios)
- [4. Proceso de Pull Request (Paso a Paso)](#4-proceso-de-pull-request-paso-a-paso)
- [5. Código de Conducta & Respeto Técnico](#5-código-de-conducta--respeto-técnico)

---

## 🏛️ 1. Filosofía & El Manifiesto

Rechazamos el "vibe coding" improvisado y la precarización del talento técnico y bioinformático. Todo cambio integrado en esta plataforma responde a **necesidades reales de mercado y valor justificado**.

- **Calidad Enterprise:** Si el código no tiene pruebas unitarias (`pytest`) o viola el formato estándar PEP 8 / `ruff`, la integración continua (CI) bloqueará el merge automáticamente.
- **Trazabilidad:** Cada commit es un ladrillo en tu portafolio público.

---

## 👥 2. Estructura de Niveles de Contribución

Organizamos la comunidad en **3 niveles de liderazgo y colaboración**:

```
        [ Nivel 3: Core Maintainers ]      ◄── Revisan PRs, arquitectura y despliegues
     [ Nivel 2: Feature Developers ]      ◄── Resuelven Tickets / Issues (`good first issue`)
  [ Nivel 1: QA & Testers de Comunidad ]  ◄── Prueban la app en producción y reportan bugs
```

1. **Nivel 1 (QA / Testers):** Prueban nuestras aplicaciones desplegadas en vivo (ej. Render) y abren **GitHub Issues** reportando fallos o mejoras de UX.
2. **Nivel 2 (Developers):** Toman un Issue asignado, crean una rama `feature/nombre-tarea` y envían su Pull Request.
3. **Nivel 3 (Maintainers):** Auditan los PRs, evalúan el paso del CI y fusionan (`Merge`) hacia `main`.

---

## 🛠️ 3. Estándares Técnicos Obligatorios

Antes de enviar un Pull Request, asegúrate de cumplir estas reglas:

1. **Python 3.10+ & Type Hints:** Tipado explícito nativo (`list[float]`, `dict[str, Any]`).
2. **Arquitectura Modular:** Separación estricta entre `src/api/`, `src/services/` y `src/domain/`.
3. **Commits en Inglés:** Siguiendo `Conventional Commits` (ej: `feat(api): add new validation schema`).
4. **Verificación Local Obligatoria:**
   ```bash
   python -m pytest tests/ -v
   python -m ruff check src tests
   python -m ruff format --check src tests
   ```

---

## 🔄 4. Proceso de Pull Request (Paso a Paso)

### Para Colaboradores del Equipo (Miembros con acceso):
1. Crea tu rama: `git checkout -b feature/mi-funcionalidad`
2. Realiza tus cambios y haz commits quirúrgicos (`git add <archivo>`).
3. Sube la rama: `git push origin feature/mi-funcionalidad`
4. Abre el **Pull Request** en GitHub y vincula el Issue (`Closes #ID`).

### Para Contribuidores Externos (Comunidad Open Source):
1. Haz **Fork** de este repositorio hacia tu cuenta personal.
2. Clona tu Fork, crea tu rama y haz los cambios.
3. Envía un **Pull Request** desde tu Fork hacia `crisiev/bio-portfolio-hub:main`.
4. El CI de GitHub Actions ejecutará las pruebas aisladas de seguridad y calidad.

---

## ⚖️ 5. Código de Conducta & Respeto Técnico

- **Cultura de Evidencia:** Las discusiones de arquitectura se resuelven con benchmarks y datos, no con opiniones personales.
- **Code Reviews Constructivos:** Criticamos el código o el bug, nunca a la persona.
- **Decisión Final:** El maintainer del proyecto se reserva el derecho de rechazar sugerencias que desvíen la visión estratégica del producto.

---
*Manifiesto impulsado por [Christian Alcivar](https://github.com/crisiev)*
