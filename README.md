# 🧠 Smart Stress Monitoring System

> **AI-powered Stress Detection using Facial Emotion Recognition, Vital Signs Estimation, and Questionnaire Analysis for Mental Well-being.**

![Project Poster](screenshots/project-poster.png)

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?logo=tensorflow)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?logo=mysql)
![License](https://img.shields.io/badge/Academic-Project-success)

---

# 📖 Project Overview

The **Smart Stress Monitoring System** is an AI-powered web application developed to monitor and predict stress levels by combining **facial emotion recognition**, **estimated vital signs**, and **questionnaire analysis**.

The system captures facial expressions through a webcam, estimates physiological indicators such as **heart rate**, **blink rate**, **respiratory rate**, and **blood pressure**, combines these with questionnaire responses, and predicts the user's stress level as:

- 🟢 Low Stress
- 🟡 Moderate Stress
- 🔴 High Stress

Based on the prediction, the application provides personalized wellness recommendations to help improve mental well-being.

This project was developed as part of the **AI & ML In-House Internship Project (2026)** at **Aditya University**.

---

# ✨ Features

- 🔐 Secure User Registration & Login
- 😀 Facial Emotion Recognition
- ❤️ Vital Signs Estimation
- 📝 Dynamic Stress Questionnaire
- 🧠 AI-Based Stress Prediction
- 📊 Dashboard & Analytics
- 📈 Stress Reports & History
- 💡 Personalized Wellness Recommendations
- 👤 User Profile Management

---

# 🏗️ System Architecture

![Architecture](screenshots/system-architecture.png)

---

# 🧠 Algorithms Used

![Algorithms](screenshots/algorithms-used.png)

---

# 🛠️ Technologies Used

## Frontend

- HTML5
- CSS3
- JavaScript
- React.js
- Bootstrap

## Backend

- Python
- Flask

## Database

- MySQL

## AI / Machine Learning

- TensorFlow
- Keras
- OpenCV
- ResNet50 (CNN)
- TensorFlow Lite (Android Deployment)

## Android Application

- Android Studio
- Java
- XML
- HTML, CSS & JavaScript (embedded in WebView)
- WebView
- Firebase Authentication
- Google ML Kit Face Detection
- TensorFlow Lite (Quantized Model)
- Android SDK
- PDF Document API
- LocalStorage

---

# 📸 Application Screenshots

## 🔐 Login Page

![Login](screenshots/login-page.png)

---

## 📊 Dashboard

![Dashboard](screenshots/dashboard.png)

---

## 📷 Face Scan

![Face Scan](screenshots/face-scan.png)

---

## 📝 Questionnaire

![Questionnaire](screenshots/questionnaire.png)

---

## 📈 Reports

![Reports](screenshots/reports.png)

---

## 💡 Recommendations

![Recommendations](screenshots/recommendations.png)

---

# 📂 Project Structure

```text
smart-stress-monitoring-system
│
├── app.py
├── requirements.txt
├── smart_stress_database.sql
├── convert_tflite.py
│
├── static/
├── templates/
├── screenshots/
├── Reports/
├── PPT's/
└── models/
```

---

# 🤖 AI Models

The project uses a deep learning model for facial emotion recognition.

## Web Application

- **ResNet50 Emotion Recognition Model (.keras)**

## Android Application

- emotion_model.tflite
- emotion_model_quant.tflite

The TensorFlow Lite models were generated from the trained ResNet50 Keras model for optimized on-device inference in the Android application.

> **Note:**  
> The trained model files are not included in this repository because they exceed GitHub's file size limitations.

---

# 📱 Android Companion Application

An Android version of the Smart Stress Monitoring System was also developed to provide mobile access to the application.

### Features

- Secure user authentication using Firebase Authentication
- Face detection using Google ML Kit
- Emotion recognition using TensorFlow Lite (Quantized Model)
- Questionnaire-based stress assessment
- Stress reports and recommendations
- Report generation using Android PDF Document API
- Local data management using LocalStorage
- WebView integration for web-based modules

The Android application serves as a mobile companion to the web application, offering the same AI-based stress assessment workflow with an optimized mobile user experience.

---

# 📄 Documentation

- 📑 **Project Report:** `Reports/Smart_Stress_Monitoring_System_Report.pdf`
- 🎤 **Project Presentation:** `PPT's/Smart_Stress_Monitoring_System_Presentation.pptx`

---

# 👥 Team

- **Biruda Purnima Pavani Ganga**
- Aatla Pavani
- Buragani Navya
- Challa Sreeya

**Repository Maintainer:**  
**Biruda Purnima Pavani Ganga**

### 👨‍🏫 Guide

- Dr. T. Chandrasekhar

### 👨‍🏫 Co-Guide

- Mr. L. Dasaradha Ramayya

---

# 🚀 Future Improvements

- ☁️ Cloud Deployment
- 📱 Full Android Application Release
- 🔔 Real-time Notifications
- 🩺 Doctor Consultation Module
- ⌚ Wearable Device Integration
- 📊 Advanced AI Analytics

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

# 📧 Contact

**Biruda Purnima Pavani Ganga**

AI & ML Undergraduate  
Aditya University

**GitHub:** https://github.com/pavanibiruda

**Repository:** https://github.com/pavanibiruda/smart-stress-monitoring-system
