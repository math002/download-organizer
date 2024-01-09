import os
import shutil
user = 'mathe'
path = f"C:/Users/{user}/Downloads"

os.mkdir(f"{path}/Img")
os.mkdir(f"{path}/Doc")
os.mkdir(f"{path}/Inst")

mydict = {
    f"{path}/Inst": ['msi','exe'],
    f"{path}/Img": ['jpg','png','gif'],
    f"{path}/Doc": ['doc','docx','pdf','xls', 'xlsx']
}

for destination, extensions in mydict.items():
    for ext in extensions:
        for file in os.listdir(f"{path}."):
            if file.endswith(f".{ext}"):
                print(file)
                shutil.move(f"{path}/{file}", destination)