# 📊 Thesis Stat Assistant — Technical Practice Scaffold

> A technical FastAPI scaffold for learning modular service design. It is **not** the selected commercial MVP and is not ready for real academic or clinical decisions.

## 🎯 Overview
Thesis Stat Assistant currently exposes one educational two-sample Student's t-test endpoint. It exists to practice contracts, validation, testing, Docker, and CI before product work begins. It does not yet select tests, validate statistical assumptions, or replace advice from a qualified statistician.

---

## 🏗️ Architecture

```
asistente-estadistica-tesis/
├── src/
│   ├── core/           ← App configuration, logging & custom exceptions
│   ├── domain/         ← Pydantic validation schemas & statistical data models
│   ├── services/       ← Biostatistical computation engine (SciPy & Statsmodels)
│   ├── api/            ← FastAPI REST routers (/v1/stats)
│   └── main.py         ← FastAPI application entry point
├── tests/              ← Automated unit & integration tests (pytest)
├── Dockerfile          ← Production container configuration
├── requirements.txt    ← Pinned Python dependencies
└── README.md           ← Project documentation
```

---

## 🚀 Getting Started

### 1. Local Setup
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run API Server
```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Run Automated Tests
```bash
pytest tests/ -v
```

### 4. Docker Containerization
```bash
docker build -t thesis-stat-assistant:latest .
docker run -p 8000:8000 thesis-stat-assistant:latest
```

---

## 📄 License
MIT License — see [`LICENSE`](./LICENSE).
