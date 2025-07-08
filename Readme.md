# 🏠 House Price Prediction - Machine Learning Web App

This project predicts house prices in King County, USA using a trained **Random Forest Regressor** model and a **Flask web app**.

---

## 📊 Dataset

Dataset used: [kc_house_data.csv](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction)  
- Contains 21,000+ housing records.
- Includes features like bedrooms, bathrooms, sqft, location, etc.

---

##⚙️ Features

- Cleaned & preprocessed dataset (outlier removal, encoding).
- Trained **RandomForestRegressor** model with 86–87% accuracy.
- Location-based dropdown selection with lat/long and zipcode_encoded mapping.
- Fully interactive **Flask-based web UI** with dropdowns.
- Predicts house price based on 15 input features.

---

## 🚀 Tech Stack

- Python
- Pandas, NumPy, Scikit-Learn, Seaborn, Matplotlib
- Flask (Backend)
- HTML, CSS (Frontend)

---



## 🛠️ How to Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/house-price-predictor.git
   cd house-price-predictor

⚠️ Note: The trained model file `house_price_model.pkl` is not included in this repository due to file size limits.
To test the app, either train the model yourself using `train_model.py` or contact the author.
