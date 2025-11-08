# with open('file.txt','r') as f: # Open a file in read mode
#     print(type(f)) #type=_io.TextIOWrapper means it is a text file object which is used to read and write text files.
#     f.seek(5) #seek() - Moves the file pointer to a specified position (5th byte here) and then the counter starts from there.
#     print(f.tell()) #tell() - Returns the current position of the file pointer (which is 5 here).
#     content = f.read(5) #read() - Reads the content of the file from the current
#     print(content)
#     f.close() #close() - Closes an open file, freeing up system resources.

with open('file.txt','w') as f: # Open a file in write mode
    f.write("Hello, World! --- IGNORE ---\n") #write() - Writes a specified string to the file.
    f.truncate(50) #truncate() - Resizes the file to a specified size (5 bytes here).
    f.close() #close() - Closes an open file, freeing up system resources.
with open('file.txt','r') as f: # Open a file in read mode
    print(f.read())
    f.close() #close() - Closes an open file, freeing up system resources.