import os


directory_path = "./layers/"

directory = os.listdir(directory_path)

new_read_me = directory_path + "README.md"
text = ""
for file in directory:
    if (".jpeg" in file):
        text += '<p align="center">  <img src="'+file+'?"> </p>'
        text += '<p align="center">'+file+'</p>'
        text += "\n\n***\n\n"
print(text)
file = open(new_read_me, "w")
file.write(text)
