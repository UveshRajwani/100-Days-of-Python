import requests
headers = {
    'Authorization': "Token ccde3efa24b64ed7e76b535015e471b705e5ed4a"
}
user_input = input("please enter the word to get its definition ")
api = requests.get(headers=headers,url=f"https://owlbot.info/api/v4/dictionary/{user_input}")
print(api.json()['definitions'][0]['definition'])