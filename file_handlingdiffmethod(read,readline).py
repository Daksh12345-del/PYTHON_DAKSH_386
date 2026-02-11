#readline() method example
#splitting the lines based on comma separator 
# f=open('file.txt','r')
# i=0
# while True:
#     i=i+1
#     line=f.readline() #readline() - Reads a single line from a file. and for multiple lines give the space after a line
#     if not line:
#         break
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     print(f"Marks1:{m1} Marks2:{m2} Marks3:{m3}")
#     print(line)
#     # if not line:
#     #     print(line,type(line))
#     #     break

##writeline method example
# f=open('file.txt1','w')
# lines=["This is first line\n","This is second line\n","This is third line\n"]
# f.writelines(lines) #writelines() - Writes a list of strings to a file.
# f.close()
# txt="hello, welcome to python programming."
# txt=txt.capitalize()
# print(txt)
from turtle import mainloop
import happy_new_year as hp

2026= hp(title="Happy New Year 2026")

2026.happiness = hp.Happiness(level="temporary")
2026.sadness   = hp.Sadness(cause="carried_from_2025")
2026.hope      = hp.Hope(enabled=True)
2026.reality   = hp.Reality(force=True)
2026.mainloop()