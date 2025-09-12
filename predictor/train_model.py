import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("framingham.csv")

# ---- Handle Missing Values ----
df = df.fillna(df.mean(numeric_only=True))

# Features (all columns except target)
X = df.drop("TenYearCHD", axis=1)   # Target column
y = df["TenYearCHD"]

# Split into train & test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Logistic Regression
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

# Evaluate model
accuracy = model.score(X_test, y_test)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# Save the model
pickle.dump(model, open("heart_model.pkl", "wb"))
print("✅ Model trained and saved as heart_model.pkl")
