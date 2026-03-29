#Basically shutil module is used to perform high level operations on files and collections of files. It provides a number of functions that allow you to copy, move, rename, and delete files and directories.
#it mainly focuses on copying 1000 files from one position to another
import shutil
# shutil.copy("shutile_module.py","copy_shutile_module.py") #it will copy the file and create a new file with the name copy_shutile_module.py
# shutil.move("copy_shutile_module.py","new_copy_shutile_module.py") #it
shutil.copytree("shutil_folder","new_shutil_folder") #it will copy the whole folder and create a new folder with the name new_shutil_folder