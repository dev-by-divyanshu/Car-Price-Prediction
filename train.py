import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_csv("car_data.csv")

# Convert categorical columns to numeric
data = pd.get_dummies(data, drop_first=True)

# Features and target
X = data.iloc[:, :-1]   # all columns except last
y = data.iloc[:, -1]    # last column = price

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Evaluate
pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, pred))

# ⭐ SAVE MODEL + COLUMNS
with open("car_price_model.pkl", "wb") as f:
    pickle.dump((model, X.columns), f)

print("Model saved successfully!")