A= int(input("Enter your first number: "))
B=int(input("Enter your second number: "))
C=int(input("Enter your third number: "))
if(A > B and B > C):
    print(f"{A} is greatest number")
elif(B > C and B > A):
    print(f"{B} is greatest number")
elif(C > A and C > B):
    print(f"{C} is greatest number")
else:
    print("Numbers are equal")