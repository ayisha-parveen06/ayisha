import time
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# 1. Accuracy Comparison and Visualization
def compare_model_accuracy_with_plot():
    data = load_breast_cancer()
    X = data.data
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Logistic Regression
    lr = LogisticRegression(max_iter=10000)
    lr.fit(X_train, y_train)
    lr_preds = lr.predict(X_test)
    lr_acc = accuracy_score(y_test, lr_preds)

    # Random Forest
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    rf_preds = rf.predict(X_test)
    rf_acc = accuracy_score(y_test, rf_preds)

    # Print report
    print("\n--- Model Accuracy Comparison ---")
    print(f"Logistic Regression Accuracy: {lr_acc:.4f}")
    print(f"Random Forest Accuracy:     {rf_acc:.4f}")

    # Confusion matrix for Random Forest
    cm = confusion_matrix(y_test, rf_preds)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix - Random Forest")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    # Bar plot of accuracy
    plt.bar(["Logistic Regression", "Random Forest"], [lr_acc, rf_acc], color=["orange", "green"])
    plt.title("Model Accuracy Comparison")
    plt.ylabel("Accuracy")
    plt.ylim(0.8, 1.0)
    plt.show()


# 2. Chatbot Latency Measurement
def chatbot_response_latency(user_input):
    start = time.time()

    if "headache" in user_input.lower():
        response = "You might have a tension headache. Try rest and hydration."
    elif "fever" in user_input.lower():
        response = "You may have an infection. Monitor temperature and consider a doctor."
    elif "hello" in user_input.lower():
        response = "Hi! How can I help you with your symptoms today?"
    else:
        response = "I'm not sure. Please provide more symptoms."

    end = time.time()
    latency = end - start

    print("\n--- Chatbot Diagnosis Response ---")
    print("Response:", response)
    print(f"Response Time: {latency:.6f} seconds")

    return latency


# 3. Real-Time IoT Data Simulation with Visualization
def simulate_iot_data():
    heart_rates = []
    temperatures = []

    print("\n--- Simulated Real-Time IoT Sensor Data ---\n")
    for i in range(10):
        hr = random.randint(60, 100)
        temp = round(random.uniform(36.0, 37.5), 2)
        heart_rates.append(hr)
        temperatures.append(temp)
        print(f"[{i+1}] Heart Rate: {hr} bpm | Temp: {temp} °C")
        time.sleep(0.5)

    # Visualization
    plt.figure(figsize=(10, 5))
    plt.plot(heart_rates, marker='o', label="Heart Rate (bpm)")
    plt.plot(temperatures, marker='x', label="Temperature (°C)")
    plt.title("Simulated IoT Sensor Data Over Time")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Measurements")
    plt.legend()
    plt.grid(True)
    plt.show()


# Main Function to Run All
def main():
    print("\n===== HEALTHCARE DIAGNOSTIC & TREATMENT PERFORMANCE =====")
    
    # 1. Accuracy comparison
    compare_model_accuracy_with_plot()

    # 2. Chatbot latency
    user_symptom = input("\nEnter your symptom for chatbot diagnosis: ")
    chatbot_response_latency(user_symptom)

    # 3. IoT data simulation
    simulate_iot_data()


if __name__ == "__main__":
    main()
