# a=(input("Enter a number: "))
# print(f"Multiplication table of {a} is:")
# try:
#     for i in range(1,11):
#         print(f"{int(a)}X{i}={int(a)*i}")
# except Exception as e:
#     print("SORRY")

# print("Done")
# print("Thank you for using this program")



try:
    a=int(input("Enter a number: "))
    b=[6,3]
    print(b[a])
except ValueError as e:
    print("Invalid input")
except IndexError as e:
    print("Index error")
