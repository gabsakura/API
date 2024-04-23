import pandas as pd
import requests
import json
from openai import OpenAI

df = pd.read_csv('C:\\Users\\pedro\\OneDrive\\Área de Trabalho\\API-main\\projeto API\\abc.csv')
user_ids = df['UserID'].tolist()
openai_api_key = 'sk-proj-oAUDw1bzg33tuU5pRB09T3BlbkFJxfEiV1eIlVW6fCSzNYPT'
url = f'https://digitalinnovationone.github.io/santander-dev-week-2023-api/mocks/find_one.json?id={id}'
client = OpenAI(api_key=openai_api_key)

def get_user(id):
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None 
users = [get_user(id) for id in user_ids if get_user(id) is not None]

def generate_ai_news(user):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um especialista em marketing bancário."},
          ]
    )
    return response.choices[0].message.content.strip('\"')



for user in users:
    news = generate_ai_news(user)
    print(news)
    user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/mocks/find_one.json?id={id}'{user['id'",
      "description": news
      })

def update_user(user):
  response = requests.put(f"{'https://digitalinnovationone.github.io/santander-dev-week-2023-api/mocks/find_one.json?id={id}'}/users/{user['id']}", json=user)
  return True if response.status_code == 200 else False

for user in users:
  success = update_user(user)
  print(f"User {user['name']} updated? {success}!")
# Supondo que você tenha uma lista de IDs de usuário
# user_ids = [1, 2, 3, 4, 5]


#print(json.dumps(users, indent=2))
