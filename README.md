# 🚗 AI-Driven Used Car Price Prediction System

---

## 🌟 Overview

Buying or selling a used car often involves uncertainty about the correct price.
This project uses **Machine Learning** to estimate the selling price of a car based on its specifications such as year, mileage, engine capacity, fuel type, ownership, and more.

👉 The system analyzes historical car data and predicts a realistic market value instantly.

---

## ✨ Key Features

✅ Predict resale price of used cars  
✅ Real-time prediction using trained ML model  
✅ User-friendly web interface (Streamlit)  
✅ Handles multiple car attributes  
✅ Dataset-driven estimation  
✅ Practical AI application for beginners  

---

## 🧠 Machine Learning Approach

* **Type:** Supervised Learning
* **Problem:** Regression
* **Algorithm Used:** Random Forest Regressor 🌳
* **Evaluation Metric:** R² Score

The model learns patterns from historical car sales data to estimate future prices.

---

## 📊 Input Parameters

The prediction is based on key car attributes:

* Manufacturing Year 📅
* Kilometers Driven 🛣️
* Engine Capacity ⚙️
* Mileage ⛽
* Maximum Power 🔥
* Number of Seats 👨‍👩‍👧‍👦
* Fuel Type (Petrol/Diesel/LPG)
* Transmission Type
* Seller Type
* Ownership History
* Car Brand

---

## 💰 Output

👉 Estimated selling price of the car (in lakhs ₹)

---

## 🖥️ Project Structure

```
Car-Price-Prediction/
│
├── car_data.csv           # Dataset
├── train.py               # Model training script
├── car_price_model.pkl    # Trained ML model
├── app.py                 # Streamlit web app
```

---

## ⚙️ Technologies Used

* 🐍 Python
* 📊 Pandas & NumPy
* 🤖 Scikit-learn
* 🌐 Streamlit
* 📉 Matplotlib / Seaborn (for analysis)

---

## 🚀 How to Run the Project

### 1️⃣ Clone or Download Repository

```bash
git clone <repository-link>
cd Car-Price-Prediction
```

---

### 2️⃣ Install Dependencies

```bash
pip install pandas numpy scikit-learn streamlit
```

---

### 3️⃣ Train the Model (Optional)

```bash
python train.py
```

This generates:

```
car_price_model.pkl
```

---

### 4️⃣ Run the Web App

```bash
streamlit run app.py
```

---

### 5️⃣ Open in Browser

If not opened automatically, visit:

```
http://localhost:8501
```

---

## 🎯 Real-World Applications

* Used car marketplaces (OLX, Cars24, etc.)
* Dealer price estimation tools
* Buyer decision support
* Market value analysis

---

## 📚 Learning Outcomes

Through this project, the following concepts were applied:

✔ Data preprocessing  
✔ Feature encoding  
✔ Model training & evaluation  
✔ Regression techniques  
✔ Model deployment with UI  
✔ End-to-end ML workflow  

---

## 👨‍🎓 Author

**Name:** Divyanshu Kumar  
**Registration no.:** 25BCE10233  
**Program:** B.Tech CSE  
**Course:** Fundamentals of AI & ML  
**University:** VIT Bhopal University  

---

## 🏁 Conclusion

This project demonstrates how Machine Learning can be applied to solve real-world problems such as estimating the resale value of used cars. By analyzing historical data and car specifications, the system provides a data-driven price prediction that can assist buyers, sellers, and dealers in making informed decisions.
The project also showcases the complete AI workflow — from data preprocessing and model training to deployment through an interactive web application.

---
