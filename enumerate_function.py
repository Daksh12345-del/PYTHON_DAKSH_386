marks=[12,56,32,98,12,45,1,4]
# a=0
# for mark in marks:
#     print(mark)
#     if(a==3):
#         print("Third index reached")
#     a+=1

for index,mark in enumerate(marks,start=0):
    # enumerate function adds a counter to an iterable and returns it in a form of enumerating object
    #enmerate helps to give loop to two things at a same time
    
    print(mark)
    if(index==3):
        print("Third index reached")
        break
