# 🛡️ TruthGuard — Explainable AI System for News Verification

TruthGuard is a **full end‑to‑end AI system** designed to assist journalists and editors in assessing whether a piece of news text is **likely REAL or FAKE**, while preserving **human decision‑making, transparency, and accountability**.

The system is built using a **modern microservice architecture**, integrates **Explainable AI (XAI)**, and follows **DevOps and Responsible AI principles**.

> ⚠️ TruthGuard is a **decision‑support tool**, not an automated truth or censorship system.

---

## 🎯 Problem Statement

The rapid spread of misinformation places immense pressure on newsrooms to verify content quickly without compromising accuracy. Manual fact‑checking does not scale, while opaque AI systems erode trust.

**TruthGuard addresses this by providing:**
- Fast AI‑based classification
- Confidence estimation
- Transparent, model‑level explanations
- Human‑in‑the‑loop decision support

---

## 🧱 System Architecture

TruthGuard follows a **layered, microservice‑based architecture**:

---

## 🧠 Core Components

### Frontend
- **React + Vite**
- Collects news text and displays results
- Pure presentation layer (no business logic)
- Clean, responsive UI with custom CSS

### Backend
- **Node.js + Express**
- Orchestrates the system
- Handles validation, routing, and persistence
- Communicates with ML service via REST APIs

### Machine Learning Service
- **Python + FastAPI**
- Logistic Regression model with TF‑IDF features
- Lightweight, interpretable, and efficient
- SHAP used for explainability

### Database
- **MongoDB**
- Stores prediction logs and metadata
- Enables traceability, auditing, and future drift analysis

---

## 🔍 Explainable AI (XAI)

TruthGuard prioritizes transparency using **SHAP (SHapley Additive Explanations)**:

- Identifies which words contributed to a prediction
- Explains *why* content was classified as REAL or FAKE
- Supports ethical, trustworthy AI use in journalism

This design choice favors **interpretability over black‑box accuracy**, aligning with Responsible AI standards.

---

## 🔧 DevOps & Infrastructure

TruthGuard applies **core DevOps practices**:

- **Docker** for containerization of all services
- **Docker Compose** for orchestration and networking
- **Infrastructure as Code** for reproducibility
- Environment‑based configuration management
- Health‑check endpoints for observability

Entire system can be started with a single command.

---

## 🔁 CI/CD Pipeline

- **GitHub Actions** used for Continuous Integration
- Automatically triggered on every `main` branch push
- Pipeline performs:
  - Dependency installation
  - Frontend build
  - Backend checks
  - ML testing
- Clean dependency hygiene (`node_modules` excluded)

✅ CI/CD pipeline is **green and stable**

---

## ▶️ How to Run the Project (From Zero)

### 1️⃣ Navigate to project root
```bash
cd newsguard-ai
```
### 2️⃣ Clean any previous containers
docker compose down --remove-orphans --volumes
``

### 3️⃣ Build all services
Shelldocker compose build --no-cacheShow more lines
``
### 4️⃣ Start the full system
Shelldocker compose upShow more lines
``
## 🌐 Service Endpoints
ServiceURLFrontendhttp://localhost:5173Backend healthhttp://localhost:5000/healthML service healthhttp://localhost:8000/healthML API docshttp://localhost:8000/docs
``
## ✅ Responsible AI Principles
TruthGuard follows Responsible AI best practices:

Human‑in‑the‑loop: AI supports, humans decide
Transparency: Confidence scores and explanations
Accountability: Logged predictions
Safety: Input validation and error handling
Ethics: No automated enforcement or censorship


## 🏛️ Regulatory Consideration
Conceptually aligns with EU AI Act – Limited Risk AI:

Advisory role only
Explicit uncertainty communication
Explainability by design


## 🧪 Testing & Quality Assurance

Backend API tests (Node.js)
ML tests using Pytest:

API correctness
Robustness checks
Metamorphic testing
Model quality validation

### 📦 Technologies Used
Frontend: React, Vite, HTML, CSS
Backend: Node.js, Express, Axios
ML: Python, FastAPI, Scikit‑learn, SHAP
Database: MongoDB
DevOps: Docker, Docker Compose, GitHub Actions
Version Control: Git, GitHub

## 📌 Project Context
This project was developed as an AI Systems Engineering / MSc‑level academic project, demonstrating:

End‑to‑end AI system design
Explainable Machine Learning deployment
Microservice architecture
DevOps and CI/CD practices
Responsible AI awareness
