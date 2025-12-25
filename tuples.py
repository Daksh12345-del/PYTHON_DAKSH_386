# #introduction to tuple
tuple=(1,5,6)
tuple1=(1,)
# tuple[0]=100  #it will give error as tuple is immutable
print(type(tuple),tuple)
print(type(tuple1),tuple1)#tuple with single element so we have to put comma after the element rather it will show type as int.
print(len(tuple))
print(tuple[0])
print(tuple[1])
print(tuple[2])
if 5 in tuple:
    print("YES")
# tuple2=tuple[0:3] #slicing
# print(tuple2)


# operations on tuple
countries=("India","USA","China","Russia")
temp=list(countries) #converting tuple to list
temp.append("Nepal")
temp.pop(3) #removing element at index 3
temp[0]="Bhutan" #modifying element at index 0
a=tuple(temp) #converting list back to tuple
print(a)


countries=("India","USA","China","Russia","India","India")
countries2=("Bhutan","Nepal")
countries3=countries+countries2 #concatenation of tuples
print(countries3)

tuple1=(1,2,3,4,5,6,7,8,9,1,1,1,1)
res=tuple1.count(1) #counting occurence of element
res1=tuple1.index(1) #finding index of first occurence of element
res2=tuple1.index(1,1,12) #finding index of first occurence of element after index 1
res3=len(tuple1) #length of tuple
print(res3)
print(res1)
print(res)
print(res2)
