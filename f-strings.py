#f wale mein {} yeh zaroori hai
#f wale mein hum variable ko direct use kar sakte hain
#f humesha string hi deta hai
letter="Hey my name is {0} and i am from {1}"
country="USA"
name="John"
# country="USA"
print(letter.format(name,country))
print(letter.format(country,name))
print(f"hey my name is {name} and my country is {country}")
txt="The price is {price:.2f} dollars"
print(txt.format(price=49.99999))
print(type(f"{2*30}"))