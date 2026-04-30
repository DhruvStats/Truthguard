# TruthGuard — Architecture Notes

This document describes the system architecture of TruthGuard, including
requirements, major design decisions, quality attributes, and known limitations.
It is written following AI Systems Engineering and Model-Based Systems Engineering principles.

---

## 1. System Requirements

### 1.1 Functional Requirements

- The system shall accept textual news input from a user.
- The system shall classify the input as REAL or FAKE.
- The system shall provide a confidence score for each prediction.
- The system shall generate a human-readable explanation.
- The system shall store prediction results for monitoring purposes.
- The system shall expose health endpoints for monitoring and orchestration.

### 1.2 Non‑Functional Requirements

- Response time should be under 2 seconds for typical inputs.
- The system shall support horizontal scalability.
- The system shall be deployable using container technology.
- The system shall be testable and observable.
- The system shall support human oversight and explainability.

---

## 2. Architecture Decision Records (ADR)

### ADR‑1: Microservices vs Monolith
- **Decision:** Microservices
- **Alternatives:** Monolithic application
- **Rationale:** Allows independent scaling of ML inference, easier deployment,
  and clearer separation of concerns.

### ADR‑2: FastAPI for ML Service
- **Decision:** FastAPI
- **Alternatives:** Flask
- **Rationale:** Built‑in request validation, OpenAPI generation, and async support.

### ADR‑3: Logistic Regression vs Deep Learning
- **Decision:** Logistic Regression
- **Alternatives:** Transformer‑based classifiers
- **Rationale:** Interpretability, faster inference, stability under distribution shift,
  and suitability for demonstrative AI system engineering.

### ADR‑4: MongoDB vs Relational Database
- **Decision:** MongoDB
- **Rationale:** Flexible schema for logging predictions, suitable for experimentation
  and monitoring workflows.

### ADR‑5: Docker + Kubernetes vs Virtual Machines
- **Decision:** Docker and Kubernetes
- **Rationale:** Reproducibility, scalability, modern deployment practices.

---

## 3. Quality Attributes (FASTEP Perspective)

| Attribute | Design Choice |
|---------|---------------|
| Fairness | Confidence display and human‑in‑the‑loop usage |
| Accuracy | Offline training with evaluation |
| Security | Input validation and restricted service exposure |
| Transparency | Confidence + explanation output |
| Ethics | Decision support, not automation |
| Privacy | No personal data stored |
| Safety | Rejection of empty or malformed input |

---

## 4. Known Limitations and Technical Debt

1. The model is trained on a limited dataset.
2. No automated retraining pipeline is implemented.
3. Canary image may not be built during demos.
4. Bias audits are not yet automated.
5. LLM explanation is deterministic (stub for future expansion).