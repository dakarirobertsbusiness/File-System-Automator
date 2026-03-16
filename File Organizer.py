import os
import shutil
path="C:/Lab"
files=os.listdir(path)
for file in files:
    name,extension=os.path.splitext(file)
    print(f"Checking file: {name} with extension: {extension}")
    if extension==".pdf":
        old_path=os.path.join(path,file)
        new_path=os.path.join(path,"PDFs",name)
        shutil.move(os.path.join(path,file), os.path.join(path, "PDFs", file))
        print(f"Moved{file}to the PDF folder")
    elif extension==".png" or extension==".jpg" or extension==".jpeg":
        shutil.move(os.path.join(path,file), os.path.join(path, "Images", file))
        print(f"Moved Image: {file}")
