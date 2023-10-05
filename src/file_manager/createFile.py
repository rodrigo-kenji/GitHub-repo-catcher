import os

# Cria um arquivo com as informações do usuário
def txtSave(user_obj):
    file_path = 'src\\output_files'

    # verifica se o diretório de destino existe, caso não, cria
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    with open(f'{file_path}\\user.txt', 'w') as f:
        f.write(str(user_obj))
    return f'{file_path}\\user.txt'