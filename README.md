# Indian Liver Patient Disease Prediction Web App

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25.0-orange)](https://streamlit.io/)  
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)  

---

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Demo](#demo)  
3. [Features](#features)  
4. [Dataset](#dataset)  
5. [Installation](#installation)  
6. [Usage](#usage)  
7. [Model Details](#model-details)  
8. [Deployment](#deployment)  
9. [Future Improvements](#future-improvements)  
10. [License](#license)  

---

## Project Overview

This is a **web-based application** that predicts **liver disease** based on patient medical data.  
The app is built with **Python**, **Streamlit**, and **scikit-learn**, and provides **real-time predictions** with a modern, interactive UI.

---

## Demo

![Liver App Screenshot](https://via.placeholder.com/800x400.png?text=Liver+Prediction+App+Demo)  
*Interactive form for liver disease prediction with risk gauge.*

---

## Features

- Sleek **two-column input layout** for patient data  
- Predicts **Liver Disease** presence/absence  
- Displays **risk probability** with a dynamic gauge  
- Color-coded results:  
  - **Red** → Liver Disease Detected  
  - **Green** → No Liver Disease  
- Optional interactive charts to compare patient values to healthy ranges  
- Fully deployable to **Streamlit Cloud / Heroku**  

---

## Dataset

- **Name:** Indian Liver Patient Dataset (ILPD)  
- **Source:** [Kaggle ILPD Dataset](https://www.kaggle.com/datasets/uciml/indian-liver-patient-records)  
- **Features:** Age, Gender, Total Bilirubin, Direct Bilirubin, Alkaline Phosphotase, ALT, AST, Total Proteins, Albumin, Albumin/Globulin Ratio  
- **Target:**  
  - `1` → Liver Patient  
  - `0` → No Liver Disease  

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/liver-disease-prediction.git
cd liver-disease-prediction
