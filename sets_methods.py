s={1,2,3,4}
s2={5,6,7,4}
print(s.union(s2)) #union dono sets ke elements ko combine kar deta hai bina repeat kiye
s.update(s2)    #update bhi union jaisa hi hai bas ye original set ko hi update kar deta hai
print(s,s2) 
print(s.intersection(s2)) #intersection dono sets ke common elements ko nikalta hai
s.intersection_update(s2) #intersection_update bhi intersection jaisa hi hai bas ye original set ko hi update kar deta hai
print(s,s2)
print(s.symmetric_difference(s2)) #symmetric_difference dono sets ke aise elements ko nikalta hai jo dono sets mein common nahi hain
s.symmetric_difference_update(s2) #symmetric_difference_update bhi symmetric_difference jaisa hi hai bas ye original set ko hi update kar deta hai
print(s,s2)
#sets mein agr koi element repeat ho to wo ek hi baar consider hota hai output mein
#aur sets unorder bhi hota hai matlab ki jis order mein apne element diye hain
s3=s.difference(s2) #difference aise elements ko nikalta hai jo pehle set mein hain lekin dusre set mein nahi hain
print(s3)
s.difference_update(s2) #difference_update bhi difference jaisa hi hai bas ye original
print(s,s2)
print(s.isdisjoint(s2)) #isdijoint check karta hai ki dono sets ke beech koi common element hai ya nahi, agar nahi hai to true return karta hai
print(s.issubset(s2)) #issubset check karta hai ki pehla set dusre set ka subset hai ya nahi
print(s.issuperset(s2)) #issuperset check karta hai ki pehla set dusre set ka superset hai ya nahi
s.add(8)
print(s)
s.remove(8) #agar element set mein nahi hai to error dega
print(s)
s.discard(8) #agar element set mein nahi hai to error nahi dega
print(s)
s.discard(7)
print(s)
items=s.pop() #pop set se random element ko remove kar deta hai aur us element ko return kar deta hai
print(items)
if 5 in s:
    print("YES")
else:
    print("NO")