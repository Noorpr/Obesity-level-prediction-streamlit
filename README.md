# Obesity Level Prediction using Streamlit

## 📌 Overview

This project is designed to predict the **obesity level** of a person based on various health and lifestyle factors. It utilizes a **Random Forest Classifier** trained on a dataset from **Kaggle**. The web application is built using **Streamlit**, allowing users to input their data and get an instant obesity level prediction.

## 📊 Dataset

The dataset used for this project is available on Kaggle: [Obesity Prediction Dataset](https://www.kaggle.com/datasets/ruchikakumbhar/obesity-prediction)

## 🏆 Model Performance

- **Algorithm Used:** Random Forest Classifier
- **Accuracy:** 97.1%

## ⚖️ Obesity Level Categories

The model predicts one of the following **seven obesity levels**:

1. **Normal Weight**
2. **Insufficient Weight**
3. **Overweight Level I**
4. **Overweight Level II**
5. **Obesity Level I**
6. **Obesity Level II**
7. **Obesity Level III**

## 🚀 Deployment Method

This application is deployed using **Streamlit**, making it interactive and user-friendly.

## 🔧 Setup and Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Noorpr/Obesity-level-prediction-streamlit.git
cd Obesity-level-prediction-streamlit
```

### 2️⃣ Install Dependencies

Ensure you have Python installed, then install the required dependencies:

```bash
pip install -r requirements.txt
```

*The **`requirements.txt`** file includes the following dependencies:*

- `pandas`
- `numpy`
- `streamlit`
- `joblib`
- `scikit-learn==1.5.2`

### 3️⃣ Run the Application

```bash
streamlit run main.py
```

This will start the Streamlit web application, where users can enter their details and receive an obesity level prediction.

## 📂 Project Structure

```
📁 Obesity-level-prediction-streamlit
├── 📜 main.py                 # Main Streamlit application script
├── 📜 obesity_model.pkl              # Trained machine learning model
├── 📜 requirements.txt       # Dependencies
├── 📜 README.md              # Project Documentation
```

## 🎯 Usage

1. Open the Streamlit web app.
2. Enter the required input values related to lifestyle and health.
3. Click on the **Predict** button.
4. View the predicted **obesity level** displayed on the screen.

## 🤝 Contributions

Feel free to contribute by opening issues or submitting pull requests to improve this project!

## 📜 License

This project is for educational purposes only. Feel free to use and modify it as needed.

---

📌 **Author:** [Noor Tariq](https://github.com/Noorpr)

