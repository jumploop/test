import os


def list_dir(dir_path):
    g = os.walk(dir_path)
    for path, dirs, files in g:
        for dir_name in dirs:
            print(os.path.normpath(os.path.join(path, dir_name)))
        for file_name in files:
            print(os.path.normpath(os.path.join(path, file_name)))


def list_dir2(dir_path):
    for file in os.listdir(dir_path):
        path = os.path.join(dir_path, file)
        if os.path.isdir(path):
            list_dir2(path)
        else:
            print(os.path.normpath(path))


if __name__ == '__main__':
    dirname = r'c:/Users/liming/Downloads/'
    # list_dir(dirname)
    list_dir2(dirname)
