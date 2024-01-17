import os
import shutil
path = './data'
images_folder = "./data/images"
labels_folder = "./data/labels"
for file in os.listdir(path):
    if ".jpg" in file:
        shutil.move(os.path.join(path, file), images_folder)
    elif ".txt" in file:
        shutil.move(os.path.join(path, file), labels_folder)