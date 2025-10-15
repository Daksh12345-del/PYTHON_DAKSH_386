#agr hum lopp mein break use karte hain to else part execute nahi hota
for i in range(5):
    print(i)
else:
    print("Sorry no i")

for i in range(5):
    if i==3:
        break
    print(i)
else:
    print("Sorry no i")