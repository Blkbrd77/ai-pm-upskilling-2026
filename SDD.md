# Software Design Description (SDD)
**Project Title:** AI/PM Upskilling Portfolio 2026

**Version:** 1.0
**Date:** December 31, 2025
**Author:** Jay Samples
**Status:** Draft

## 1. Introduction

### 1.1 Purpose
This Software Design Description outlines the structure, components, and implementation approach for a public GitHub repository serving as a machine learning upskilling portfolio. The repository documents daily progress, hosts classical ML experiments, and culminates in a deployed web application. It supports the developer's transition to AI Product Manager or AI Program Manager roles by demonstrating practical application of ML concepts to project management domains (e.g., earned value analysis, risk prediction).

### 1.2 Scope
The project encompasses:
- A GitHub repository with Markdown documentation for progress tracking.
- Jupyter notebooks (or Python scripts) for four classical ML mini-projects.
- A Flask-based web application integrating one ML model for prediction.
- Deployment of the web app to a free hosting platform.
- Supporting files (e.g., README, requirements.txt, datasets).

It excludes advanced topics like deep learning, LLMs, or production-scale MLOps.

### 1.3 Overview
The repository acts as a living portfolio, updated daily/weekly during Q1 2026. It combines documentation, code artifacts, and a deployable product to showcase consistency, technical growth, and domain relevance.

### 1.4 References
- Andrew Ng's Machine Learning Specialization (Coursera).
- Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow (Aurélien Géron).
- Previous personal projects (e.g., EVMS workbook generator, Flask sites).

## 2. System Overview

### 2.1 High-Level Architecture
The system is a static/dynamic hybrid hosted on GitHub:
- **Documentation Layer:** Markdown files in root and `/notes/` for progress tracking.
- **Code Layer:** Jupyter notebooks/Python modules in `/projects/` for ML experiments.
- **Application Layer:** Flask web app in root or `/app/` , using scikit-learn models.
- **Deployment:** GitHub Pages for static elements; Render.com or Vercel for the Flask app.

Data flow:
- Synthetic/real datasets (e.g., extended EVMS data) → ML notebooks → Trained models (pickled) → Flask app for inference → User interface for predictions.

### 2.2 Components
| Component              | Description                                                                 | Technologies                  |
|------------------------|-----------------------------------------------------------------------------|-------------------------------|
| Progress Tracker      | README with weekly table; daily/weekly Markdown notes                        | Markdown, GitHub              |
| ML Notebooks          | Four experimental notebooks for regression, classification, clustering, ensembles | Python, scikit-learn, Pandas, Matplotlib, Jupyter/Colab |
| Datasets              | Synthetic or anonymized project data (e.g., BAC, hours, risks)              | CSV/Excel files               |
| Flask Web App         | "Project Health Predictor" with input form, model inference, results display | Flask, scikit-learn, Plotly (optional), HTML/templates |
| Deployment Scripts    | Configuration for free hosting                                               | Render.yaml or Vercel config  |

### 2.3 Data Design
- Datasets stored in `/data/` (CSV format for portability).
- Models saved as `.pkl` files using joblib.
- No persistent database; all state is file-based or in-memory for simplicity.

## 3. Detailed Design

### 3.1 Repository Structure
```
ai-pm-upskilling-2026/
├── README.md                  # Overview, goals, progress table
├── notes/
│   ├── week-01-jan-2026.md    # Daily scrum-style entries
│   └── ...
├── projects/
│   ├── cost-overrun-regression/
│   │   ├── notebook.ipynb
│   │   └── data.csv
│   ├── risk-classification/
│   │   └── ...
│   ├── performance-clustering/
│   │   └── ...
│   └── ensemble-comparison/
│       └── ...
├── app/                       # Flask application (March phase)
│   ├── main.py
│   ├── models/model.pkl
│   ├── templates/index.html
│   ├── static/
│   └── requirements.txt
├── data/                      # Shared datasets
└── .gitignore
```

### 3.2 Phase-Specific Design

#### Phase 1: January (Foundations)
- No code artifacts beyond notes.
- Focus: Conceptual understanding; optional simple scripts for course exercises.

#### Phase 2: February (Hands-On ML)
- Four independent notebooks:
  1. Linear regression for cost overruns (features: planned BAC, time elapsed, hours logged).
  2. Logistic regression for task risk classification.
  3. K-means clustering for performance patterns.
  4. Random Forest ensemble with metric comparison.
- Each notebook includes: Data loading/preprocessing, model training, evaluation (e.g., MSE, accuracy, silhouettes), visualizations.

#### Phase 3: March (Integration & Deployment)
- Select best model (e.g., cost overrun predictor).
- Flask app design:
  - Routes: `/` (home with form), `/predict` (POST handling, model load, inference, results).
  - Input: Form fields matching model features.
  - Output: Prediction value, explanation (e.g., feature importance via sklearn).
  - Optional: Basic charts with Plotly.
- Deployment: Free tier (Render/Vercel); environment variables if needed.

### 3.3 Interfaces
- User Interface: Simple HTML forms/templates (Bootstrap for responsiveness).
- External: None (no APIs beyond optional dataset sources).

### 3.4 Non-Functional Considerations
- **Performance:** Lightweight; models <100MB, inference <1s.
- **Security:** No sensitive data; public repo.
- **Maintainability:** Clean code, comments, READMEs per project.
- **Portability:** Google Colab for development; export to .py if needed.

## 4. Implementation Plan (Q1 2026 Timeline)

| Month   | Focus                          | Key Deliverables                          |
|---------|--------------------------------|-------------------------------------------|
| January | ML Foundations                 | Completed Coursera modules; updated notes |
| February| Classical ML Experiments       | Four notebooks in `/projects/`            |
| March   | Productization & Showcase      | Deployed Flask app; video walkthrough; portfolio page updates |

Daily commitment: 30 minutes (20–25 min learning, 5–10 min hands-on/documentation).

## 5. Risks and Assumptions
- **Risks:** Time constraints may delay deployment; mitigated by phased scope.
- **Assumptions:** Free hosting remains available; datasets synthetic/anonymized.

---

*This SDD provides a clear blueprint for the AI/PM Upskilling Portfolio 2026 project.*
