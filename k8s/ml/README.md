# Canary Deployment for TruthGuard ML Service

A canary deployment is used to safely deploy new versions of the ML model.

## How it works in this project:

- The stable model runs with 3 replicas (`track: stable`)
- The canary model runs with 1 replica (`track: canary`)
- A single Kubernetes Service load-balances traffic across all pods
- Approximately 25% of traffic is routed to the canary model
- Model behavior is monitored before promoting the canary to stable

## Why canary deployments are important for ML systems:

- ML updates can silently degrade accuracy
- Canary deployment reduces the blast radius of faulty models
- Performance, confidence, and drift can be observed safely
- Supports responsible and controlled model evolution
- Aligns with industry best practices for MLOps