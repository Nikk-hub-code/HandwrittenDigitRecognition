# Handwritten Digit Recognition 🚀

A Deep Learning-based Handwritten Digit Recognition system built using **TensorFlow/Keras**, **CNN (Convolutional Neural Network)**, and **Flask**.  
This project can recognize handwritten digits (0–9) from uploaded images with high accuracy using the famous MNIST dataset.

---

# 📌 Project Overview

This project demonstrates a complete end-to-end AI workflow:

- Image preprocessing
- CNN model training
- Model evaluation
- Flask web deployment
- Real-time digit prediction

The system takes an uploaded handwritten digit image and predicts the corresponding digit using a trained deep learning model.

---

# 🧠 Technologies Used

- Python
- TensorFlow / Keras
- CNN (Convolutional Neural Network)
- Flask
- OpenCV
- NumPy
- Matplotlib
- HTML

---

# 📂 Project Structure

```text
HandwrittenDigitRecognition/
│
├── dataset/
│   └── raw/
│
├── models/
│   └── digit_model.h5
│
├── notebooks/
│   └── training.ipynb
│
├── app/
│   ├── __init__.py
│   ├── app.py
│   │
│   ├── static/
│   │   └── uploads/
│   │
│   └── templates/
│       └── index.html
│
├── utils/
│   ├── __init__.py
│   └── preprocess.py
│
├── requirements.txt
├── README.md
└── main.py
```

---

# 🔥 Features

✅ Handwritten digit recognition using CNN  
✅ Real-time image upload prediction  
✅ Flask web application integration  
✅ Image preprocessing pipeline  
✅ Deep learning model training and evaluation  
✅ High prediction accuracy (~98–99%)  
✅ End-to-end AI deployment workflow  

---

# 🖼️ How It Works

```text
User Uploads Image
        ↓
Image Preprocessing
        ↓
CNN Model Prediction
        ↓
Predicted Digit Displayed
```

---

# 🧠 CNN Architecture

The model uses a Convolutional Neural Network consisting of:

- Conv2D Layer
- ReLU Activation
- MaxPooling Layer
- Flatten Layer
- Dense Hidden Layer
- Softmax Output Layer

---

# 📊 Model Performance

| Metric | Value |
|---|---|
| Training Accuracy | ~99% |
| Validation Accuracy | ~98% |
| Dataset | MNIST |
| Classes | 10 Digits (0–9) |

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Nikk-hub-code/HandwrittenDigitRecognition.git
```

---

## 2️⃣ Navigate to Project Directory

```bash
cd HandwrittenDigitRecognition
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash
.\venv\Scripts\Activate.ps1
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Run Flask Application

From project root directory:

```bash
python -m app.app
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# 🏋️‍♂️ Train the Model

Open Jupyter Notebook:

```bash
jupyter notebook
```

Then run:

```text
notebooks/training.ipynb
```

---

# 📸 Input Image Requirements

- Handwritten single digit
- Preferably centered
- Supported formats:
  - PNG
  - JPG
  - JPEG

---

# 📈 Future Improvements

- Drawing canvas support
- Real-time prediction
- Streamlit deployment
- Better UI/UX
- Real-world handwriting optimization
- Multi-digit recognition
- Mobile-friendly interface

---

# 🎯 Learning Outcomes

This project helped in understanding:

- CNN architecture
- Image preprocessing
- Deep learning workflow
- Model deployment
- Flask integration
- Computer vision fundamentals

---

# 🤝 Contributing

Contributions are welcome.  
Feel free to fork this repository and improve the project.

---

# 📜 License

This project is for educational and learning purposes.

---

# 👨‍💻 Author

## Kaushal Kumar Jha

AI/ML Enthusiast | Deep Learning Learner
