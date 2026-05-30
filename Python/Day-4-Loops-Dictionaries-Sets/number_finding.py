list = (1,4,9,16,25,36,49,72,81,100)
n= int(input("Enter you number: "))
i=0
while i < len(list):
    if(list[i] == n):
        print("Found at idx list", i)
    i += 1