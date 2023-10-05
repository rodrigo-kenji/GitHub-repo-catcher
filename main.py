from flask import Flask, request, send_file
from src.github.gitController import GitHub
from src.file_manager.createFile import txtSave


app = Flask(__name__)

@app.route('/download', methods=['GET'])
def getUserDownload():
    user = request.args.get('user')
    rep = GitHub(user)
    response = rep.getUserInfo()

    if user is None:
        return 'Usuário não informado', 400
    if 'message' in response:
        return 'Usuário não encontrado', 404
    
    file_path = txtSave(response)

    return send_file(file_path, as_attachment=True), 200

@app.route('/')
def hello():
    return 'Bem vindo a API GitHub-repo-catcher!'

if __name__ == '__main__':
    app.run(debug=False, port=9001, host='0.0.0.0')