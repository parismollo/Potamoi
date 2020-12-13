import os

def delete_csv(path):
    if os.path.exists(path):
        print(f"\nFile {path} removed")
        os.remove(path)
    else:
        print(f"The file {path} does not exist")


def delete_all_csv(data_dir="data/"):
    directory_path = os.listdir(data_dir)
    for filename in directory_path:
            path = os.path.join(data_dir, filename)
            delete_csv(path)
