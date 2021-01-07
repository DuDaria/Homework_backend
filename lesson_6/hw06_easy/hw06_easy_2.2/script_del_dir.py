import os

def del_dir(name_dir, n):
    """
    del directories and checks for del
    """
    try:
        for i in range(1, n):
            os.rmdir('{}_{}'.format(name_dir, i))
            print('Директории {}_{} удалены'. format(name_dir, i))
    except FileExistsError:
        print('Директории {} уже удалены'.format(name_dir))