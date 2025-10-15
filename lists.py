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
# lst=[i for i in range(4)]
# print(lst)
# lst1=[i*i for i in range(4)]
# print(lst1)
# lst2=[i*i for i in range(10) if i%2==0]
# print(lst2)



##list method in python
l=[11,66,45,69,1,2,3,4,1,1,1,]
print(l)
l.append(5) #add element at the end
print(l) 
l.sort() #sort the list in ascending order
print(l)
l.sort(reverse=True) #sort the list in descending order
print(l)
l.reverse() #reverse the list
print(l)
print(l.index(3)) #gives the index of the element
print(l.count(1)) #count the occurence of the element
m=l.copy()
m[0]=0
print(l)
l.insert(2,100) #insert element at the given index
print(l)
n=[7,8,9]
l.extend(n) #extend the list by adding elements of another list
print(l)
