import datetime, requests
from secretstuff import API_KEY, APP_ID, SHEETY_USERNAME, SHEETY_BEARER

NLP_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL = f"https://api.sheety.co/{SHEETY_USERNAME}/workoutTracking/workouts"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SHEETY_BEARER}"
}

GENDER = "female"
WEIGHT_KG = 78.9
HEIGHT_CM = 167.64
AGE = 34

TODAY = datetime.datetime.now().strftime("%Y/%m/%d")
TIME = datetime.datetime.now().strftime("%H:%M:%S")
print(TODAY)
print(TIME)

exercise_input = input("Exercise?: ")

params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

response = requests.post(url=NLP_URL, json=params, headers=headers).json()

for ex in response["exercises"]:
    exercise = ex["name"].title()
    duration = int(ex["duration_min"])
    calories = int(ex["nf_calories"])
    row_data = {
        "workout": {
            "date": TODAY,
            "time": TIME,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }
    write_row = requests.post(url=SHEETY_URL, json=row_data, headers=HEADERS)
