
# EduMind AI 🎓

EduMind AI is a machine learning project designed to predict whether a student will **Pass** or **Fail** based on three key inputs:
- 📘 Study Hours per Day
- 📚 Attendance Percentage
- 🎤 Participation Level (1 to 10)

---

## 🚀 Research Motivation
- Helps identify students at risk of failing at an early stage.
- Provides actionable insights for teachers and institutions.
- Supports data-driven decision-making in education.

---

## 📌 Scope
- Useful for schools, colleges, and online learning platforms.
- Analyzes academic and engagement factors together.
- Can be integrated with learning management systems (LMS).

---

## ⚙️ Installation

Clone the repository and set up the environment:

```bash
git clone https://github.com/your-username/edumind-ai.git
cd edumind-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
# venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the Flask app:

```bash
python edumind.py
```

The app will start on `http://127.0.0.1:5000/`.

---

## 📡 API Endpoint

**POST** `/predict`  
Send JSON data with the following format:

```json
{
  "study_hours": 5,
  "attendance": 85,
  "participation": 7
}
```

**Response:**
```json
{
  "prediction": "Pass"
}
```

---

## 📊 Example Block Diagram

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/a3a65d44-cde5-44b9-865e-a03de3970760" />


---
## Screenshots
<img width="1440" height="900" alt="Screenshot 2025-08-27 at 7 52 06 PM" src="https://github.com/user-attachments/assets/39bcaab3-a6ca-4d75-aecb-8fbdad2df889" />
<img width="1440" height="900" alt="Screenshot 2025-08-27 at 7 52 19 PM" src="https://github.com/user-attachments/assets/5772ae42-6b99-4e1b-af5b-83287bdfb90f" />
<img width="1440" height="900" alt="Screenshot 2025-08-27 at 7 52 35 PM" src="https://github.com/user-attachments/assets/343003f8-96b7-4d89-b20c-71e69de1880e" />
<img width="1440" height="900" alt="Screenshot 2025-08-27 at 7 52 47 PM" src="https://github.com/user-attachments/assets/8cba4633-5af1-42db-89e8-1051cfcd625b" />


---
## ✅ Objectives
1. Predict student performance using ML.  
2. Identify key academic factors affecting success.  
3. Provide a practical tool for educators.  
