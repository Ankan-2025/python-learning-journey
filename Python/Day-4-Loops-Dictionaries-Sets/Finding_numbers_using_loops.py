list_of_numbers = (1,4,9,16,25,36,49,72,81,100)
n=int(input("Enter your number: "))
idx=0
for el in list_of_numbers:
    if( el == n ):
        print("Found at index:",idx)
    idx += 1