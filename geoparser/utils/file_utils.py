import os


def dir_exists(dir_name):
    if not os.path.exists(dir_name):
        return False

    if os.path.isfile(dir_name):
        return False

    return True

def file_exists(file_name):
    if not os.path.exists(file_name):
        return False

    if not os.path.isfile(file_name):
        return False

    return True

def create_folder(folder):
    os.makedirs(folder, exist_ok= True)

def get_files_in_folder(folder):
    files = os.listdir(folder)

    result = {}

    for file in files:
        result[file] = {
            "fileName": file,
            "filePath": os.path.join(folder, file)
        }

    print(result)

    return result