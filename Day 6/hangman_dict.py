import random
import requests

def get_word():
    response = requests.get(
        'https://www.mit.edu/~ecprice/wordlist.10000',
        timeout=10
    )
    string_of_words = response.content.decode('utf-8')
    list_of_words = string_of_words.splitlines()
    return random.choice(list_of_words)
