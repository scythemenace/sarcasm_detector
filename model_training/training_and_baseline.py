import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Loading my dataset
# df = pd.read_csv("../ground_labels/ground_labels_without3.csv")

df = pd.read_csv("../ground_labels/ground_labels.csv")

# Number of rows Sarcastic vs Not-Sarcastic
# print(df["label"].value_counts())

# Ideal split for our case: 70% train, 15% validation and 15% test

# First, splitting data into 70/30 - obtaining training set
train_df, temp_df = train_test_split(
    df,
    test_size=0.3,
    random_state=42,
    stratify=df[
        "label"
    ],  # stratify makes sure Sarcastic/Not-Sarcastic ratio is maintained
)

# Second, splitting remaining temp_df data into 15/15 - obtaining validation and testing set
val_df, test_df = train_test_split(
    temp_df, test_size=0.5, random_state=42, stratify=temp_df["label"]
)

# Check sizes
print(f"Train: {len(train_df)}, Validation: {len(val_df)}, Test: {len(test_df)}")

print("----------------------------------------------------------------------")

# Save splits (we’ll modify test later)
train_df.to_csv("train.csv", index=False)
val_df.to_csv("val.csv", index=False)
test_df.to_csv("test_full.csv", index=False)  # Temporary full test set

# Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer(max_features=5000, stop_words="english")

# Fit on training data and transform all sets
X_train = vectorizer.fit_transform(train_df["text"])
X_val = vectorizer.transform(val_df["text"])
X_test = vectorizer.transform(test_df["text"])

# Labels - Converting them to 0/1
y_train = train_df["label"].map({"Sarcastic": 1, "Not-Sarcastic": 0})
y_val = val_df["label"].map({"Sarcastic": 1, "Not-Sarcastic": 0})
y_test = test_df["label"].map({"Sarcastic": 1, "Not-Sarcastic": 0})

# Random predictions (0 or 1) for validation set
np.random.seed(42)
random_preds = np.random.randint(0, 2, size=len(y_val))
random_f1_val = f1_score(y_val, random_preds)
random_acc_val = accuracy_score(y_val, random_preds)
print(f"Random Baseline accuracy for validation set: {random_acc_val:.4f}")
#print(f"Random Baseline F1-score for validation set: {random_f1_val:.4f}")

# Generate for test sets as well
random_test_preds = np.random.randint(0, 2, size=len(y_test))
random_f1_test = f1_score(y_test, random_test_preds)
random_acc_test = accuracy_score(y_test, random_test_preds)
print(f"Random Baseline accuracy for test set: {random_acc_test:.4f}")
#print(f"Random Baseline F1-score for test set: {random_f1_test:.4f}")

print("----------------------------------------------------------------------")

# Majority baseline ----------------------------------------------------------------------

# Find the most common label in training data
majority_label = y_train.mode()[0]  # 0 or 1
majority_preds = [majority_label] * len(y_val)
majority_f1_val = f1_score(y_val, majority_preds)
majority_acc_val = accuracy_score(y_val, majority_preds)
print(f"Majority Baseline accuracy for validation set: {majority_acc_val:.4f}")
# majority_f1_val = f1_score(y_val, majority_preds, pos_label=0)
#print(f"Majority Baseline F1-score for validation set: {majority_f1_val:.4f}")

# Generate for test set
majority_test_preds = [majority_label] * len(y_test)
majority_f1_test = f1_score(y_test, majority_test_preds)
majority_acc_test = accuracy_score(y_test, majority_test_preds)
print(f"Majority Baseline accuracy for test set: {majority_acc_test:.4f}")
#print(f"Majority Baseline F1-score for test set: {majority_f1_test:.4f}")

print("----------------------------------------------------------------------")

# Logistic Regression ----------------------------------------------------------------------

# Train the model
model = LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42) # Without balancing results in 0
model.fit(X_train, y_train)

# Evaluate on validation set
val_preds = model.predict(X_val)
logistic_f1_val = f1_score(y_val, val_preds)
logistic_acc_val = accuracy_score(y_val, val_preds)
print(f"Logistic Regression accuracy for validation set: {logistic_acc_val:.4f}")
# print(f"Logistic Regression F1-score for validation set: {logistic_f1_val:.4f}")

# Predict on test set
test_preds = model.predict(X_test)
logistic_f1_test = f1_score(y_test, test_preds)
logistic_acc_test = accuracy_score(y_test, test_preds)
print(f"Logistic Regression accuracy for test set: {logistic_acc_test:.4f}")
# print(f"Logistic Regression F1-score for test set: {logistic_f1_test:.4f}")

print("----------------------------------------------------------------------")

# Random Forest ----------------------------------------------------------------------

# Train Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
rf_model.fit(X_train, y_train)

# Evaluate
rf_val_preds = rf_model.predict(X_val)
rf_f1_val = f1_score(y_val, rf_val_preds)
rf_acc_val = accuracy_score(y_val, rf_val_preds)
print(f"Random Forest accuracy for validation set: {rf_acc_val:.4f}")
# print(f"Random Forest F1-score for validation set: {rf_f1_val:.4f}")

rf_test_preds = rf_model.predict

# Predict on test set
rf_test_preds = rf_model.predict(X_test)
rf_f1_test = f1_score(y_test, rf_test_preds)
rf_acc_test = accuracy_score(y_test, rf_test_preds)
print(f"Random Forest accuracy for test set: {rf_acc_test:.4f}")
# print(f"Random Forest F1-score: {rf_f1_test:.4f}")