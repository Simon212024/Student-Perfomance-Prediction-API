from pathlib import Path
import joblib
import pandas as pd

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Model path
MODEL_PATH = BASE_DIR / "models" / "StudentPerformancePrediction.pkl"

# Load model
model = joblib.load(MODEL_PATH)

def predict_score(student):
    df = pd.DataFrame([student])
    prediction = model.predict(df)
    return prediction[0]