import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/trainers'
TOKEN = 'c3538b5f165ded8a3593d2ad990c91df'
HEADER = {'Content-Type': 'application/json','trainer_token':TOKEN}
TRAINER_ID = '8310'

def test_status_code():
    response = requests.get(url = f'{URL}', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200


URL = 'https://api.pokemonbattle.ru/v2/me'

def test_name_trainer():
    response = requests.get(url = f'{URL}', headers = HEADER)
    


