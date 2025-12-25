# ep1={122:45,123:89,69:670}
# ep2={222:67,566:90}
# ep1.update(ep2)
# print(ep1) #dictionaries mein basically key-value pairs hote hain
# # ep1.clear()
# ep1.pop(122)
# print(ep1) #dictionary ke andar value ko access karne ke liye uski key ka use karte hain
# empt={}
# ep1.popitem()#it removes the last inserted key-value pair
# print(ep1)
# # del ep1 #it deletes the entire dictionary
# del ep1[123] #it deletes the key-value pair with the specified key
# print(ep1)
# print(empt)
fact=1
num=int(input("Enter a number"))
while(num>0):
    fact=fact*num
    num-=1
print(fact)