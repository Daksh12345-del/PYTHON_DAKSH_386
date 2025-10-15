#try ke saath except humesha aega error handling mein
a=(input("Enter a number between 5 and 9: "))
if a == "quit":
    print("Program terminated")
else:
    try:
        a=int(a)
        if a<5 or a>9:
            raise ValueError("The value should be betwen 5 and 9")
        print(f"You entered {a}")
    except ValueError as e:
        print("Invalid input:",e)

'''Types of Erros:
1. Syntax Error
2. Logical Error
3. Runtime Error
4. Semantic Error
5. Exception
6.Arithematic Error
7. Index Error
8. Value Error
9. Type Error
10. Name Error
11. Key Error
12. Attribute Error
13. IOError
14. Import Error
15. ZeroDivision Error
16. Module Not Found Error
17.Assertion Error
18.Attribute Error
19.EOF Error
20.Memory Error
21.Overflow Error
22.Tab Error
23.Unicode Error
24.Unbound Local Error
25.Windows Error
26.User Defined Error
27.Stop Iteration Error
28.Stop Async Iteration Error
29.Floating Point Error
30.Recursion Error
'''
