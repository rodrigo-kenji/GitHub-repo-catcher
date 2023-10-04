import requests
from github.gitExceptions import requestException

def request(user: str, endpoint: str = ''):

    response = requests.get(f'https://api.github.com/users/{user}{endpoint}')
    if response.status_code == 200:
        return response.json()
    else:
        raise requestException(message=f'Erro na requisição status code: {response.status_code}')