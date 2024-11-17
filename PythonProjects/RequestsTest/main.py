import requests

URL = 'https://api.pokemonbattle.ru/v2/pokemons'
TOKEN = 'c3538b5f165ded8a3593d2ad990c91df'
HEADER = {'Content-Type': 'application/json','trainer_token':TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}   

body_change = {

    "pokemon_id": "60321",
    "name": "New Name",
    "photo_id": 2
}


'''response_create = requests.post(url = f'{URL}', headers = HEADER, json = body_create) 
print(response_create.text)'''


'''response_change = requests.put(url = f'{URL}', headers = HEADER, json = body_change) 
print(response_change.text)'''


URL ='https://api.pokemonbattle.ru/v2/trainers/add_pokeball'

body_cath = {
        "pokemon_id": "60321"
}

response_cath = requests.post(url = f'{URL}', headers = HEADER, json = body_change) 
print(response_cath.text)