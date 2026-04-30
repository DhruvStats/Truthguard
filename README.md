<<<<<<< HEAD
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
=======
TruthGuard — An AI Systems Engineering Project
Course: AI Systems Engineering
University: Università di Napoli Federico II
Project Type: End‑to‑End AI System (Not a standalone ML model)

1. Project Overview
TruthGuard is a fake news detection system designed to assist journalists and content reviewers by classifying news text as REAL or FAKE, while also providing a confidence score and a human‑readable explanation.
The key goal of TruthGuard is not only to achieve reasonable classification accuracy, but to demonstrate how an AI model can be engineered, deployed, monitored, tested, and evolved as part of a complete AI system.
The project emphasizes system architecture, MLOps, DevOps, Kubernetes orchestration, and responsible AI considerations, in alignment with the course objectives.
TruthGuard is explicitly designed as a decision‑support tool, not an automated decision maker.

2. AI Systems Engineering vs Data Science
Data Science typically focuses on:

Exploring data in notebooks
Training models
Optimizing accuracy or F1 score
Producing experimental results

AI Systems Engineering, in contrast, focuses on:

Designing systems that integrate AI models into real applications
Managing the full life‑cycle: training → deployment → monitoring → retraining
Ensuring reliability, scalability, testability, and maintainability
Addressing operational, ethical, and governance concerns

TruthGuard follows the AI Systems Engineering approach.
The machine‑learning model is only one component in a larger system that includes:

A frontend interface
A backend orchestration layer
A containerized ML inference service
Automated testing
Monitoring and drift detection
Kubernetes‑based deployment strategies
Responsible AI documentation

This distinction is a deliberate design choice aligned with course goals.

3. System Architecture
TruthGuard is implemented as a microservice‑based system, with clear separation of responsibilities.
High‑level architecture:
User (Browser)
      |
      v
Frontend (React + Vite)
      |
      v
Backend (Node.js / Express)
      |
      v
ML Inference Service (FastAPI, Kubernetes)
      |
      v
MongoDB (Prediction Logging & Monitoring)

Key design principles:

Separation of concerns: UI, orchestration, inference, and persistence are decoupled
Scalability: ML and backend services can scale independently
Replaceability: The ML model or explanation layer can be replaced without changing the frontend
Observability: Predictions and confidence scores are logged for monitoring and drift analysis


4. Technology Stack

ComponentTechnologyPurposeFrontendReact + ViteUser interaction and result visualizationBackendNode.js + ExpressRequest validation, orchestration, API gatewayML ServicePython + FastAPIModel inference and explanationML ModelTF‑IDF + Logistic RegressionFake news classificationDatabaseMongoDBPrediction logging & monitoringContainersDockerEnvironment reproducibilityOrchestrationDocker Compose, KubernetesDeployment and scalingCI/CDGitHub ActionsAutomated build and testingMonitoringCustom DriftMonitorDetect model confidence drift

5. ML Model
The ML component uses:

TF‑IDF vectorization for text feature extraction
Logistic Regression for binary classification (REAL / FAKE)

Motivation for this choice:

Interpretable coefficients
Stable behavior under small data shifts
Fast inference suitable for real‑time systems
Easier debugging and monitoring than opaque deep models

The model outputs:

A prediction label (REAL or FAKE)
A confidence score derived from class probabilities

Deep learning models were considered but not selected to maintain interpretability and reduce system complexity for this context.

6. MLOps Life‑Cycle
TruthGuard implements a complete MLOps loop:

Train

Model trained offline using labeled news data


Deploy

Model packaged into a FastAPI service
Deployed using Docker and Kubernetes


Monitor

Confidence scores logged
DriftMonitor computes statistics (mean confidence, low‑confidence rate)


Detect Drift

Drift flagged when confidence degrades beyond thresholds


Retrain (Manual Decision)

Retraining is recommended, not automatic, preserving human oversight



This controlled life‑cycle avoids unsafe fully automated retraining.

7. How to Run (Docker Compose)
Prerequisites

Docker
Docker Compose

Steps
Shellgit clone <repository-url>cd newsguard-aidocker compose builddocker compose upShow more lines

Frontend: http://localhost:5173
Backend API: http://localhost:5000
ML Service: http://localhost:8000


8. How to Run Tests
The ML service includes automated tests for:

API correctness
Robustness
Metamorphic properties

Run tests with:
Shellpython -m pytest ml/tests -vShow more lines
Tests are also executed automatically in the CI/CD pipeline.

9. EU AI Act Compliance (Overview)
TruthGuard is a high‑impact decision‑support system because it assists journalists in evaluating news credibility.
Key compliance principles addressed:

Human oversight: The system provides recommendations, not automated decisions
Transparency: Confidence scores and explanations are shown to users
Robustness: Input validation and testing prevent unsafe behavior
Traceability: Predictions are logged for auditing

A detailed Responsible AI and ALTAI assessment is provided in docs/responsible-ai.md.

10. Future Work

Integrate a real LLM or RAG‑based explanation module
Add SHAP‑based feature attribution for model interpretability
Perform systematic bias and fairness evaluations
Deploy to a managed cloud Kubernetes platform (EKS/GKE)


Final Note
This project intentionally prioritizes engineering correctness, system lifecycle management, and responsible AI practices over model complexity.
TruthGuard demonstrates how AI models should be embedded into real systems, monitored over time, and governed responsibly — which is the core objective of AI Systems Engineering.
>>>>>>> 7f64435 (Fix frontend mounting, Docker setup, and stabilize full system startup)
