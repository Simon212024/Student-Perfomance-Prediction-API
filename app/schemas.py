from pydantic import BaseModel,Field
from typing import Literal


class StudentData(BaseModel):
    Hours_Studied: int=Field(...,ge=0,le=24)
    Attendance: int=Field(...,ge=0,le=100)
    Parental_Involvement: Literal[
        'Low','Medium','High'
    ]
    Access_to_Resources: Literal[
        'Low','Medium','High'
    ]
    Extracurricular_Activities: Literal['No','Yes']
    Sleep_Hours: int=Field(...,ge=0,le=24)

    Previous_Scores: int=Field(...,ge=0,le=100)

    Motivation_Level: Literal[
        'Low','Medium','High'
    ]
    Internet_Access: Literal['Low','Medium','High']

    Tutoring_Sessions: int=Field(...,ge=0)

    Family_Income: Literal['Low','Medium','High']

    Teacher_Quality: Literal['Low','Medium','High']

    School_Type: Literal['Public','Private']
    Peer_Influence: Literal['Positive','Neutral','Negative']
    Physical_Activity: int=Field(...,ge=0)
    Learning_Disabilities: Literal['Yes','No']
    Parental_Education_Level: Literal['High School','College','Postgraduate']
    Distance_from_Home: Literal['Near','Moderate','Far']
    Gender: Literal['Male','Female']