import requests
from urllib.parse import urlencode

OAUTH_URL = 'https://oauth.vk.com/authorize'
USER_URL = 'https://vk.com/id'
APP_ID = input('Ввведите id приложения')

auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'status, friends, users',
    'response_type': 'token',
    'v': 5.92
}

TOKEN = input('Введите токен:')

print('?'.join((OAUTH_URL, urlencode(auth_data))))


class User:
    def __init__(self, id):
        self.id = id

    def get_params(self):
        return {
            'user_id': self.id,
            'user_ids': self.id,
            'access_token': TOKEN,
            'v': 5.92
        }

    def get_friends(self):
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params
        )
        return response.json()

    def get_users(self):
        params = self.get_params()
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params
        )
        return response.json()

    def __str__(self):
        return (USER_URL + str(self.get_users()['response'][0]['id']))

    def __and__(self, other):
        return list(set(self.get_friends()['response']['items'])& set(other.get_friends()['response']['items']))


user1_id = input('Введите id первого пользоваетеля:')
user1 = User(int(user1_id))
user2_id = input('Введите id второго пользоваетеля:')
user2 = User(int(user2_id))

print(user1 & user2)
print(user1)
