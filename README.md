# ⛰️ TERROVA

### Terrain Risk Observation & Early Warning Platform

**AI-Powered Landslide Risk Monitoring and Early Warning System**

[![SIH 2026](https://img.shields.io/badge/SIH%202026-SIH26001-blue)](https://www.sih.gov.in/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest-green)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Prototype-orange)]()

## 🚀 Live Demo

**[Launch TERROVA](https://terrova-risk.streamlit.app/)**

---

## 📌 Overview

**TERROVA** is an AI-powered disaster-management platform designed to identify and monitor areas vulnerable to landslides.

The platform analyses environmental and terrain-related factors such as:

* 🌧️ Rainfall
* 💧 Soil moisture
* ⛰️ Terrain slope
* 🏔️ Elevation
* 📚 Historical landslide activity

Using a **Random Forest machine-learning model**, TERROVA generates a landslide risk score and classifies locations into different risk levels.

The platform combines risk prediction, GIS-based visualization, emergency prioritisation and field reporting into a single interface.

---

## 🎯 Problem Statement

### SIH26001 — AI-Based Early Warning and Landslide Risk Monitoring System in NER

The North Eastern Region of India is highly vulnerable to landslides due to heavy rainfall, steep terrain, fragile geological conditions and human activity.

Traditional monitoring is often reactive, making it difficult for authorities to identify vulnerable locations and prioritize preventive action.

TERROVA aims to provide an intelligent decision-support platform that can help identify high-risk areas and support faster disaster response.

---

## 💡 Our Solution

TERROVA follows a simple pipeline:

```text
Environmental & Terrain Data
            ↓
      Data Processing
            ↓
      Machine Learning
            ↓
      Landslide Risk Score
            ↓
    Risk Classification
            ↓
 ┌──────────┼──────────┐
 ↓          ↓          ↓
GIS Map   Alerts   Response Priority
            ↓
      Field Reporting
            ↓
     Disaster Response
```

---

## ✨ Key Features

### 🤖 AI-Based Risk Prediction

The system uses a **Random Forest Classifier** to estimate landslide probability from environmental and terrain features.

### 📊 Risk Score

Each prediction produces a percentage-based risk score.

| Risk Score | Risk Level   |
| ---------: | ------------ |
|      0–39% | 🟢 Low       |
|     40–59% | 🟡 Moderate  |
|     60–79% | 🟠 High      |
|    80–100% | 🔴 Very High |

### 🗺️ GIS Risk Visualization

The platform provides an interactive map showing risk levels across selected locations in the North Eastern Region.

Users can visually identify high-risk locations and prioritize monitoring.

### 🚨 Early Warning

The platform generates warning levels based on predicted risk:

```text
LOW       → Normal Monitoring
MODERATE  → Monitor Closely
HIGH      → Increase Monitoring
VERY HIGH → Immediate Response
```

### 🚑 Emergency Response Prioritisation

High-risk locations are ranked according to severity and associated recommended actions.

This helps authorities decide where response resources should be deployed first.

### 📍 Field Reporting

Citizens and field officers can submit:

* Landslide reports
* Road blockages
* Slope cracks
* Slope movement
* Flooding reports
* Photographic evidence

### 🧠 Explainable Risk Factors

TERROVA doesn't only display a prediction.

It also identifies environmental conditions contributing to the risk, such as:

```text
🌧️ Heavy rainfall
💧 High soil moisture
⛰️ Steep terrain
📚 Previous landslide activity
🏔️ High elevation
```

---

## 🛠️ Technology Stack

| Component            | Technology                  |
| -------------------- | --------------------------- |
| Frontend             | Streamlit                   |
| Programming Language | Python                      |
| Machine Learning     | Scikit-learn                |
| ML Algorithm         | Random Forest               |
| Data Processing      | Pandas, NumPy               |
| Visualization        | Plotly                      |
| GIS Visualization    | Plotly Maps / OpenStreetMap |
| Deployment           | Streamlit Community Cloud   |
| Version Control      | GitHub                      |

---

## 🧠 Machine Learning Pipeline

The current prototype uses the following input features:

```text
Rainfall
Soil Moisture
Slope
Elevation
Historical Landslide Events
```

### Prediction Process

```text
Input Environmental Conditions
            ↓
      Feature Preparation
            ↓
      Random Forest Model
            ↓
       Probability Score
            ↓
      Risk Classification
            ↓
     Warning / Recommendation
```

The model is trained using a demonstration dataset and produces a probability-based risk assessment.

---

## 🖥️ Application Modules

### 1. Risk Assessment Dashboard

Displays:

* Current risk score
* Risk level
* Rainfall
* Soil moisture
* Selected location
* Recommended action

### 2. Environmental Analysis

Visualizes the environmental factors contributing to the current risk.

### 3. AI Model Analysis

Displays the relative importance of the input features used by the machine-learning model.

### 4. Regional Risk Map

Provides a geographic view of risk levels across selected North Eastern locations.

### 5. Emergency Response

Ranks high-risk areas according to response priority.

### 6. Field Reporting

Allows field personnel or citizens to submit observations and photographic evidence.

### 7. Alert System

Generates warnings according to the predicted risk severity.

---

## 📂 Project Structure

```text
TERROVA-Terrain-Risk-Observation-Platform/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/maheswari755/TERROVA-Terrain-Risk-Observation-Platform.git
```

Move into the project directory:

```bash
cd TERROVA-Terrain-Risk-Observation-Platform
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The application will open locally at:

```text
http://localhost:8501
```

---

## 📦 Requirements

```text
streamlit
pandas
numpy
scikit-learn
plotly
```

---

## 🌐 Deployment

TERROVA is deployed using **Streamlit Community Cloud**.

### Live Application

**https://terrova-risk.streamlit.app/**

The application can be accessed directly through a web browser without installing the project locally.

---

## 🔮 Future Enhancements

The current version is a functional prototype. Future versions can integrate real-world data sources to improve prediction accuracy and operational usefulness.

### Planned Enhancements

* 🌦️ Real-time weather API integration
* 🛰️ Satellite imagery analysis
* 🗺️ More detailed GIS layers
* 📡 IoT soil-moisture sensor integration
* 📍 Automatic GPS-based field reporting
* 📱 SMS and mobile notifications
* 🌐 Multilingual alerts
* 📶 Offline-first field reporting
* 🧠 Advanced ML models
* 👁️ Computer vision for crack and slope analysis
* 📈 Time-series landslide forecasting
* 🛣️ Road and infrastructure vulnerability analysis

---

## ⚠️ Current Prototype Limitation

The current prototype uses **synthetic demonstration data** for model training and simulated regional risk values.

It is intended to demonstrate the complete software architecture and user workflow.

For production deployment, the model should be retrained and validated using reliable historical landslide, rainfall, terrain, soil and geospatial datasets.

---

## 🎯 Expected Impact

TERROVA aims to support disaster-management authorities by:

* Identifying vulnerable areas
* Supporting preventive monitoring
* Prioritising emergency response
* Improving situational awareness
* Providing a centralized risk dashboard
* Enabling field-level incident reporting
* Supporting faster decision-making

The ultimate objective is to move from **reactive disaster response toward predictive risk management**.

---

## 🏆 Smart India Hackathon 2026

**Problem Statement:** SIH26001

**Theme:** Disaster Management

**Problem:** AI-Based Early Warning and Landslide Risk Monitoring System in NER

**Organization:** Ministry of Development of North Eastern Region (MDoNER)

---

## 👥 Project

**TERROVA — Terrain Risk Observation & Early Warning Platform**

Built as a software prototype for **Smart India Hackathon 2026**.

---

## 📜 License

This project is intended for educational, research and hackathon purposes.
