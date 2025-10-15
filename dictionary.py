#dictionaries mein basically key-value pairs hote hain
dic={"Harry":"Burger","Spoon":"Object"}
print(dic["Harry"]) #dictionary ke andar value ko access karne ke liye uski key ka use karte hain
print(dic)
print(dic.get("Spoon")) #get method bhi value ko access karne ke liye use hota hai
print(dic.get("Spoon2")) #agar key dictionary mein nahi hai to None return karega
print(dic.keys())   #keys method dictionary ke andar jitni bhi keys hain unko return kar deta hai
print(dic.values()) #values method dictionary ke andar jitni bhi values hain unko return kar
for keys in dic.keys():
    print(keys) #dictionary ke andar jitni bhi keys hain unko print kar dega
    print(f"the value corresponding to {keys} is {dic[keys]}") #dictionary ke andar jitni bhi keys hain unke corresponding values ko print kar dega
