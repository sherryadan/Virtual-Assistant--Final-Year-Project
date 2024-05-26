import pathlib

def create_folder_c(folder_name):
    try:
        (pathlib.Path("C:\\") / folder_name).mkdir()
        print(f"Folder {folder_name} created in C drive")
    except Exception as e:
        print(f"Error creating folder {folder_name} in C drive: {str(e)}")

def create_folder_d(folder_name):
    try:
        (pathlib.Path("D:\\") / folder_name).mkdir()
        print(f"Folder {folder_name} created in D drive")
    except Exception as e:
        print(f"Error creating folder {folder_name} in D drive: {str(e)}")

def create_folder_desktop(folder_name):
    try:
        (pathlib.WindowsPath.home() / 'Desktop' / folder_name).mkdir()
        print(f"Folder {folder_name} created in Desktop")
    except Exception as e:
        print(f"Error creating folder {folder_name} in Desktop: {str(e)}")