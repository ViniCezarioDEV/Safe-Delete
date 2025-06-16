import os

FILE_NAME = os.path.basename(__file__)

def secure_delete(file_path, passes=35):
    
    with open(file_path, "rb+") as file:
        length = file.seek(0, 2)
        for _ in range(passes):
            file.seek(0)
            
            file.write(os.urandom(length))
    os.remove(file_path)
    

def get_all_files():
    all_files = os.listdir()
    if FILE_NAME in all_files:
        all_files.remove(FILE_NAME)

    return all_files

files = get_all_files()
for file in files:
    try:
        secure_delete(file)
        print(f'{file} Deleted successfully.')
    except Exception as e:
        print(f'{file} Error: {e}.')
print('\nEnd of process')