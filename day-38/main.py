import datetime, json, requests

nx_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Continuing to use JSON so that I don't have six million env variables
with open("../info.json") as f:
    info = json.load(f)

activity = input("What activities did you do today? ")

nx_headers = {
    "x-app-id": info["nutritionix_app_id"],
    "x-app-key": info["nutritionix_api_key"]
}

nx_params = {
    "query": activity
}

response = requests.post(
    json=nx_params,
    url=nx_endpoint,
    headers=nx_headers
)
exercises = response.json()["exercises"]


sheety_workout_endpoint = info["sheety_workout_endpoint"]
sheety_workout_token = info["sheety_workout_token"]
sheety_headers = {
    "Authorization": sheety_workout_token,
}

for exercise in exercises:
    params = {
        "workout": {
            "date": datetime.datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise['name'].title(),
            "duration": int(float(exercise['duration_min'])),
            "calories": int(float(exercise['nf_calories']))
        }
    }
    print(params)
    response = requests.post(sheety_workout_endpoint, json=params, headers=sheety_headers)
    print(response.text)

