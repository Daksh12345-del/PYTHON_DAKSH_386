# #File handling methods are built-in functions in Python that allow you to create, read, write, and manipulate files on your computer. Here are some common file handling methods:
#READ MODE
# f=open('file.txt','r') # Open a file in read mode
# f=open('file.txt1','w') # Open a file in write mode and automatically creates the file if it does not exist
# #open() - Opens a file and returns a file object in different modes (read, write, append, etc.).
# # print(f)
# text=f.read() #read() - Reads the entire content of a file as a single string.
# print(text)
# f.close() #close() - Closes an open file, freeing up system resources.


# #WRITE MODE
# f=open('file.txt','w')# Open a file in write mode and automatically creates the file if it does not exist
# f.write("Hello, World!\n") #write() - Writes a string to a file and it will overwrite its earlier content
# f.close() #close() - Closes an open file, freeing up system resources.

with open('file.txt','a') as f: # Open a file in append mode and automatically creates the file if it does not exist
    f.write("Welcome to Python file handling.\n") #append() - Adds content to the end of a file without overwriting existing content.
    f.close() #close() - Closes an open file, freeing up system resources.