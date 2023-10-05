# GitHub-repo-catcher
GitHub-repo-catcher possui a funcionalidade de buscar informações de usuários e seus repositórios consumindo a API do GitHub.

Este projeto possui uma API utilizando flask que consome a API do GitHub e retorna um arquivo em txt com as informações de usuário.

Para utilizar ela basta instalar os pacotes flask e requests com os comandos:
pip install flask
pip install requests

Para iniciar a aplicação use o comando python main.py.

Para consumir a API deve utilizar o seguinte url http://localhost:9001/download?user=<usuário desejado> substituindo o campo <usuário desejado> pelo nome de usuário do GitHub da pessoa que deseja retornar.

Caso utilize um navegador ele deve iniciar o download de um arquivo .txt com as informações, caso utilize uma ferramenta para testes como PostMan ele irá retornar um objeto json em formato de texto.
