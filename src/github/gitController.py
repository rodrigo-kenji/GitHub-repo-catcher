from src.github.gitRequests import request
from src.github.gitExceptions import requestException


class GitHub():

    def __init__(self, user: str):
        self._user = user

    # Faz uso da API do GitHub para obter informações do repositório do usuário
    def _getRepos(self):

        try:
            repos = request(user=self._user, endpoint='/repos')
        except requestException as e:
            return { 'message': e.message }

        repos_list = []
        for i in range(len(repos)):
            repos_list.append(repos[i]['name'])

        return { 'lista-de-repositorios': repos_list }

    # Faz uso da API do GitHub para obter informações do usuário
    def _getUser(self):

        try:
            user_info = request(user=self._user)
        except requestException as e:
            return { 'message': e.message }

        user = {
            'nome': user_info['login'],
            'perfil': user_info['url'],
            'numero-de-repositorios-publicos': user_info['public_repos'],
            'numero-de-seguidores': user_info['followers'],
            'numero-de-usuarios-seguidos': user_info['following']
        }
        return user

    # Retorna um dicionário com as informações do usuário e seus repositórios
    def getUserInfo(self):
        repo = self._getRepos()
        user = self._getUser()
        if 'message' in user:
            return user
        if (repo and user):
            user.update(repo)
            return user
        return None