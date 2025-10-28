import os
folders=os.listdir('data')
# print(folders)
# print(os.getcwd())
# os.chdir("/Users")
# print(os.getcwd())
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
    os.remove(f"data/{folder}")
#os.remove help to remove a file
#os.rmdir help to remove an empty folder
