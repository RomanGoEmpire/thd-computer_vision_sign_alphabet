import os
import shutil

source_dir = "data"
DATA_DIR = 'dataset5'

# for i in range(25):
#     os.makedirs(os.path.join(source_dir, str(i)))
# #
for dir_ in os.listdir(DATA_DIR):
    for user in os.listdir(os.path.join(DATA_DIR, dir_)):
        for img_path in os.listdir(os.path.join(DATA_DIR, dir_, user)):
            x = img_path.split("_")
            if x[0] == "color":
                os.rename(os.path.join(DATA_DIR, dir_, user, img_path), os.path.join(DATA_DIR, dir_, user, f"{dir_}_{img_path}"))
                new_name = f"{dir_}_{img_path}"
                source_directory = os.path.join(os.path.join(DATA_DIR, dir_, user), new_name).replace("\\", "/")
                destination_directory = os.path.join(source_dir, x[1]).replace("\\", "/")

                shutil.move(source_directory, destination_directory)
