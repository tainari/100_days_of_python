import requests

def get_questions():
    request = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
    question_data = request.json()["results"]
    return question_data

question_data = get_questions()