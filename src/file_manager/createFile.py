import os

def txtSave(user_obj):
    file_path = 'src\\output_files'

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    with open(f'{file_path}\\user.txt', 'w') as f:
        f.write(str(user_obj))
    return f'{file_path}\\user.txt'