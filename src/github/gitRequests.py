import requests
from src.github.gitExceptions import requestException

def request(user: str, endpoint: str = ''):

    response = requests.get(f'https://api.github.com/users/{user}{endpoint}')
    if response.status_code == 200:
        return response.json()
    else:
        if response.status_code == 404:
            raise requestException(message='Usuário não encontrado')
        else:
            raise requestException(message='Erro na requisição')