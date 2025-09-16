# def average(a,b,c=1): #default arguements
#     print("The average is",(a+b+c)/2)
# average(4,6)
# average(1,5) # this is priortised firstly
# average(5,8) #value of a is privuded and b is default

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is :",sum/len(numbers))


average(4,6,7,8)

def name(**names):
    print("Hello",names["fname"],names["mname"],names["lname"])
# def name(fname,mname='john',lname="watson"):
#     print("Hello", fname,mname,lname)

# name("Amy","Agarwal","Jain")
