from github.gitRequests import request
from github.gitExceptions import requestException

class GitHub():

    def __init__(self, user: str):
        self._user = user

    def _getRepos(self):

        try:
            repos = request(user=self._user, endpoint='repos')
        except requestException as e:
            print(e.message)
            return None

        repos_list = []
        for i in range(len(repos)):
            repos_list.append(repos[i]['name'])

        return { 'repos_list': repos_list }

    def _getUser(self):

        try:
            user_info = request(user=self._user)
        except requestException as e:
            print(e.message)
            return None

        user = {
            'name': user_info['login'],
            'perfil': user_info['url'],
            'public_repos': user_info['public_repos'],
            'followers': user_info['followers'],
            'following': user_info['following']
        }
        return user

    def getUserInfo(self):
        repo = self._getRepos()
        user = self._getUser()
        if (repo and user):
            user.update(repo)
            return user
        return None