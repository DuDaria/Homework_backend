import os

def make_dir(name_dir, n):
    """
    creates directories and checks for created
    """
    try:
        for i in range(1, n):
            os.mkdir('{}_{}'.format(name_dir, i))
            print('Директория {}_{} создана'. format(name_dir, i))
    except FileExistsError:
        print('Директория {} уже существует'.format(name_dir))
