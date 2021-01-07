import os

def make_dir():
    """
    creates directories and checks for created
    """
    try:
        for i in range(1, 10):
            os.mkdir('dir_{}'.format(i))
            print('Директория dir_{} создана'. format(i))
    except FileExistsError:
        print('Директория {} уже существует'.format(name_dir))
