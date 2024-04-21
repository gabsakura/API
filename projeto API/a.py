import pandas as pd
import requests
import json
df = pd.read_csv('abc.csv')
user_ids = df['UserID'].tolist()

def get_user(id):
    url = f'https://digitalinnovationone.github.io/santander-dev-week-2023-api/mocks/find_one.json?id={id}'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

# Supondo que você tenha uma lista de IDs de usuário
#user_ids = [1, 2, 3, 4, 5]

users = [get_user(id) for id in user_ids if get_user(id) is not None]
print(json.dumps(users, indent=2))
