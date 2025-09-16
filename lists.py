# l=[3,5,6,"Daksh",True,5.6,345,'ksh',234]
# print(l)
# print(type(l))
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])
# print(l[5])

# print(l[-3]) #negative indexing
# print(l[len(l)-3]) #positive indexing
# print(l[2:5]) #slicing
# print(l[5-3]) #positive indexing

# if 5 in l:
#     print("YES")
# else:
#     print("NO")

#same things apply for stirng as well
# if "ksh" in "Daksh":
#     print("YES")
# else:
#     print("NO")

# print(l)
# print(l[1:-1])
# print(l[1:8:2])


#this is important to understand
lst=[i for i in range(4)]
print(lst)
lst1=[i*i for i in range(4)]
print(lst1)
lst2=[i*i for i in range(10) if i%2==0]
print(lst2)