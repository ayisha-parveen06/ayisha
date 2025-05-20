# healthcare_diagnostic.py

def get_diagnosis(symptoms):
    disease_database = {
        "Flu": {
            "symptoms": ["fever", "cough", "sore throat", "body ache"],
            "treatment": "Rest, hydration, and antiviral medication if severe."
        },
        "Common Cold": {
            "symptoms": ["sneezing", "stuffy nose", "sore throat", "mild cough"],
            "treatment": "Rest, fluids, and over-the-counter cold remedies."
        },
        "Malaria": {
            "symptoms": ["fever", "chills", "sweating", "headache", "nausea"],
            "treatment": "Antimalarial drugs prescribed by a physician."
        },
        "COVID-19": {
            "symptoms": ["fever", "dry cough", "fatigue", "loss of taste", "breathlessness"],
            "treatment": "Isolation, rest, fever reducers, and medical supervision if symptoms worsen."
        }
    }

    match_scores = {}
    for disease, info in disease_database.items():
        match_count = len(set(symptoms).intersection(info["symptoms"]))
        match_scores[disease] = match_count

    best_match = max(match_scores, key=match_scores.get)
    confidence = (match_scores[best_match] / len(disease_database[best_match]["symptoms"])) * 100

    return {
        "disease": best_match,
        "confidence": confidence,
        "treatment": disease_database[best_match]["treatment"]
    }

def main():
    print("Welcome to the Healthcare Diagnostic System")
    print("Enter your symptoms (comma separated): ")
    user_input = input().lower()
    symptoms = [s.strip() for s in user_input.split(',')]

    result = get_diagnosis(symptoms)

    print("\n--- Diagnosis Result ---")
    print(f"Disease: {result['disease']}")
    print(f"Confidence: {result['confidence']:.2f}%")
    print(f"Suggested Treatment: {result['treatment']}")

if __name__ == "__main__":
    main()
