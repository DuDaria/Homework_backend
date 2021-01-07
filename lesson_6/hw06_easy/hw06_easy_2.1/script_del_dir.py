import os

def del_dir():
    """
    creates directories and checks for created
    """
    try:
        for i in range(1, 10):
            os.rmdir('dir_{}'.format(i))
            print('Директории dir_{} удалены'. format(i))
    except FileExistsError:
        print('Директории dir уже удалены')