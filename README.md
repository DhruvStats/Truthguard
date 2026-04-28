# 🛡️ TruthGuard — AI‑Powered Fake News Detection System

TruthGuard is a **production‑ready AI system** that identifies whether a given news article or headline is **REAL ✅ or FAKE ❌** in real time.  
The project is designed using **AI System Engineering principles** and integrates **Machine Learning, Full‑Stack Development, DevOps, MLOps, and Kubernetes‑ready architecture**.

---

## 🎯 Why This Project Was Built

The rapid spread of misinformation affects journalism, public trust, and decision‑making. Most users lack fast, reliable tools to verify news credibility before sharing or publishing.

**TruthGuard was created to:**
- Reduce the spread of fake news
- Provide instant credibility verification
- Demonstrate a real‑world AI system end‑to‑end
- Apply DevOps and MLOps best practices practically

---

## 👥 Who This Project Helps

- 📰 **Journalists & Media Houses** — quick verification before publishing  
- 🎓 **Students & Learners** — understanding AI System Engineering  
- 🧑‍🤝‍🧑 **General Users** — verify news before sharing  
- 🏢 **Organizations** — prototype misinformation‑filtering systems  

---

## 🧠 System Architecture

TruthGuard follows a **modular microservices architecture** with independent, scalable components communicating via REST APIs.

---

## 🧩 Core Components

### Frontend (Presentation Layer)
- React + Vite
- Clean, modern, user‑friendly UI
- Accepts news text and displays final result only (REAL / FAKE)

### Backend (Application Layer)
- Node.js + Express
- Orchestrates the system
- Connects frontend and ML service
- Handles validation, error handling, and logging

### Machine Learning (Intelligence Layer)
- Python + Scikit‑learn
- TF‑IDF + Logistic Regression
- FastAPI inference service

### Database (Persistence & MLOps Layer)
- MongoDB
- Stores prediction history for monitoring and retraining

---

## 🔁 DevOps & MLOps Overview

### ✅ DevOps
- Docker containerization for all services
- Docker Compose for orchestration
- CI/CD pipeline using GitHub Actions
- Environment‑aware configuration (local & containerized)

### ✅ MLOps
- Separate training and inference pipelines
- Model persistence and versioning
- Prediction logging for monitoring
- Health endpoints and retraining hooks

> Kubernetes manifests are included as an **optional, future‑ready deployment layer**.

---

TruthGuard is a complete AI system that demonstrates how machine learning, DevOps, and MLOps work together to combat misinformation using a real‑world, production‑style architecture.
