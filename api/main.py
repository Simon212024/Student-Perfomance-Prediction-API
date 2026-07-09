from fastapi import FastAPI,HTTPException
from app.predictor import predict_score
from app.schemas import StudentData
from datetime import datetime


app = FastAPI(
    app = FastAPI(
    title="Student Performance Prediction API",
    description="""
Predicts student exam scores using a trained Gradient Boosting Regressor model.

Built with:
- Scikit-learn
- FastAPI
- Pandas
- Joblib
""",
    version="1.0.0"
)

)

@app.get('/',tags=['Home'],summary='Welcome endpoint',description='Checks whether the ' \
'Student Performance API is running'
         )
def home():
    return{
        'status':'Success',
        'message': "Welcome to student performance prediction API and it's running successfully",
        'version': '1.0.0',
        'year':datetime.now().year
    }
        
@app.post("/predict",tags=['Prediction'],summary='Predicts the score',
          description= "Predicts the student's exam score using the trained machine learning model"
          )

def predict(student: StudentData):

    try:
        prediction = predict_score(student.model_dump())

        return {
            "status": "success",
            "prediction": {
                "exam_score": round(prediction, 2)
            },
            "model": "Gradient Boosting Regressor"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )
        